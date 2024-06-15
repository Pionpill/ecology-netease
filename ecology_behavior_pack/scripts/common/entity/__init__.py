"""
entity 层的两个作用
1. 获取原始数据
2. 给 python 插件提供类型
entity 的数据都是只读的，且相同的数据使用单例模式返回实例
"""

# 作物表，防止每次都需要 new Crop
from scripts.common.entity.Biome import Biome
from scripts.common.entity.Crop import Crop
from scripts.common.entity.Effect import Effect
from scripts.common.entity.Item import Item
from scripts.common.entity.Land import Land
from scripts.common.entity.Recipe import Recipe
from scripts.common.error import AddonDataError
from scripts.common import logger

biomeMap = {} # type: dict[str, Biome]

def GetBiome(biomeName):
    # type: (str) -> Biome | None
    """获取生态实例，单例模式"""
    biome = biomeMap.get(biomeName)
    if biome is not None:
        return biome
    try:
        biome = Biome.FromBiomeName(biomeName)
    except AddonDataError as e:
        logger.warn(e.message)
        return None
    biomeMap[biomeName] = biome
    return biome

cropMap = {} # type: dict[str, Crop]

def GetCrop(seedKey):
    # type: (str) -> Crop | None
    """获取作物实例，单例模式"""
    crop = cropMap.get(seedKey)
    if crop is not None:
        return crop
    try:
        crop = Crop(seedKey)
    except AddonDataError as e:
        logger.error(e.message)
        return None
    cropMap[seedKey] = crop
    return crop
    
landMap = {} # type: dict[str, Land]

def GetLand(blockName):
    # type: (str) -> Land | None
    """获取土地实例，单例模式"""
    land = landMap.get(blockName)
    if land is not None:
        return land
    try:
        land = Land(blockName)
    except AddonDataError as e:
        logger.warn(e.message)
        return None
    landMap[blockName] = land
    return land
    
recipeMap = {} # type: dict[str, Recipe]

def GetRecipe(blockName):
    # type: (str) -> Recipe | None
    """获取生态实例，单例模式"""
    recipe = recipeMap.get(blockName)
    if recipe is not None:
        return recipe
    try:
        recipe = Recipe(blockName)
    except AddonDataError as e:
        logger.warn(e.message)
        return None
    recipeMap[blockName] = recipe
    return recipe
    
itemMap = {} # type: dict[str, Item]

def GetItem(itemName):
    # type: (str) -> Item | None
    """获取物品实例，单例模式"""
    item = itemMap.get(itemName)
    if item is not None:
        return item
    try:
        item = Item(itemName)
    except AddonDataError as e:
        logger.warn(e.message)
        return None
    itemMap[itemName] = item
    return item

__all__ = ['GetBiome', 'GetCrop', 'GetLand', 'GetRecipe']
