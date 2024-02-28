from scripts.common.utils import strUtils
from scripts.common import logger
from scripts.workbench.client.ui.base import BaseInventoryScreen
import mod.client.extraClientApi as clientApi

playerId = clientApi.GetLocalPlayerId()
levelId = clientApi.GetLevelId()
engineCompFactory = clientApi.GetEngineCompFactory()

'''
UI 必须包含如下结构
|- main
    |- furnace_panel
        |- furnace_arrow_mask
        |- furnace_arrow_img
        |- flame_mask
        |- flame_img
'''

class FurnaceScreen(BaseInventoryScreen):
    def __init__(self, namespace, name, param):
        BaseInventoryScreen.__init__(self, namespace, name, param)
        self.__InitPanelPath()
        self.__InitData()

    def __InitPanelPath(self):
        self.furnacePanelPath = "/furnace_panel"
        self.flameMaskPath = self.furnacePanelPath + "/flame_mask"
        self.arrowMaskPath = self.furnacePanelPath + "/furnace_arrow_mask"

    def __InitData(self):
        self.isBurning = False
        self.isProducing = False
        self.burnProgress = 0
        self.burnDuration = 0
        self.produceProgress = 0
        self.blockType = 'furnace'

    def Create(self):
        BaseInventoryScreen.Create(self)
        self.flameMaskControl = self.GetBaseUIControl(self.flameMaskPath).asImage()
        self.arrowMaskControl = self.GetBaseUIControl(self.arrowMaskPath).asImage()
        self.flameMaskControl.SetClipDirection("fromTopToBottom")

    def Update(self):
        if not self.isShow:
            return
        BaseInventoryScreen.Update(self)
        # 更新燃烧动画
        if not self.isBurning:
            self.burnProgress = 0
            self.flameMaskControl.SetSpriteClipRatio(1)
        else:
            self.burnProgress += 1
            fireRatio = (self.burnProgress * 2.0) / (self.burnDuration * 3.0)
            self.flameMaskControl.SetSpriteClipRatio(fireRatio)
            if fireRatio == 1:
                self.burnProgress = 0
        # 更新进程动画
        if not self.isProducing:
            self.produceProgress = 0
            self.arrowMaskControl.SetSpriteClipRatio(1)
        else:
            self.produceProgress += 1
            arrowRatio = self.produceProgress / (5 * 30.0)
            self.arrowMaskControl.SetSpriteClipRatio(1.0 - arrowRatio)
            if arrowRatio == 1:
                self.produceProgress = 0

    def ShowUI(self, inventoryData, args):
        # type: (dict, dict) -> None
        """显式 UI 并更新工作台数据"""
        self.position = args['position']
        self.dimensionId = args['dimensionId']
        self.blockName = args['blockName']
        self.blockType = args['blockType']
        self.UpdateUI(args['slotData'], args['burnData'])
        BaseInventoryScreen.ShowUI(self, inventoryData)

    def UpdateUI(self, slotData, burnData):
        # type: (dict, dict) -> None
        """更新工作台数据"""
        for key, value in burnData.items():
            if key == "burnDuration" and value != self.burnDuration:
                self.burnDuration = value
                self.burnProgress = 0
            elif key == "burnProgress":
                self.burnProgress = value
            elif key == "isBurning":
                self.isBurning = value
            elif key == "isProducing":
                self.isProducing = value
            elif key == "produceProgress":
                self.produceProgress = value
        for slotName, itemDict in slotData.items():
            slotPath = strUtils.JoinPath(self.furnacePanelPath, slotName)
            self.slotMgr.SetSlotInfo(slotName, slotPath, itemDict)
            self.SetSlotUI(slotPath, itemDict)
