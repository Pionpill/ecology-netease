from scripts.common import logger
from scripts.crop.server.entity import Crop

class CropProxy(object):
    def __init__(self, cropName):
        # type: (str) -> None
        object.__init__(self)
        self.crop = Crop.FromSeedKey(cropName)
        self.cropName = cropName
    
    def CanPlantOnBlock(self, plantBlockName):
        # type: (str) -> bool
        """判断某个方块能否种植"""
        return plantBlockName in self.__GetPlantLands()

    def GetTickNum(self, stageId):
        # type: (int) -> int
        """获取生长阶段需要 tick 的次数"""
        tickList = self.__GetField('ticks')
        if stageId + 1 > len(tickList):
            logger.error('{}: tick 状态超范围，注意检查数据'.format(self.cropName))
        return tickList[stageId]

    def GetStageTickCount(self, stageId):
        # type: (int) -> int
        """获取植物的生长状态（ticks）总数"""
        tickList = self.__GetField('ticks')
        if stageId + 1 > len(tickList):
            logger.error('{}: tick 状态超范围，注意检查数据'.format(self.cropName))
        return tickList[stageId]
    
    def IsLastStage(self, blockName):
        # type: (str) -> bool
        """判断是否为作物最终生长状态"""
        stageId = self.__GetStageId(blockName)
        stageCount = self.GetStageTickCount(stageId)
        return stageCount == stageId + 1
    
    def GetHarvestCount(self):
        # type: () -> int
        """获取作物收获次数"""
        return self.__GetField('harvest_count')
    
    def GetTemperatureRange(self, type):
        # type: (str) -> (int, int)
        """获取温度生长范围，type: suit/can"""
        if type == 'suit':
            return self.__GetField('temperature_suit')
        elif type == 'can':
            return self.__GetField('temperature_can')
        else:
            logger.error('请选择温度范围类型，suit/can')

    def GetRainfallRange(self, type):
        # type: (str) -> (int, int)
        """获取降水生长范围，type: suit/can"""
        if type == 'suit':
            return self.__GetField('rainfall_suit')
        elif type == 'can':
            return self.__GetField('rainfall_can')
        else:
            logger.error('请选择降水范围类型，suit/can')

    def GetBrightnessRange(self, type):
        # type: (str) -> (int, int)
        """获取光照生长范围，type: suit/can"""
        if type == 'suit':
            return self.__GetField('brightness_suit')
        elif type == 'can':
            return self.__GetField('brightness_can')
        else:
            logger.error('请选择光照范围类型，suit/can')

    def GetRainMultiply(self):
        # type: () -> float
        """获取下雨时作物生长倍率"""
        return self.__GetField('rain_multiply', 1)
    
    def GetMultiGrowCount(self):
        # type: () -> int
        """获取作物多次生长数"""
        return self.__GetField('multi_grow_count', 1)
    
    def GetMultiGrowStage(self):
        # type: () -> int
        """获取作物多次生长被收获后回归的状态"""
        return self.__GetField('multi_grow_stage', 1)
    
    def GetHarvestStages(self):
        # type: () -> list[int]
        """获取作物可收获的状态，默认最终状态可收获"""
        lastStage = self.GetStageTickCount()
        return self.__GetField('middle_harvest_stages', [lastStage])

    def __GetField(self, fieldName, default = None):
        # type: (str, any) -> None
        """获取作物的数据字段，如果不存在则报错"""
        fieldData = self.crop.plantInfo.get(fieldName)
        if fieldData is None:
            fieldData = self.crop.growInfo.get(fieldName)
        if fieldData is None and default is None:
            logger.error('{}: 不存在{}数据'.format(self.cropName, fieldName))
        else:
            return fieldData or default
    
    def __GetStageId(self, blockName):
        # type: (str) -> int
        return int(blockName.split("_")[-1])
    
    def __GetPlantLands(self):
        # type: () -> [str]
        """获取可以种植的方块列表"""
        return self.__GetField('land')