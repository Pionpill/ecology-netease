from scripts.common import logger
from scripts.common.data.workbench.slot import SLOT_DATA
from scripts.common.entity import GetRecipe
from scripts.common.utils import itemUtils


class RecipeManager(object):
    def __init__(self, blockName):
        object.__init__(self)
        recipe = GetRecipe(blockName)
        if recipe is None:
            return
        self.__recipe = recipe
        self.__resultSlotNum = SLOT_DATA[blockName]['result']
        self.__matchedRecipeKey = None

    def GetLastUsedRecipeMaterial(self):
        # type: () -> dict[str, dict | None] | None
        return self.__recipe.GetMaterialByKey(self.__matchedRecipeKey) if self.__matchedRecipeKey else None
    
    def GetLastUsedRecipeResult(self):
        # type: () -> dict[str, dict | None] | None
        return self.__recipe.GetResultByKey(self.__matchedRecipeKey) if self.__matchedRecipeKey else None
    
    def MatchRecipe(self, materialSlotItemDict):
        # type: (dict[str, dict[str, dict] | None]) -> dict[str, dict | None]
        """配方原材料匹配，如果成功返回结果槽字典"""
        materialSlotItemDict = itemUtils.FilterDict(materialSlotItemDict)
        for recipeKey, recipe in self.__recipe.GetAllRecipe().items():
            recipeMaterial = self.__recipe.GetRecipeMaterial(recipe)
            slotMaterialLength = sum(1 for key in materialSlotItemDict.keys() if 'fixed' not in key)
            recipeMaterialLength = sum(1 for key in recipeMaterial.keys() if 'fixed' not in key and 'result' not in key)
            # 非固定槽物品数量不同，认为不匹配
            if slotMaterialLength != recipeMaterialLength:
                continue
            matchCount = 0
            for slotName, recipeItemDict in recipeMaterial.items():
                matchCount += 1
                workbenchItemDict = materialSlotItemDict.get(slotName)
                if not self.__CanMatch(recipeItemDict, workbenchItemDict):
                    break
                if matchCount == len(recipeMaterial):
                    self.__matchedRecipeKey = recipeKey
                    return self.__recipe.GetRecipeResult(recipe)
        self.__matchedRecipeKey = None
        return {
            'result_slot' + str(index) : None
            for index in range(self.__resultSlotNum)
        }

    def __CanMatch(self, recipeItemDict, workbenchItemDict):
        # type: (dict | None, dict | None) -> bool
        """判读能否匹配槽物品"""
        if recipeItemDict is None or workbenchItemDict is None:
            return recipeItemDict is None and workbenchItemDict is None
        workbenchItemCount = workbenchItemDict.get('count')
        recipeItemCount = recipeItemDict.get('count')
        if workbenchItemCount is None or recipeItemCount is None:
            logger.error('匹配配方时，工作台或匹配物品数量为空，这是一个程序BUG')
            return False
        return itemUtils.IsSameItem(recipeItemDict, workbenchItemDict) and workbenchItemCount >= recipeItemCount