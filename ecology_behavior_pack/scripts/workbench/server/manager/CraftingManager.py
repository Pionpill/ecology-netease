import mod.server.extraServerApi as serverApi
from scripts.common import logger
from scripts.workbench.server.manager.base import BaseWorkbenchManager

compFactory = serverApi.GetEngineCompFactory()
levelId = serverApi.GetLevelId()
itemComp = compFactory.CreateItem(levelId)

class CraftingManager(BaseWorkbenchManager):
    def __init__(self, blockName, position, dimensionId):
        # type: (str, tuple[int, int, int], int) -> None
        BaseWorkbenchManager.__init__(self, blockName, position, dimensionId)

    def Consume(self):
        """工作台合成物品"""
        materialSlotItemDict = self.proxy.matchedRecipeMaterial
        if materialSlotItemDict is None:
            return
        for slotName, itemDict in materialSlotItemDict.items():
            if itemDict is None:
                continue
            count = itemDict.get("count")
            self._ItemReduce(slotName, count)

    def GetRecipeResultSlotItemDict(self):
        """获取匹配的物品"""
        materialSlotItemDict = self.GetAllSlotData(['material'])
        if len(materialSlotItemDict) == 0 or all(value is None for value in materialSlotItemDict.values()):
            return {'material_slot' + str(i): None for i in range(self.slotNum['result'])}
        return self.proxy.MatchRecipe(materialSlotItemDict)
    
    def Reset(self, playerId):
        # type: (int) -> None
        """重置工作台，将非固定材料槽物品返回"""
        resetMaterialSlotNum = self.slotNum['material'] - self.slotNum['fixed_material']
        for i in range(resetMaterialSlotNum):
            slotKey = 'material_slot' + str(i)
            itemComp.SpawnItemToPlayerInv(self.GetSlotData(slotKey),  playerId)
            self.blockEntityData[slotKey] = None

    def GetBurnData(self):
        """工作台没有熔炉数据"""
        return {}