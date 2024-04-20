from scripts.common.enum import Period
from scripts.common.data.crop import CROP_DATA
from scripts.common.error import AddonDataError
from scripts.common.utils import dataUtils
from scripts.common import logger

class GrowStageInfo(object):
    """某状态的作物信息"""
    def __init__(self, tick, height):
        # type: (int | None, tuple[int, int]) -> None
        self.tick = tick
        self.height = height

    @staticmethod
    def FromData(data, seedName, index = None):
        # type: (dict, str, int | None) -> GrowStageInfo
        tick = data.get('tick')
        height = data.get('height')
        if height is None:
            indexMsg = index or '最终'
            raise AddonDataError('{}: 不存在状态 {} 对应的 height 数据'.format(seedName, indexMsg))
        return GrowStageInfo(tick, height)

class LootInfo(object):
    """凋落物信息"""
    def __init__(self, itemName, chance, count):
        # type: (str, int, int) -> None
        self.itemName = itemName 
        self.chance = chance
        self.count = count
    
    @staticmethod
    def FromData(data, seedName, index = None):
        # type: (dict, str, int | None) -> LootInfo
        indexMsg = index or '最终'
        itemName = data.get('name')
        if itemName is None:
            raise AddonDataError('{}: 不存在 {} 状态的凋落物品名称'.format(seedName, indexMsg))
        chance = data.get('chance', 100)
        count = data.get('count')
        if count is None:
            raise AddonDataError('{}: 不存在 {} 状态的凋落物品数量'.format(seedName, indexMsg))
        return LootInfo(itemName, chance, count)

class Crop(object):
    def __init__(self, seedKey):
        # type: (str) -> None 
        self.seedName = seedKey
        data = CROP_DATA.get(seedKey)
        if data is None:
            raise AddonDataError('{}: 不存在对应的作物数据'.format(seedKey))
        self.__data = data
        self.growStageTuple = None # type: tuple[GrowStageInfo, ...] | None
        self.lootsMap = {} # type: dict[int, tuple[LootInfo, ...]]
        
    def IsBeta(self):
        # type: () -> bool
        """判断是否beta上线"""
        return self._GetField("beta", False)
    
    def GetSeedName(self):
        # type: () -> str
        """获取对应的种子名称"""
        return self._GetField("seed")
    
    def GetBlockPrefix(self):
        # type: () -> str
        """获取作物方块的前缀"""
        def GetDefaultPrefix():
            seedName = self.GetSeedName()
            defaultValue = seedName
            for suffix in ['_seeds', '_seed']:
                defaultValue = defaultValue.replace(suffix, '')
            return defaultValue
        return self._GetField("blockPrefix", GetDefaultPrefix)
    
    def GetGrowStageTuple(self):
        # type: () -> tuple[GrowStageInfo, ...]
        """获取生长状态元组"""
        if self.growStageTuple is None:
            stages = self._GetField(("grow", "stage")) # type: tuple[dict]
            result = [] # list[GrowStageInfo, ...]
            for index, stage in enumerate(stages):
                result.append(GrowStageInfo.FromData(stage, self.seedName, index))
            self.growStageTuple = tuple(result)
        return self.growStageTuple
    
    def GetGrowStageLength(self):
        # type: () -> int
        """获取总的状态数"""
        return len(self.GetGrowStageTuple())
    
    def IsLastStage(self, stage):
        # type: (int) -> bool
        """判断是否为最终生长状态"""
        stageLength = self.GetGrowStageLength()
        return stage == (stageLength - 1)
    
    def GetGrowStageInfo(self, stage):
        # type: (int) -> GrowStageInfo
        """获取总的状态数"""
        growStageTuple = self.GetGrowStageTuple()
        if stage >= len(growStageTuple):
            raise AddonDataError('{} 没有状态 {}'.format(self.seedName, stage))
        return growStageTuple[stage]
    
    def GetGrowHarvestCount(self):
        # type: () -> int
        """获取可收获次数"""
        return self._GetField(("grow", "harvest", "count"), 1)

    def GetGrowHarvestStage(self):
        # type: () -> tuple[int, ...]
        """获取可收获的状态，返回一个元组"""
        stage = self._GetField(("grow", "harvest", "stage"))
        return stage if isinstance(stage, tuple) else (stage,)

    def GetGrowHarvestReturn(self):
        # type: () -> int
        """获取收获后返回的状态数，返回 -1 表示只能收获一次"""
        return self._GetField(("grow", "harvest", "return"), -1)
    
    def GetGrowTemperature(self, type = 'can'):
        # type: (str) -> tuple[int, int]
        """获取生长温度
        
        :param type: 范围类型 can, suit
        """
        return self._GetField(("grow", "temperature", type))

    def GetGrowRainfall(self, type = 'can'):
        # type: (str) -> tuple[int, int]
        """获取生长温度
        
        :param type: 范围类型 can, suit
        """
        return self._GetField(("grow", "rainfall", type))

    def GetGrowBrightness(self, type = 'can'):
        # type: (str) -> tuple[int, int]
        """获取生长温度
        
        :param type: 范围类型 can, suit
        """
        return self._GetField(("grow", "brightness", type))
    
    def GetGrowRainMultiply(self):
        # type: () -> float
        """获取生长温度"""
        return self._GetField(("grow", "rain_multiply"))

    def GetGrowPeriod(self):
        # type: () -> Period
        return self._GetField(("grow", "period"), Period.DAY)

    def GetGrowFertilityMin(self):
        # type: () -> int
        """获取最低土地肥沃度要求"""
        return self._GetField(("grow", "fertility", "min"))
    
    def GetGrowFertilitySensitivity(self):
        # type: () -> int
        """获取土地肥沃灵敏度"""
        return self._GetField(("grow", "fertility", "sensitivity"))
    
    def GetGrowLandType(self):
        # type: () -> tuple[str, ...]
        """获取可种植的土地类型"""
        return self._GetField(("grow", "fertility", "type"))
    
    def GetLoots(self, stage = None):
        # type: (int | None) -> tuple[LootInfo, ...] | None
        """获取某一状态的掉落物表"""
        lootField = self._GetField("loot") # type: tuple[dict] | None
        lastStage = self.GetGrowStageLength() - 1
        if isinstance(lootField, tuple) and (stage is None or self.IsLastStage(stage)):
            if self.lootsMap.get(lastStage) is None:
                self.lootsMap[lastStage] = tuple(LootInfo.FromData(lootInfo, self.seedName, stage) for lootInfo in lootField)
            return self.lootsMap[lastStage]
        if isinstance(lootField, dict):
            realStage = stage or lastStage
            loots = lootField.get(realStage)
            if loots is None:
                raise AddonDataError('{} 没有状态 {} 的掉落物'.format(self.seedName, stage))
            if self.lootsMap.get(realStage) is None:
                self.lootsMap[realStage] = tuple(LootInfo.FromData(lootInfo, self.seedName, stage) for lootInfo in loots)
            return self.lootsMap[realStage]
        raise AddonDataError('{} 凋落物数据结构异常'.format(self.seedName))
    
    def _GetField(self, key, defaultValue = None, data = None):
        """获取字段值，支持递归获取
        
        :param key: 键, str 或可迭代 str 容器
        :param defaultValue: 默认值
        :param data: 数据集，任意类型
        """
        realData = data or self.__data
        return dataUtils.GetField(key, realData, self.seedName, defaultValue)