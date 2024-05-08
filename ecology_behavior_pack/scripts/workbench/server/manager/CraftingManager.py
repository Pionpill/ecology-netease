import mod.server.extraServerApi as serverApi
from scripts.common.data.workbench import CONVERT_DATA
from scripts.common.utils import itemUtils
from scripts.common import logger
from scripts.workbench.server.manager.base import BaseWorkbenchManager

compFactory = serverApi.GetEngineCompFactory()
levelId = serverApi.GetLevelId()
itemComp = compFactory.CreateItem(levelId)

class CraftingManager(BaseWorkbenchManager):
    def __init__(self, blockName, position, dimensionId):
        # type: (str, tuple[int, int, int], int) -> None
        BaseWorkbenchManager.__init__(self, blockName, position, dimensionId)

    def Consume(self, playerId):
        """工作台合成物品"""
        materialSlotItemDict = self.recipeManager.GetLastUsedRecipeMaterial()
        if materialSlotItemDict is None:
            return
        for slotName, itemDict in materialSlotItemDict.items():
            if itemDict is None:
                continue
            itemName = itemDict.get('newItemName')
            if itemName is None:
                return
            count = itemDict.get("count", 1)
            convertItemName = CONVERT_DATA.get(itemName)
            if convertItemName:
                itemComp.SpawnItemToPlayerInv(itemUtils.GetItemDict(convertItemName, 0, count),  playerId)
            self.ReduceItem(slotName, count)
    
    def Reset(self, playerId):
        # type: (str) -> None
        """重置工作台，将非固定材料槽物品返回"""
        resetMaterialSlotNum = self.slotNum['material']
        for i in range(resetMaterialSlotNum):
            slotKey = 'material_slot' + str(i)
            itemComp.SpawnItemToPlayerInv(self.GetSlotData(slotKey),  playerId)
            self.blockEntityData[slotKey] = None