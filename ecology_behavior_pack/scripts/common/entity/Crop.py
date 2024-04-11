from scripts.common.data.crop import CROP_DATA
from scripts.common.error import AddonDataError
from scripts.common.utils import dataUtils
from scripts.common import logger

class GrowStageInfo(object):
    """某状态的作物信息"""
    def __init__(self, tick, height):
        # type: (int, tuple[int, int]) -> None
        self.tick = tick
        self.height = height

class LootInfo(object):
    """凋落物信息"""
    def __init__(self, itemName, chance, count):
        # type: (str, int, float) -> None
        self.itemName = itemName 
        self.chance = chance
        self.count = count

class Crop(object):
    def __init__(self, seedKey):
        # type: (str) -> None 
        data = CROP_DATA.get(seedKey)
        self.seedName = seedKey
        if data is None:
            raise AddonDataError('{}: 不存在对应的作物数据'.format(seedKey))
        self.__data = data
        
    def IsBeta(self):
        # type: () -> bool
        """判断是否beta上线"""
        return self.__GetField("beta", False)
    
    def GetSeedName(self):
        # type: () -> str
        """获取对应的种子名称"""
        return self.__GetField("seed")
    
    def GetGrowStageTuple(self):
        # type: () -> tuple[GrowStageInfo, ...]
        """获取生长状态元组"""
        return self.__GetField(("grow", "stage"))
    
    def GetGrowStageLength(self):
        # type: () -> int
        """获取总的状态数"""
        return len(self.GetGrowStageTuple())
    
    def IsLastStage(self, stage):
        # type: (int) -> bool
        """判断是否为最终生长状态"""
        stageLength = self.GetGrowStageLength()
        return stage == (stageLength - 1)
    
    def CanGrow(self):
        # type: () -> bool
        """判断能否生长"""
        return self.GetGrowStageLength() > 1
    
    def GetGrowStageInfo(self, stage):
        # type: (int) -> GrowStageInfo
        """获取总的状态数"""
        growStageTuple = self.GetGrowStageTuple()
        if stage >= len(growStageTuple):
            logger.error('{} 没有状态 {}'.format(self.seedName, stage))
            raise 
        return growStageTuple[stage]
    
    def GetGrowHarvestCount(self):
        # type: () -> int
        """获取可收获次数"""
        return self.__GetField(("grow", "harvest", "count"), 1)

    def GetGrowHarvestStage(self):
        # type: () -> tuple[int]
        """获取可收获的状态，返回一个元组"""
        stage = self.__GetField(("grow", "harvest", "stage"))
        return stage if isinstance(stage, tuple) else (stage)

    def GetGrowHarvestReturn(self):
        # type: () -> int
        """获取收获后返回的状态数"""
        return self.__GetField(("grow", "harvest", "return"))
    
    def GetGrowTemperature(self, type = 'can'):
        # type: (str) -> tuple[int, int]
        """获取生长温度
        
        :param type: 范围类型 can, suit
        """
        return self.__GetField(("grow", "temperature", type))

    def GetGrowRainfall(self, type = 'can'):
        # type: (str) -> tuple[int, int]
        """获取生长温度
        
        :param type: 范围类型 can, suit
        """
        return self.__GetField(("grow", "rainfall", type))

    def GetGrowBrightness(self, type = 'can'):
        # type: (str) -> tuple[int, int]
        """获取生长温度
        
        :param type: 范围类型 can, suit
        """
        return self.__GetField(("grow", "brightness", type))
    
    def GetGrowRainMultiply(self):
        # type: () -> float
        """获取生长温度"""
        return self.__GetField(("grow", "rain_multiply"))

    def GetGrowFertilityMin(self):
        """获取最低土地肥沃度要求"""
        return self.__GetField(("grow", "fertility", "min"))
    
    def GetGrowFertilitySensitivity(self):
        # type: () -> int
        """获取土地肥沃灵敏度"""
        return self.__GetField(("grow", "fertility", "sensitivity"))
    
    def GetGrowLandType(self):
        # type: () -> tuple[str, ...]
        """获取可种植的土地类型"""
        return self.__GetField(("grow", "fertility", "type"))
    
    def GetLoots(self, stage = None):
        # type: (int | None) -> tuple[LootInfo] | None
        """获取某一状态的掉落物表"""
        lootField = self.__GetField("loot")
        if isinstance(lootField, tuple) and (stage is None or self.IsLastStage(stage)):
            return lootField
        if isinstance(lootField, dict):
            return lootField.get(stage)
        return None
    
    def __GetField(self, key, defaultValue = None, data = None):
        """获取字段值，支持递归获取
        
        :param key: 键, str 或可迭代 str 容器
        :param defaultValue: 默认值
        :param data: 数据集，任意类型
        """
        realData = data or self.__data
        return dataUtils.GetField(key, realData, self.seedName, defaultValue)