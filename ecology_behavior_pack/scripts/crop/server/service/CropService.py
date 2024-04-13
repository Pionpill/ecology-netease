import math
import random
from scripts.common import logger
from scripts.common.error import AddonDevelopError
from scripts.common.entity import Crop, GetCrop, GetLand
from scripts.crop.server.utils import cropUtils
from scripts.common.params import EcologyInfo
from scripts.common.utils import mathUtils

class CropService(object):
    @staticmethod
    def CanPlant(itemName, plantBlockName, blockAux, temperature, rainfall):
        # type: (str, str, int | None, int, float) -> str | bool
        """判断是否可以种植，返回 True 表示可种植，字符串(biome, block)表示不可种植原因"""
        crop = CropService.__GetCrop(itemName)
        if not CropService.CanPlantOnBlock(itemName, plantBlockName, blockAux):
            return 'block'
        elif not mathUtils.between(temperature, crop.GetGrowTemperature('can')):
            return 'temperature'
        elif not mathUtils.between(rainfall, crop.GetGrowRainfall('can')):
            return 'rainfall'
        return True

    @staticmethod
    def CanGrow(blockOrItemName, ecology, brightness, plantBlockName, blockAux):
        # type: (str, EcologyInfo, int, str, int | None) -> bool
        """判断作物能否生长"""
        crop = CropService.__GetCrop(blockOrItemName)
        temperature = ecology.temperature
        rainfall = ecology.rainfall

        # 生长过程中，土地可能变化
        if not CropService.CanPlantOnBlock(blockOrItemName, plantBlockName, blockAux):
            return False
        if not mathUtils.between(temperature, crop.GetGrowTemperature('can')):
            return False
        if not mathUtils.between(rainfall, crop.GetGrowRainfall('can')):
            return False
        if not mathUtils.between(brightness, crop.GetGrowBrightness('can')):
            return False
        return True

    @staticmethod
    def CanPlantOnBlock(blockOrItemName, plantBlockName, blockAux = None):
        # type: (str, str, int | None) -> bool
        """判断某个作物(块)能否种植在方块上"""
        crop = CropService.__GetCrop(blockOrItemName)
        land = GetLand(plantBlockName)
        if land is None:
            return False
        fertility = land.GetFertility(blockAux)
        tags = land.GetTags()
        return crop.GetGrowFertilityMin() <= fertility and mathUtils.hasCommonElements(tags, crop.GetGrowLandType())
    
    @staticmethod
    def GetStageTickCount(blockName):
        # type: (str) -> int | None
        """获取作物块进入下一阶段所需要 tick 总数"""
        crop = CropService.__GetCrop(blockName)
        stageId = CropService.__GetStageId(blockName)
        return crop.GetGrowStageInfo(stageId).tick

    @staticmethod
    def IsLastStage(blockName):
        # type: (str) -> bool
        """判断是否为最终生长阶段"""
        crop = CropService.__GetCrop(blockName)
        stageId = CropService.__GetStageId(blockName)
        return crop.IsLastStage(stageId)

    @staticmethod
    def CalculateGrowTick(blockName, ecology, brightness, weather = None):
        # type: (str, EcologyInfo, int, str | None) -> int
        """
        计算 tick 时生长的速度
        
        :param weather: 天气，rain, snow
        """
        crop = CropService.__GetCrop(blockName)
        temperature = ecology.temperature
        rainfall = ecology.rainfall
        
        tickCount = 1
        tickCount *= CropService.__CalculateAbleTickRatio(temperature, crop.GetGrowTemperature('suit'), crop.GetGrowTemperature('can'))
        tickCount *= CropService.__CalculateAbleTickRatio(rainfall, crop.GetGrowRainfall('suit'), crop.GetGrowRainfall('can'))
        tickCount *= CropService.__CalculateAbleTickRatio(brightness, crop.GetGrowBrightness('suit'), crop.GetGrowBrightness('can'))
        if weather == 'rain':
            tickCount *= crop.GetGrowRainMultiply()

        floor = math.floor(tickCount)
        ceil = math.ceil(tickCount)
        return ceil if random.random() < (tickCount - floor) else floor

    @staticmethod
    def CanHarvest(blockName):
        # type: (str) -> bool
        """判断是否可以收获"""
        crop = CropService.__GetCrop(blockName)
        stage = CropService.__GetStageId(blockName)
        harvestStages = crop.GetGrowHarvestStage()
        return stage in harvestStages
    
    @staticmethod
    def GetHarvestStage(blockOrItemName):
        # type: (str) -> int
        """获取收获后返回的状态"""
        crop = CropService.__GetCrop(blockOrItemName)
        return crop.GetGrowHarvestReturn()

    @staticmethod
    def __GetStageId(blockName):
        # type: (str) -> int
        """获取作物快的状态 id"""
        return int(blockName.split("_")[-1])

    @staticmethod
    def __GetCrop(blockOrItemName):
        # type: (str) -> Crop
        """获取 Crop 对象"""
        cropKey = cropUtils.GetSeedKey(blockOrItemName)
        crop = GetCrop(cropKey)
        if crop is None:
            raise AddonDevelopError('自定义作物 {} 未找到对应的数据'.format(blockOrItemName))
        return crop

    @staticmethod
    def __CalculateAbleTickRatio(value, suitRange, canRange):
        # type: (int | float, tuple[float, float], tuple[float, float]) -> float
        """获取温度，降水，光照的适宜度"""
        if mathUtils.between(value, suitRange):
            return 1.0
        if value < suitRange[0]:
            return (float(value) - canRange[0]) / (suitRange[0] - canRange[0])
        else:
            return (suitRange[1] - float(value)) / (canRange[1] - suitRange[1])
