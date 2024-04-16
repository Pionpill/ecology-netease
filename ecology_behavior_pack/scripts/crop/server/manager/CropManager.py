import random
import mod.server.extraServerApi as serverApi

from scripts.common.enum import Period
from scripts.common import logger
from scripts.common.entity import Crop
from scripts.common.entity import GetCrop, GetLand
from scripts.common.utils import itemUtils
from scripts.common.utils import mathUtils
from scripts.common.utils import positionUtils
from scripts.crop.server.utils import cropUtils
from scripts.ecology.server.entity import DynamicEcology
from scripts.ecology.server.facade import EcologyFacade
from scripts.ecology.server.service import FrameService

levelId = serverApi.GetLevelId()
engineCompFactory = serverApi.GetEngineCompFactory()
blockEntityDataComp = engineCompFactory.CreateBlockEntityData(levelId)
blockInfoComp = engineCompFactory.CreateBlockInfo(levelId)
itemComp = engineCompFactory.CreateItem(levelId)
weatherComp = engineCompFactory.CreateWeather(levelId)


class CropManager(object):
    """作物管理类"""
    def __init__(self, position, dimensionId, crop = None, ecology = None):
        # type: (tuple[int, int, int], int, Crop | None, DynamicEcology | None) -> None
        object.__init__(self)
        self.position = position
        self.dimensionId = dimensionId
        self.RenewCropInfo()
        self.RenewLandInfo()
        if not self.cropBlockName:
            return
        
        if crop:
            self.crop = crop
        else:
            cropKey = cropUtils.GetSeedKey(self.cropBlockName)
            crop = GetCrop(cropKey)
            if crop is None:
                logger.error('无法通过 {} 获取作物实例'.format(cropKey))
                return
            self.crop = crop
        self.ecology = ecology or EcologyFacade.GetEcologyInfo(position, dimensionId)

    def CanGrow(self):
        """判断能否生长"""
        if self.crop.IsLastStage(self.cropStage):
            return False
        if not self.__CanPlantDuringPeriod():
            return False
        if not self.__CanPlantOnBlock():
            return False
        temperature = self.ecology.GetAdjustTemperature()
        if not mathUtils.between(temperature, self.crop.GetGrowTemperature('can')):
            return False
        rainfall = self.ecology.GetAdjustRainfall()
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

        growTicks = self.__CalculateGrowTick()
        blockTick = cropEntityData['tick'] or 0
        blockTickCount = cropEntityData['tickCount'] or 0
        blockFertility = cropEntityData['fertility'] or 0
        nextTick = growTicks + blockTick
        if nextTick < tickCount:
            cropEntityData['tick'] = nextTick
            cropEntityData['tickCount'] = blockTickCount + 1
            cropEntityData['fertility'] = blockFertility + self.__GetGrowFertility()
            return
        cropBlockNameList = self.cropBlockName.split("_")
        cropBlockNameList[-1] = str(int(cropBlockNameList[-1]) + 1)
        nextBlock = {"name": "_".join(cropBlockNameList), "aux": 0}
        blockInfoComp.SetBlockNew(self.position, nextBlock, dimensionId=self.dimensionId)
        cropEntityData = self.__GetCropEntityData()
        if cropEntityData is None:
            logger.error('生长后 {} 无法获取实体数据'.format(nextBlock.get('name', self.cropBlockName)))
            return
        cropEntityData['tick'] = nextTick - tickCount
        cropEntityData['tickCount'] = blockTickCount + 1
        cropEntityData['fertility'] = blockFertility + self.__GetGrowFertility()
        self.RenewCropInfo()

    def Harvest(self, remove = False, loot = True):
        # type: (bool, bool) -> bool
        """
        收获作物
        
        :param remove: 是否删除作物，否则尝试多次收获 TODO 多次收获功能未实装
        :param loot: 是否生成凋落物
        """
        if self.cropBlockName is None:
            return False
        harvestStages = self.crop.GetGrowHarvestStage()
        stage = self.__GetStage()
        if stage not in harvestStages:
            return False

        if loot:
            self.SpawnLoots()

        if remove:
            result = blockInfoComp.SetBlockNew(self.position, {'name': 'minecraft:air', 'aux': 0}, dimensionId = self.dimensionId)
            if not result:
                logger.error('发生了不可能出现的错误，收获作物失败')
                return False
        else:
            returnStage = self.crop.GetGrowHarvestReturn()
            if returnStage is None:
                return False
            cropBlockNameList = self.cropBlockName.split("_")
            cropBlockNameList[-1] = str(returnStage)

            newBlockDict = {"name": "_".join(cropBlockNameList), "aux": 0}
            cropEntityData = self.__GetCropEntityData()
            if cropEntityData is None:
                return False
            blockTickCount = cropEntityData['tickCount'] or 0
            blockFertility = cropEntityData['fertility'] or 0
            result = blockInfoComp.SetBlockNew(self.position, newBlockDict, dimensionId = self.dimensionId)
            cropEntityData = self.__GetCropEntityData()
            if cropEntityData is None:
                return False
            self.RenewCropInfo()
            cropEntityData['tickCount'] = blockTickCount
            cropEntityData['fertility'] = blockFertility
            if not result:
                logger.error('发生了不可能出现的错误，收获作物失败')
                return False
        return True

    def SpawnLoots(self):
        loots = self.crop.GetLoots()
        if loots is None:
            return
        for loot in loots:
            if random.random() * 100 > loot.chance:
                return
            cropEntityData = self.__GetCropEntityData()
            if cropEntityData is None:
                return
            fertility = cropEntityData['fertility']
            tickCount = cropEntityData['tickCount']
            avgFertility = 1 + (fertility / tickCount) / 100 if fertility and tickCount else 1
            count = mathUtils.GetRandomInteger(loot.count * avgFertility)
            itemDict = itemUtils.GetItemDict(loot.itemName, 0, count)
            itemComp.SpawnItemToLevel(itemDict,  self.dimensionId, self.position)
        
    def GetStageTickCount(self):
        """获取作物块进入下一阶段所需要 tick 总数"""
        stageId = self.__GetStage()
        return self.crop.GetGrowStageInfo(stageId).tick

    def CanHarvest(self):
        """判断是否可以收获"""
        stage = self.__GetStage()
        harvestStages = self.crop.GetGrowHarvestStage()
        return stage in harvestStages
    
    def GetHarvestStage(self):
        """获取收获后返回的状态"""
        return self.crop.GetGrowHarvestReturn()
        
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
        self.land = GetLand(self.landName) if self.landName else None

    def __CanPlantDuringPeriod(self):
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

    def __CanPlantOnBlock(self):
        """判断能否种植在土地上"""
        if self.land is None:
            return False
        minFertility = self.crop.GetGrowFertilityMin()
        landFertility = self.land.GetFertility()
        cropTags = self.crop.GetGrowLandType()
        landTags = self.land.GetTags()
        return minFertility <= landFertility and mathUtils.hasCommonElements(landTags, cropTags)

    def __CalculateGrowTick(self):
        """计算生长可获得 tick 数"""
        temperature = self.ecology.GetAdjustTemperature()
        rainfall = self.ecology.GetAdjustRainfall()
        brightness = blockInfoComp.GetBlockLightLevel(self.position, self.dimensionId)
        tickCount = 1

        tickCount *= mathUtils.calculateAbleTickRatio(temperature, self.crop.GetGrowTemperature('suit'), self.crop.GetGrowTemperature('can'))
        tickCount *= mathUtils.calculateAbleTickRatio(rainfall, self.crop.GetGrowRainfall('suit'), self.crop.GetGrowRainfall('can'))
        tickCount *= mathUtils.calculateAbleTickRatio(brightness, self.crop.GetGrowBrightness('suit'), self.crop.GetGrowBrightness('can'))
        weather = 'rain' if weatherComp.IsRaining() else None
        if weather == 'rain':
            tickCount *= self.crop.GetGrowRainMultiply()

        return mathUtils.GetRandomInteger(tickCount)

    def __GetGrowFertility(self):
        if self.land is None:
            return False
        cropMinFertility = self.crop.GetGrowFertilityMin()
        cropSensitivityFertility = self.crop.GetGrowFertilitySensitivity()
        landFertility = self.land.GetFertility()
        fertility = 1 + (landFertility - cropMinFertility) * cropSensitivityFertility / cropMinFertility
        return mathUtils.GetRandomInteger(fertility)

    def __GetCropEntityData(self):
        cropEntityData = blockEntityDataComp.GetBlockEntityData(self.dimensionId, self.position)
        if not cropEntityData:
            logger.error('不存在作物 {} 实体数据'.format(self.cropBlockName))
        return cropEntityData

    def __GetStage(self):
        if self.cropBlockName is None:
            logger.error('空作物无法获取生长状态，这是一个逻辑bug')
            return 0
        return int(self.cropBlockName.split("_")[-1])