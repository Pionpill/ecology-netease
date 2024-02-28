from scripts.common import logger
from scripts.common.utils import strUtils
from scripts.workbench.client.ui.base import BaseInventoryScreen

'''
UI 必须包含如下结构
|- main
    |- crafting_panel
        |- material_slot0
        |- material_slot1
        |- ......
        |- result_slot0
        |- arrow_image
'''

class CraftingScreen(BaseInventoryScreen):
    def __init__(self, namespace, name, param):
        BaseInventoryScreen.__init__(self, namespace, name, param)
        self.craftingPanelPath = "/crafting_panel"

    def ShowUI(self, inventoryData, args):
        # type: (dict, dict) -> None
        """显式 UI 并更新工作台数据"""
        self.position = args['position']
        self.dimensionId = args['dimensionId']
        self.blockName = args['blockName']
        self.blockType = args['blockType']
        self.UpdateUI(args['slotData'])
        BaseInventoryScreen.ShowUI(self, inventoryData)

    def UpdateUI(self, slotData, burnData = {}):
        # type: (dict, dict) -> None
        """更新工作台数据"""
        for slotName, itemDict in slotData.items():
            slotPath = strUtils.JoinPath(self.craftingPanelPath, slotName)
            self.slotMgr.SetSlotInfo(slotName, slotPath, itemDict)
            self.SetSlotUI(slotPath, itemDict)
