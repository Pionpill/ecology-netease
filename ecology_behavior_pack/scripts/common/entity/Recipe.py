from scripts.common import logger
from scripts.common.data.workbench.slot import SLOT_DATA
from scripts.common.error import AddonDataError
from scripts.common.utils import itemUtils


class Recipe(object):
    def __init__(self, blockName):
        # type: (str) -> None
        object.__init__(self)
        slotData = SLOT_DATA.get(blockName)
        if not slotData:
            raise AddonDataError('不存在 {} 工作台数据'.format(blockName))
        self.__recipe = slotData.get('recipe', {})  # type: dict[str, dict]
        self.__fixedMaterialItems = slotData.get('fixed_material_items')
        self.__slotNum = {
            'material': slotData['material'],
            'fixed_material': len(slotData.get('fixed_material_items', ())),
            'liquid': slotData.get('liquid', 0),
            'fuel': slotData.get('fuel', 0),
            'result': slotData['result']
        }
        self.__type = slotData['type']

    def GetSlotNum(self):
        # type: () -> dict[str, int]
        return self.__slotNum

    def GetMaterialNum(self, fixedInclude=False):
        # type: (bool) -> int
        if fixedInclude:
            return self.__slotNum['material'] + self.GetFixedMaterialNum()
        return self.__slotNum['material']
    
    def GetFixedMaterialNum(self):
        # type: () -> int
        return self.__slotNum['fixed_material']
    
    def GetLiquidNum(self):
        # type: () -> int
        return self.__slotNum['liquid']

    def GetFuelNum(self):
        # type: () -> int
        return self.__slotNum['fuel']

    def GetResultNum(self):
        # type: () -> int
        return self.__slotNum['result']

    def GetType(self):
        # type: () -> str
        return self.__type

    def GetAllRecipe(self):
        # type: () -> dict[str, dict]
        return self.__recipe
    
    def GetRecipe(self, recipeKey):
        # type: (str) -> dict[str, dict] | None
        return self.__recipe.get(recipeKey)
    
    def GetFormatRecipe(self, recipeKey):
        material = self.GetMaterialByKey(recipeKey)
        result = self.GetResultByKey(recipeKey)
        return {k: v for d in [material, result] for k, v in d.items()}

    def GetMaterialByKey(self, recipeKey):
        """通过配方键获取原材料"""
        recipe = self.GetRecipe(recipeKey)
        if recipe is None:
            return {}
        return self.__FormatRecipe(recipe, 'material')
    
    def GetRecipeMaterial(self, recipe):
        return self.__FormatRecipe(recipe, 'material')

    def GetResultByKey(self, recipeKey):
        recipe = self.GetRecipe(recipeKey)
        if recipe is None:
            return {}
        return self.__FormatRecipe(recipe, 'result')
    
    def GetRecipeResult(self, recipe):
        return self.__FormatRecipe(recipe, 'result')

    def __FormatRecipe(self, recipe, type):
        # type: (dict[str, dict], str) -> dict[str, dict | None]
        """❗️ 将数据转换为统一格式"""
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
        # 槽值是 str，说明值就是结果物品
        if isinstance(materialOrResultDict, str):
            return {type + '_slot0': itemUtils.GetItemDict(materialOrResultDict)}
        # 仅一个物品，默认槽位为 0
        if materialOrResultDict.get('newItemName'):
            return {type + '_slot0': itemUtils.GetItemDict(itemDict = materialOrResultDict)} # type: ignore
        outDict = {type + '_slot' + str(slotIndex) : itemUtils.GetItemDict(itemName = item) if isinstance(item, str) else itemUtils.GetItemDict(itemDict = item) for slotIndex, item in materialOrResultDict.items()}
        if type == 'material' and self.__fixedMaterialItems:
            fixedMaterial = recipe.get("fixed_material", tuple([0] * len(self.__fixedMaterialItems)))
            for slotIndex, count in enumerate(fixedMaterial):
                if count == 0:
                    continue
                outDict["fixed_material_slot"+str(slotIndex)] = itemUtils.GetItemDict(self.__fixedMaterialItems[slotIndex], 0, count)
        return outDict