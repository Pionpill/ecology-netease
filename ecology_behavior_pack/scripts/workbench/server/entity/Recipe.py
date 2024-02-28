from scripts.common import logger
from scripts.common.utils import itemUtils
from scripts.workbench.server.data import WORKBENCH_MAP

class Recipe(object):
    def __init__(self, blockName):
        # type: (str) -> None
        object.__init__(self)
        self.recipe = WORKBENCH_MAP[blockName]['recipe']

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
        # type: (dict, str[str, dict]) -> dict[str, dict]
        """将数据转换为统一格式"""
        if not type in ['material', 'result']:
            logger.error(type + ' 不属于工作台配方的键')
        if isinstance(recipe, str):
            return {
                type + '_slot0': itemUtils.GetItemDict(itemName = recipe)
            }
        materialOrResultDict = recipe.get(type)
        if materialOrResultDict is None:
            return {
                type + '_slot0': itemUtils.GetItemDict(itemDict = recipe)
            }
        if isinstance(materialOrResultDict, str):
            return {'result_slot0': itemUtils.GetItemDict(materialOrResultDict)}
        return {type + '_slot' + str(slotIndex) : itemUtils.GetItemDict(itemName = item) if isinstance(item, str) else itemUtils.GetItemDict(itemDict = item) for slotIndex, item in materialOrResultDict.items()}