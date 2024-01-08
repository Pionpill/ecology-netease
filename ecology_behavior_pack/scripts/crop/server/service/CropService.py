import math
import random
from scripts.crop.server.utils import cropUtils
from scripts.common.params import EcologyInfo
from scripts.common.utils import mathUtils
from scripts.crop.server.proxy import CropProxy

class CropService(object):
    # 作物信息表，防止每次都需要 new cropProxy 对象
    cropProxyMap = {}  

    def __init__(self):
        object.__init__(self)

    @staticmethod
    def CanPlant(itemName, plantBlockName, temperature, rainfall):
        # type: (str, str, int, float) -> str | bool
        """判断是否可以种植，返回 True 表示可种植，字符串(biome, block)表示不可种植原因"""
        cropProxy = CropService.__GetCropProxy(itemName)
        if not cropProxy.CanPlantOnBlock(plantBlockName):
            return 'block'
        elif not mathUtils.between(temperature, cropProxy.GetTemperatureRange('can')):
            return 'temperature'
        elif not mathUtils.between(rainfall, cropProxy.GetTemperatureRange('can')):
            return 'rainfall'
        return True
    
    @staticmethod
    def CanGrow(blockOrItemName, ecology, brightness, plantBlockName):
        # type: (str, EcologyInfo, int, str) -> bool
        """判断作物能否生长"""
        cropProxy = CropService.__GetCropProxy(blockOrItemName)
        temperature = ecology.temperature
        rainfall = ecology.rainfall

        if not cropProxy.CanPlantOnBlock(plantBlockName):
            return False
        if not mathUtils.between(temperature, cropProxy.GetTemperatureRange('can')):
            return False
        if not mathUtils.between(rainfall, cropProxy.GetRainfallRange('can')):
            return False
        if not mathUtils.between(brightness, cropProxy.GetBrightnessRange('can')):
            return False
        return True

    @staticmethod
    def CanPlantOnBlock(blockOrItemName, plantBlockName):
        # type: (str, str) -> bool
        """判断某个作物(块)能否种植在方块上"""
        cropProxy = CropService.__GetCropProxy(blockOrItemName)
        return cropProxy.CanPlantOnBlock(plantBlockName)
    
    @staticmethod
    def GetStageTickCount(blockOrItemName):
        # type: (str) -> int
        """获取作物块进入下一阶段所需要 tick 总数"""
        cropProxy = CropService.__GetCropProxy(blockOrItemName)
        stageId = int(blockOrItemName.split('_')[-1])
        return cropProxy.GetStageTickCount(stageId)

    @staticmethod
    def IsLastStage(blockName):
        # type: (str) -> bool
        """判断是否为最终生长阶段"""
        cropProxy = CropService.__GetCropProxy(blockName)
        return cropProxy.IsLastStage(blockName);

    @staticmethod
    def GetGrowTick(blockName, ecology, brightness, weather=None):
        # type: (str, EcologyInfo, int, str) -> int
        """获取 tick 时生长的速度"""
        cropProxy = CropService.__GetCropProxy(blockName)
        temperature = ecology.temperature
        rainfall = ecology.rainfall
        
        tickCount = 1
        tickCount *= CropService.__GetAbleTickRatio(temperature, cropProxy.GetTemperatureRange('suit'), cropProxy.GetTemperatureRange('can'))
        tickCount *= CropService.__GetAbleTickRatio(rainfall, cropProxy.GetRainfallRange('suit'), cropProxy.GetRainfallRange('can'))
        tickCount *= CropService.__GetAbleTickRatio(brightness, cropProxy.GetBrightnessRange('suit'), cropProxy.GetBrightnessRange('can'))
        if weather == 'rain':
            tickCount *= cropProxy.GetRainMultiply()

        floor = math.floor(tickCount)
        ceil = math.ceil(tickCount)
        return ceil if random.random() < (tickCount - floor) else floor

    @staticmethod
    def CanHarvest(blockName):
        # (str) -> bool
        """判断是否可以收获"""
        cropProxy = CropService.__GetCropProxy(blockName)
        stage = CropService.__GetStageId(blockName)
        harvestStages = cropProxy.GetHarvestStages()
        return stage in harvestStages
    
    @staticmethod
    def GetHarvestStage(blockOrItemName, harvestCount = None):
        # (str) -> int | None
        """获取收获后的状态，None 表示不可再次生长"""
        cropProxy = CropService.__GetCropProxy(blockOrItemName)
        if (harvestCount is not None) and (harvestCount <= cropProxy.GetMultiGrowCount()):
            return cropProxy.GetMultiGrowStage()
        return None

    @staticmethod
    def __GetStageId(blockName):
        # type: (str) -> int
        """获取作物快的状态 id"""
        return int(blockName.split("_")[-1])

    @staticmethod
    def __GetCropProxy(blockOrItemName):
        # type: (str) -> CropProxy
        """获取 CropProxy 对象"""
        cropKey = cropUtils.GetSeedKey(blockOrItemName)
        cropProxy = CropService.cropProxyMap.get(blockOrItemName)
        if cropProxy:
            return cropProxy
        else:
            CropService.cropProxyMap[cropKey] = CropProxy(cropKey)
            return CropService.cropProxyMap[cropKey]

    @staticmethod
    def __GetAbleTickRatio(value, suitRange, canRange):
        # type: (float, tuple, tuple) -> float
        """获取温度，降水，光照的适宜度"""
        if mathUtils.between(value, suitRange):
            return 1
        if value < suitRange[0]:
            return (value - canRange[0]) / (suitRange[0] - canRange[0])
        if value > suitRange[1]:
            return (suitRange[1] - value) / (canRange[1] - suitRange[1])
