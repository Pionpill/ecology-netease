from functools import reduce
import math
import operator
import random
from time import time
import mod.server.extraServerApi as serverApi

from scripts.common.enum import Period
from scripts.common import logger
from scripts.common.entity import Crop, Land
from scripts.common.utils import itemUtils
from scripts.common.utils import mathUtils
from scripts.common.utils import positionUtils
from scripts.crop.server.utils import cropUtils
from scripts.ecology.server.entity.Ecology import DynamicEcology
from scripts.ecology.server.facade import EcologyFacade
from scripts.ecology.server.service.FrameService import FrameService

levelId = serverApi.GetLevelId()
engineCompFactory = serverApi.GetEngineCompFactory()
gameComp = engineCompFactory.CreateGame(levelId)
blockEntityDataComp = engineCompFactory.CreateBlockEntityData(levelId)
blockInfoComp = engineCompFactory.CreateBlockInfo(levelId)
itemComp = engineCompFactory.CreateItem(levelId)
weatherComp = engineCompFactory.CreateWeather(levelId)


class CropManager(object):
    """作物管理类"""
    def __init__(self, position, dimensionId):
        # type: (tuple[int, int, int], int) -> None
        object.__init__(self)
        self.position = position
        self.dimensionId = dimensionId
        self.RenewCropInfo()
        self.RenewLandInfo()
        if not self.cropBlockName:
            return
        seedKey = cropUtils.GetSeedKey(self.cropBlockName)
        crop = Crop.FromSeedKey(seedKey)
        if crop is None:
            logger.error('无法通过 {} 获取作物实例'.format(seedKey))
            return
        self.crop = crop
        self.ecology = EcologyFacade.GetEcologyManager(position, dimensionId)
        # 右键和左键方块都可以收获作物，该变量用于防止收获多次
        self.lastHarvestTime = None
        # 作物生长替换原本方块会触发 BlockRemoveServerEvent 事件，用于标记是否为生长导致
        self.growBlockRemove = False

    def CanGrow(self):
        """判断能否生长"""
        if self.crop.IsLastStage(self.cropStage):
            return False
        if not self.__CanGrowDuringPeriod():
            return False
        if not self.__CanGrowOnBlock():
            return False
        ecologyInfo = self.ecology.GetDynamicEcology()
        temperature = ecologyInfo.GetAdjustTemperature()
        if not mathUtils.between(temperature, self.crop.GetGrowTemperature('can')):
            return False
        rainfall = ecologyInfo.GetAdjustRainfall()
        if not mathUtils.between(rainfall, self.crop.GetGrowRainfall('can')):
            return False
        brightness = blockInfoComp.GetBlockLightLevel(self.position, self.dimensionId)
        if not mathUtils.between(brightness, self.crop.GetGrowBrightness('can')):
            return False
        return True
    
    def Grow(self):
        """作物生长"""
        cropEntityData = self.__GetCropEntityData()
        if not self.cropBlockName or not cropEntityData:
            logger.error('不存在作物 {} 实体数据'.format(self.cropBlockName))
            return
        
        tickCount = self.GetStageTickCount()
        if not tickCount:
            return
        if not self.CanGrow():
            return

        ratioTuple = self.__CalculateRatio().values()
        tickRatio = reduce(operator.mul, ratioTuple, 1)
        growTicks = mathUtils.GetRandomInteger(tickRatio)

        blockTick = cropEntityData['tick'] or 0
        blockTickCount = cropEntityData['tickCount'] or 0
        blockFertility = cropEntityData['fertility'] or 0
        nextTick = growTicks + blockTick

        # 生长，但不进入下一阶段
        if nextTick < tickCount:
            cropEntityData['tick'] = nextTick
            cropEntityData['tickCount'] = blockTickCount + 1
            cropEntityData['fertility'] = blockFertility + self.__GetGrowFertility() * growTicks
            return
        
        if not self.CanGrowToStage(self.__GetStage() + 1):
            return

        blockHarvestCount = cropEntityData['harvestCount'] or 0
        nextBlockName = self.GetCropBlockName(self.__GetStage() + 1)
        nextBlock = {"name": nextBlockName, "aux": 0}
        self.growBlockRemove = True
        blockInfoComp.SetBlockNew(self.position, nextBlock, dimensionId=self.dimensionId)
        cropEntityData = self.__GetCropEntityData()
        if cropEntityData is None:
            logger.error('生长后 {} 无法获取实体数据'.format(nextBlock.get('name', self.cropBlockName)))
            return
        cropEntityData['tick'] = nextTick - tickCount
        cropEntityData['tickCount'] = blockTickCount + 1
        cropEntityData['fertility'] = blockFertility + self.__GetGrowFertility()
        cropEntityData['harvestCount'] = blockHarvestCount
        self.RenewCropInfo()

    def Harvest(self, remove = False, loot = True):
        # type: (bool, bool) -> bool
        """
        收获作物
        
        :param remove: 是否删除作物，否则尝试多次收获
        :param loot: 是否生成凋落物
        """
        now = time()
        # 防止重复收获
        if self.lastHarvestTime is not None and now - self.lastHarvestTime < 1:
            return False
        if self.cropBlockName is None:
            return False
        canGrow = self.crop.CanGrow()
        if canGrow:
            harvestStages = self.crop.GetGrowHarvestStage()
            stage = self.__GetStage()
            if stage not in harvestStages:
                return False

        self.lastHarvestTime = now
        if loot:
            self.SpawnLoots()

        if remove or not canGrow:
            result = blockInfoComp.SetBlockNew(self.position, {'name': 'minecraft:air', 'aux': 0}, dimensionId = self.dimensionId)
            if not result:
                logger.error('发生了不可能出现的错误，收获作物失败')
                return False
        else:
            returnStage = self.crop.GetGrowHarvestReturn()
            harvestCount = self.crop.GetGrowHarvestCount()
            cropEntityData = self.__GetCropEntityData()
            if cropEntityData is None:
                return False
            blockHarvestCount = cropEntityData['harvestCount'] or 0
            if returnStage < 0 or blockHarvestCount + 1 == harvestCount:
                blockInfoComp.SetBlockNew(self.position, {"name": "minecraft:air", "aux": 0}, dimensionId = self.dimensionId)
                return True

            newBlockDict = {"name": self.GetCropBlockName(returnStage), "aux": 0}
            blockTickCount = cropEntityData['tickCount'] or 0
            blockFertility = cropEntityData['fertility'] or 0
            result = blockInfoComp.SetBlockNew(self.position, newBlockDict, dimensionId = self.dimensionId)
            cropEntityData = self.__GetCropEntityData()
            if cropEntityData is None:
                return False
            self.RenewCropInfo()
            cropEntityData['tickCount'] = blockTickCount
            cropEntityData['fertility'] = blockFertility
            cropEntityData['harvestCount'] = blockHarvestCount + 1
            if not result:
                logger.error('发生了不可能出现的错误，收获作物失败')
                return False
        return True

    def SpawnLoots(self):
        stageId = self.__GetStage()
        loots = self.crop.GetLoots(stageId)
        if loots is None:
            return
        for loot in loots:
            if random.random() * 100 > loot.chance:
                continue
            cropEntityData = self.__GetCropEntityData()
            if cropEntityData is None:
                if not self.crop.CanGrow():
                    count = mathUtils.GetRandomInteger(loot.count)
                    itemDict = itemUtils.GetItemDict(loot.itemName, 0, count)
                    itemComp.SpawnItemToLevel(itemDict,  self.dimensionId, self.position)
                continue
            fertility = cropEntityData['fertility']
            tickCount = cropEntityData['tickCount']
            avgFertility = 1 + (fertility / tickCount) / 100 if fertility and tickCount else 1
            count = mathUtils.GetRandomInteger(loot.count * avgFertility)
            itemDict = itemUtils.GetItemDict(loot.itemName, 0, count)
            if itemDict:
                itemComp.SpawnItemToLevel(itemDict,  self.dimensionId, self.position)
        
    def GetStageTickCount(self):
        """获取作物块进入下一阶段所需要 tick 总数"""
        stageId = self.__GetStage()
        return self.crop.GetGrowStageInfo(stageId).tick

    def CanGrowToStage(self, stage = None):
        # type: (int | None) -> bool
        """能否进入下一阶段：上方是否有遮挡物"""
        stage = stage or self.__GetStage()
        nextStageInfo = self.crop.GetGrowStageInfo(stage)
        nextStageHeightTuple = nextStageInfo.height
        nextStageHeight = int(math.ceil(float(nextStageHeightTuple[0]) / nextStageHeightTuple[1]))
        for offset in range(1, nextStageHeight):
            position = positionUtils.GetAbovePosition(self.position, offset)
            blockName = blockInfoComp.GetBlockNew(position, self.dimensionId).get('name')
            if blockName is not None and blockName != 'minecraft:air':
                return False
        return True

    def CanHarvest(self):
        """判断是否可以收获"""
        stage = self.__GetStage()
        harvestStages = self.crop.GetGrowHarvestStage()
        return stage in harvestStages
    
    def GetHarvestStage(self):
        """获取收获后返回的状态"""
        return self.crop.GetGrowHarvestReturn()
        
    def GetCropBlockName(self, stage):
        # type: (int) -> str
        blockPrefix = self.crop.GetBlockPrefix()
        return blockPrefix + '_stage_' + str(stage)

    def RenewCropInfo(self):
        """更新作物信息：作物生长，收获时调用"""
        blockInfo = blockInfoComp.GetBlockNew(self.position, self.dimensionId)
        cropBlockName = blockInfo.get('name')
        self.cropBlockName = cropBlockName
        if self.cropBlockName is None:
            logger.error('无法获取位置：{}的作物信息'.format(self.position))
            return
        self.cropAux = blockInfo.get('aux', 0)
        self.cropStage = self.__GetStage()

    def RenewLandInfo(self):
        """更新土地信息：实例化与底部方块变化时调用"""
        landPosition = positionUtils.GetBelowPosition(self.position)
        landInfo = blockInfoComp.GetBlockNew(landPosition, self.dimensionId)
        self.landName = landInfo.get('name')
        self.landAux = landInfo.get('aux')
        self.land = Land.FromBlockName(self.landName) if self.landName else None

    def GetGrowInfo(self):
        ecologyInfo =self.ecology.GetDynamicEcology()
        ratioDict = self.__CalculateRatio(ecologyInfo)
        ratioTuple = ratioDict.values()
        tickRatio = reduce(operator.mul, ratioTuple, 1)

        cropName = gameComp.GetChinese('item.' + self.crop.GetBlockPrefix() + '.name')

        basicInfo = None
        if not self.__CanGrowDuringPeriod():
            periodName = Period.GetChinese(self.crop.GetGrowPeriod())
            basicInfo = '{0} 休眠中(需要{1})\n'.format(cropName, periodName)
        elif self.CanGrow():
            basicInfo = '{0} 生长中 速度: {1}％\n'.format(cropName, round(tickRatio * 100))
        else:
            basicInfo = '{0} 休眠中(环境不适宜)\n'.format(cropName)

        temperatureText = self.__FormatRatioText(ecologyInfo, 'temperature', ratioDict['temperature'])
        rainfallText = self.__FormatRatioText(ecologyInfo, 'rainfall', ratioDict['rainfall'])
        brightText = self.__FormatRatioText(ecologyInfo, 'bright', ratioDict['bright'])
        weather = ratioDict['weather']
        weatherText = '天气: {0}％\n'.format(weather * 100) if weather != 1 else ''
        fertilityText = '预计收获: {0}％'.format(str(100 + self.__GetGrowFertility()))

        return basicInfo + temperatureText + rainfallText + brightText + weatherText + fertilityText

    def __FormatRatioText(self, ecologyInfo, type, ratio):
        # type: (DynamicEcology, str, float) -> str
        typeDict = {
            'temperature': {
                'cn': '温度',
                'rangeFunc': self.crop.GetGrowTemperature,
                'valueFunc': ecologyInfo.GetAdjustTemperature,
            },
            'rainfall': {
                'cn': '湿度',
                'rangeFunc': self.crop.GetGrowRainfall,
                'valueFunc': ecologyInfo.GetAdjustRainfall,
            },
            'bright': {
                'cn': '光照',
                'rangeFunc': self.crop.GetGrowBrightness,
                'valueFunc': None,
            }
        }
        name = typeDict[type]['cn']
        getRangeFunc = typeDict[type]['rangeFunc']
        valueFunc = typeDict[type]['valueFunc']
        value = valueFunc() if valueFunc else blockInfoComp.GetBlockLightLevel(self.position, self.dimensionId)
        suitTuple = getRangeFunc('suit')
        canTuple = getRangeFunc('can')
        symbol = '℃' if type == 'temperature' else '％' if type == 'rainfall' else ''
        suitText = '适宜: {0}{2}—{1}{2}'.format(suitTuple[0], suitTuple[1], symbol)
        canText = '可行: {0}{2}—{1}{2}'.format(canTuple[0], canTuple[1], symbol)
        return name + ': ' + str(round(ratio * 100)) + '％ (' + ('%.2f'% value + symbol if type != 'bright' else (str(value) + symbol)) + ') ' + suitText + ' ' + canText + '\n'

    def __CanGrowDuringPeriod(self):
        cropPeriod = self.crop.GetGrowPeriod()
        if cropPeriod == Period.NONE:
            return True
        if cropPeriod == Period.SUN and FrameService.HasSun(self.dimensionId):
            return True
        if cropPeriod == Period.MOON and FrameService.HasMoon(self.dimensionId):
            return True
        if cropPeriod == Period.DAY and FrameService.IsDay(self.dimensionId):
            return True
        if cropPeriod == Period.NIGHT and FrameService.IsNight(self.dimensionId):
            return True
        return False

    def __CanGrowOnBlock(self):
        """判断能否种植在土地上"""
        if self.land is None:
            return False
        minFertility = self.crop.GetGrowFertilityMin()
        landFertility = self.land.GetFertility()
        cropTags = self.crop.GetGrowLandType()
        landTags = self.land.GetTags()
        return minFertility <= landFertility and mathUtils.hasCommonElements(landTags, cropTags)
    
    def __CalculateRatio(self, ecologyInfo = None):
        # type: (DynamicEcology | None) -> dict[str, float]
        """计算生长概率，四个分别是"""
        ecologyInfo = ecologyInfo or self.ecology.GetDynamicEcology()
        temperatureRatio = self.__CalculateTemperatureRatio(ecologyInfo)
        rainfallRatio = self.__CalculateRainfallRatio(ecologyInfo)
        brightnessRatio = self.__CalculateBrightnessRatio()
        weatherRatio = 1
        weather = 'rain' if weatherComp.IsRaining() else None
        if weather == 'rain':
            weatherRatio *= self.crop.GetGrowRainMultiply()
        return {
            'temperature': temperatureRatio,
            'rainfall': rainfallRatio,
            'bright': brightnessRatio,
            'weather': weatherRatio
        }

    def __CalculateTemperatureRatio(self, ecologyInfo):
        # type: (DynamicEcology) -> float
        """获取温度适宜比例"""
        temperature = ecologyInfo.GetAdjustTemperature()
        return mathUtils.calculateAbleTickRatio(temperature, self.crop.GetGrowTemperature('suit'), self.crop.GetGrowTemperature('can'))

    def __CalculateRainfallRatio(self, ecologyInfo):
        # type: (DynamicEcology) -> float
        """获取湿度适宜比例"""
        temperature = ecologyInfo.GetAdjustRainfall()
        return mathUtils.calculateAbleTickRatio(temperature, self.crop.GetGrowRainfall('suit'), self.crop.GetGrowRainfall('can'))

    def __CalculateBrightnessRatio(self):
        # type: () -> float
        """获取亮度适宜比例"""
        brightness = blockInfoComp.GetBlockLightLevel(self.position, self.dimensionId)
        return mathUtils.calculateAbleTickRatio(brightness, self.crop.GetGrowBrightness('suit'), self.crop.GetGrowBrightness('can'))

    def __GetGrowFertility(self):
        """获取生长肥沃度"""
        if self.land is None:
            return False
        cropMinFertility = self.crop.GetGrowFertilityMin()
        cropSensitivityFertility = self.crop.GetGrowFertilitySensitivity()
        landFertility = self.land.GetFertility()
        fertility = 1 + (landFertility - cropMinFertility) * cropSensitivityFertility / cropMinFertility
        return mathUtils.GetRandomInteger(fertility)

    def __GetCropEntityData(self):
        cropEntityData = blockEntityDataComp.GetBlockEntityData(self.dimensionId, self.position)
        if not cropEntityData and self.crop.CanGrow():
            logger.error('不存在作物 {} 实体数据'.format(self.cropBlockName))
        return cropEntityData

    def __GetStage(self):
        if self.cropBlockName is None:
            logger.error('空作物无法获取生长状态，这是一个逻辑bug')
            return 0
        return int(self.cropBlockName.split("_")[-1]) if "stage" in self.cropBlockName else 0