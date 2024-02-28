from scripts.workbench.server.data.recipes import WORKBENCH_MAP
from scripts.common import logger
from scripts.common.utils import itemUtils
from scripts.workbench.server.entity import Recipe

class RecipeProxy(object):
    def __init__(self, blockName):
        object.__init__(self)
        self.recipe = Recipe(blockName)
        self.matchedRecipeKey = None
        self.matchedRecipeMaterial = None
        self.matchedRecipeResult = None
        self.resultSlotNum = WORKBENCH_MAP[blockName]['result']

    def GetLastUsedRecipeMaterial(self):
        # type: () -> dict[str, dict]
        return self.matchedRecipeMaterial or self.recipe.GetMaterial(self.matchedRecipeKey) if self.matchedRecipeKey else None
    
    def GetLastUsedRecipeResult(self):
        # type: () -> dict[str, dict]
        return self.matchedRecipeResult or self.recipe.GetResult(self.matchedRecipeKey) if self.matchedRecipeKey else None

    def MatchRecipe(self, materialSlotItemDict):
        # type: (dict[str, dict[str, dict]]) -> dict[str, dict]
        """配方原材料匹配，如果成功返回结果槽字典"""
        # 过滤值为 None 的元素
        materialSlotItemDict = { k:v for k,v in materialSlotItemDict.items() if v }
        for recipeKey, recipe in self.recipe.GetAllRecipe().items():
            materials = self.recipe.GetMaterial(recipe = recipe)
            if len(materials) != len(materialSlotItemDict):
                continue
            matchCount = 0
            for slotName, itemDict in materials.items():
                matchCount += 1
                workbenchItemDict = materialSlotItemDict.get(slotName)
                if not self.__CanMatch(itemDict, workbenchItemDict):
                    break
                if matchCount == len(materials):
                    self.matchedRecipeKey = recipeKey
                    self.matchedRecipeMaterial = self.recipe.GetMaterial(recipe = recipe)
                    self.matchedRecipeResult = self.recipe.GetResult(recipe = recipe)
                    return self.matchedRecipeResult
        self.matchedRecipeKey = None
        self.matchedRecipeMaterial = None
        self.matchedRecipeResult = None
        return {
            'result_slot' + str(index) : None
            for index in range(self.resultSlotNum)
        }

    def __CanMatch(self, recipeDict, workbenchDict):
        # type: (dict, dict | None) -> bool
        """判读能否匹配槽物品"""
        return workbenchDict is not None and itemUtils.IsSameItem(recipeDict, workbenchDict) and workbenchDict.get('count') >= recipeDict.get('count')
