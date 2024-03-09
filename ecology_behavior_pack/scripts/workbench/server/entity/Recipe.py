from scripts.common.data.workbench import SLOT_DATA
from scripts.common import logger
from scripts.common.utils import itemUtils

class Recipe(object):
    def __init__(self, blockName):
        # type: (str) -> None
        object.__init__(self)
        self.recipe = SLOT_DATA[blockName]['recipe']
        self.fixedMaterialItems = SLOT_DATA[blockName].get('fixed_material_items')

    def GetAllRecipe(self):
        # type: () -> dict[str, dict]
        return self.recipe

    def GetRecipe(self, recipeKey):
        # type: (str) -> dict[str, dict]
        return self.GetAllRecipe().get(recipeKey)
    
    def GetMaterial(self, recipeKey=None, recipe=None):
        # type: (str, dict) -> dict[str, dict]
        """获取原材料"""
        realRecipe = recipe or self.GetRecipe(recipeKey)
        return self.__GetMaterialFromRecipe(realRecipe, 'material')
    
    def GetResult(self, recipeKey=None, recipe=None):
        # type: (str, dict) -> dict[str, dict]
        """获取产品"""
        realRecipe = recipe or self.GetRecipe(recipeKey)
        return self.__GetMaterialFromRecipe(realRecipe, 'result')
    
    def __GetMaterialFromRecipe(self, recipe, type):
        # type: (dict[str, dict], str) -> dict[str, dict]
        """将数据转换为统一格式"""
        if not type in ['material', 'result']:
            logger.error(type + ' 不属于工作台配方的键')
        # 值是 str，说明值就是结果槽物品名，例如: "minecraft:apple": "minecraft:apple"
        if isinstance(recipe, str):
            return {
                type + '_slot0': itemUtils.GetItemDict(itemName = recipe)
            }
        materialOrResultDict = recipe.get(type)
        if materialOrResultDict is None:
            return {
                type + '_slot0': itemUtils.GetItemDict(itemDict = recipe)
            }
        # 槽值是 str，说明值就是结果物品，例如: "result": "ham:corn_pieces"
        if isinstance(materialOrResultDict, str):
            return {type + '_slot0': itemUtils.GetItemDict(materialOrResultDict)}
        outDict = {type + '_slot' + str(slotIndex) : itemUtils.GetItemDict(itemName = item) if isinstance(item, str) else itemUtils.GetItemDict(itemDict = item) for slotIndex, item in materialOrResultDict.items()}
        if type == 'material' and self.fixedMaterialItems:
            for slotIndex, count in enumerate(recipe.get("fixed_material")):
                if count == 0:
                    continue
                outDict["fixed_material_slot"+str(slotIndex)] = itemUtils.GetItemDict(self.fixedMaterialItems[slotIndex], 0, count)
        return outDict
