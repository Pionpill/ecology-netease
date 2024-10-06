"""
entity 层的两个作用
1. 获取原始数据
2. 给 python 插件提供类型
entity 的数据都是只读的，且相同的数据使用单例模式返回实例
"""
from scripts.common.entity.Crop import Crop
from scripts.common.entity.Item import Item
from scripts.common.entity.Land import Land
from scripts.common.entity.Recipe import Recipe

__all__ = ['Crop', 'Land', 'Recipe', 'Item']
