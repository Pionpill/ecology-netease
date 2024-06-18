import math
from scripts.common.entity import Effect
from scripts.common.enum.Item import FoodSaturation
from scripts.common.data.item import ITEM_DATA
from scripts.common.error import AddonDataFieldError
from scripts.common.utils import dataUtils

class Food(object):
    """食物"""
    def __init__(self, data):
        # type: (dict) -> None
        self.__data = data

    def GetNutrition(self):
        # type: () -> float | None
        return self.__data.get('nutrition')
    
    def GetEatNutrition(self):
        # type: () -> int | None
        nutrition = self.GetNutrition()
        return math.trunc(math.floor(nutrition)) if nutrition else None
    
    def GetSaturationModifier(self):
        # type: () -> str
        return self.__data.get('saturation', FoodSaturation.POOR)
    
    def GetEffects(self):
        try:
            effects = self.__data.get('effect')
            return [Effect(effect) for effect in effects] if effects else None
        except AddonDataFieldError:
            return None
    
    def CanEat(self):
        # type: () -> bool
        return self.__data.get('can_eat', False)


class Item(object):
    """物品数据"""
    def __init__(self, name):
        self.name = name
        data = ITEM_DATA.get(self.name)
        if data is None:
            raise AddonDataFieldError('{}: 不存在对应的物品数据'.format(name))
        self.__data = data

    def GetQuality(self):
        # type: () -> int
        return self._GetField('quality')
    
    def GetSource(self, sourceType=None):
        # type: (str | None) -> dict[str, tuple[str, ...]] | None
        try:
            key = ('source', sourceType) if sourceType else 'source'
            key = ('source', sourceType) if sourceType else 'source'
        except AddonDataFieldError:
            return None
    
    def GetCategory(self):
        # type: () -> int
        return self._GetField('category')
    
    def GetTags(self):
        # type: () -> tuple[str,]
        return self._GetField('tag')

    def GetHiddenEffects(self):
        # type: () -> tuple[Effect,] | None
        try:
            return self._GetField('hidden_effect')
        except AddonDataFieldError:
            return None
    
    def GetFood(self):
        # type: () -> Food | None
        try:
            food = self._GetField('food')
            return Food(self._GetField('food')) if food else None
        except AddonDataFieldError:
            return None

    def _GetField(self, key, defaultValue = None, data = None):
        """获取字段值，支持递归获取
        
        :param key: 键, str 或可迭代 str 容器
        :param defaultValue: 默认值
        :param data: 数据集，任意类型
        """
        realData = data or self.__data
        return dataUtils.GetField(key, realData, self.name, defaultValue)