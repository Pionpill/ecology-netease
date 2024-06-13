import math
from scripts.common.enum.Item import FoodSaturation
from scripts.common.data.item import ITEM_DATA
from scripts.common.error import AddonDataError
from scripts.common.utils import dataUtils

class Food(object):
    """食物"""
    def __init__(self, data):
        # type: (dict) -> None
        self.__data = data

    def GetNutrition(self):
        # type: () -> float
        return self.__data.get('nutrition', 0)
    
    def GetEatNutrition(self):
        # type: () -> int
        return math.floor(self.GetNutrition())
    
    def GetSaturationModifier(self):
        # type: () -> str
        return self.__data.get('saturation_modifier', FoodSaturation.POOR)
    
    def CanEat(self):
        # type: () -> bool
        return self.__data.get('can_eat', False)


class Item(object):
    """物品数据"""
    def __init__(self, name):
        self.name = name
        data = ITEM_DATA.get(self.name)
        if data is None:
            raise AddonDataError('{}: 不存在对应的物品数据'.format(name))
        self.__data = data

    def GetQuality(self):
        # type: () -> int
        return self._GetField('quality')
    
    def GetSource(self, sourceType):
        # type: (str | None) -> tuple[str, ...]
        key = ('source', sourceType) if sourceType else 'source'
        return self._GetField(key)
    
    def GetCategory(self):
        # type: () -> int
        return self._GetField('category')
    
    def GetTags(self):
        # type: () -> int
        return self._GetField('tag')

    def GetHiddenEffectTypes(self):
        # type: () -> int | None
        return self._GetField('hidden_effect')
    
    def _GetField(self, key, defaultValue = None, data = None):
        """获取字段值，支持递归获取
        
        :param key: 键, str 或可迭代 str 容器
        :param defaultValue: 默认值
        :param data: 数据集，任意类型
        """
        realData = data or self.__data
        return dataUtils.GetField(key, realData, self.name, defaultValue)