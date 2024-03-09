from abc import abstractmethod
from scripts.common import modConfig
from scripts.common import logger
from scripts.common.utils import itemUtils, strUtils
from scripts.workbench.common.events import WorkbenchOutSlotClickEvent, WorkbenchSlotItemSwapEvent
from scripts.workbench.client.ui.base.BaseBlockScreen import BaseBlockScreen
from scripts.workbench.client.ui.manager import NodeStateMachine, SlotManager
from scripts.workbench.client.ui.manager.NodeStateMachine import NodeState, EventType
from scripts.workbench.client.ui.utils import slotUtils
import mod.client.extraClientApi as clientApi

playerId = clientApi.GetLocalPlayerId()
levelId = clientApi.GetLevelId()
engineCompFactory = clientApi.GetEngineCompFactory()
itemComp = engineCompFactory.CreateItem(playerId)

maxResultWareMap = {
    "ham:pan": 3.0,
    "ham:stew_pot": 5.0
}

"""
UI 必须包含如下结构
|- main
    |- inventory_panel
        |- bag_grid
        |- hand_grid
        |- item_detail
        |- progressive_bar
grid 的元素 item_slot 具有以下结构
|- item_slot
    |- item_renderer
    |- count_label
    |- item_button
    |- selected_image
    |- durability_bar
"""
class BaseInventoryScreen(BaseBlockScreen):

    def __init__(self, namespace, name, param):
        BaseBlockScreen.__init__(self, namespace, name, param)
        self.__InitPanelPath()
        self.__InitData()

    def __InitPanelPath(self):
        self.inventoryPanelPath = "/inventory_panel"
        self.bagGridPath = self.inventoryPanelPath + "/bag_grid"
        self.handGridPath = self.inventoryPanelPath + "/hand_grid"
        self.progressiveBarPath = self.inventoryPanelPath + "/progressive_bar"
        self.progressiveBarImagePath = self.progressiveBarPath + "/bar_mask"
        self.itemDetail = self.inventoryPanelPath + "/item_detail"
        self.itemDetailBgPath = self.itemDetail + "/item_detail_bg"
        self.itemDetailTextPath = self.itemDetailBgPath + "/item_detail_text"

    def __InitData(self):
        self.clientSystem = clientApi.GetSystem(modConfig.ADDON_NAME, modConfig.WORKBENCH_CLIENT_NAME)
        self.lastSelectedPath = None
        self.lastTouchButtonPath = None
        self.lastTouchPosition = None
        self.holdTime = None
        self.isDoubleClick = False
        self.detailAlpha = 0.0
        self.clickInterval = 0
        self.takePercent = 1
        self.slotMgr = SlotManager()

    def Create(self):
        BaseBlockScreen.Create(self)
        self.__CreateUIControl()
        self.__RegisterStateMachine()

    def __CreateUIControl(self):
        self.progressiveBarImageControl = self.GetBaseUIControl(
            self.progressiveBarImagePath).asImage()
        self.progressiveBarControl = self.GetBaseUIControl(
            self.progressiveBarPath).asImage()
        self.itemDetailBgControl = self.GetBaseUIControl(
            self.itemDetailBgPath).asImage()
        self.itemDetailTextControl = self.GetBaseUIControl(
            self.itemDetailTextPath).asLabel()

    def __RegisterStateMachine(self):
        self.stateMachine = NodeStateMachine()
        # 注册节点
        self.stateMachine.AddNode(NodeState.Idle, self._HandleIdle)
        self.stateMachine.AddNode(NodeState.Select, self._HandleSelected)
        self.stateMachine.AddNode(NodeState.UnSelect, self._HandleUnSelected)
        self.stateMachine.AddNode(NodeState.Swap, self._HandleSwap)
        self.stateMachine.AddNode(NodeState.KeepSelect, self._HandleKeepSelect)
        self.stateMachine.AddNode(NodeState.KeepSelectComplete, self._HandleKeepSelectComplete)
        self.stateMachine.AddNode(NodeState.KeepSelectCancel, self._HandleKeepSelectCancel)
        self.stateMachine.AddNode(NodeState.Coalesce, self._HandleCoalesce)
        # 注册状态转移路径
        self.stateMachine.AddEdge(NodeState.Idle, NodeState.Select, self._CanSelect)
        self.stateMachine.AddEdge(NodeState.Idle, NodeState.KeepSelect, self._CanKeepSelect)
        self.stateMachine.AddEdge(NodeState.Select, NodeState.UnSelect, self._CanUnSelected)
        self.stateMachine.AddEdge(NodeState.Select, NodeState.Swap, self._CanSwap)
        self.stateMachine.AddEdge(NodeState.Select, NodeState.Coalesce, self._CanCoalesce)
        self.stateMachine.AddEdge(NodeState.KeepSelect, NodeState.KeepSelectCancel, self._CanProgressiveCancel)
        self.stateMachine.AddEdge(NodeState.KeepSelect, NodeState.KeepSelectComplete, self._CanProgressiveComplete)
        self.stateMachine.AddEdge(NodeState.KeepSelectComplete, NodeState.Swap, self._CanSwap)
        self.stateMachine.AddEdge(NodeState.KeepSelectComplete, NodeState.KeepSelectCancel, self._CanUnSelected)

    def _HandleIdle(self, buttonPath):
        """进入默认状态: 基础属性重置，不显示选中图片"""
        self.clickInterval = 0
        self.holdTime = None
        self.lastTouchButtonPath = None
        self.isDoubleClick = False
        self.takePercent = 1
        self.progressiveBarControl.SetVisible(False)
        if self.lastSelectedPath:
            self.GetBaseUIControl(self.lastSelectedPath + "/selected_image").SetVisible(False)
            self.lastSelectedPath = None

    def _HandleSelected(self, buttonPath):
        """处理选中按钮: 显示选中图片"""
        self.lastSelectedPath = slotUtils.GetSlotPath(buttonPath)
        self.GetBaseUIControl(self.lastSelectedPath + "/selected_image").SetVisible(True)

    def _HandleUnSelected(self, buttonPath):
        """处理未被选中: 状态重置"""
        self.stateMachine.ResetToDefault(buttonPath)

    def _HandleSwap(self, buttonPath):
        """处理物品交换: 向服务端传入 WorkbenchSlotItemSwapEvent 事件及相关数据"""
        if not self.lastSelectedPath:
            logger.error("交换失败，为找到最后选中的槽")
            return
        args = self.clientSystem.CreateEventData()
        args['fromSlotName'] = self.slotMgr.GetSlotName(slotUtils.GetSlotPath(self.lastSelectedPath))
        args['toSlotName'] = self.slotMgr.GetSlotName(slotUtils.GetSlotPath(buttonPath))
        args['fromItemDict'] = self.slotMgr.GetSlotItem(slotPath = slotUtils.GetSlotPath(self.lastSelectedPath))
        args['toItemDict'] = self.slotMgr.GetSlotItem(slotPath = slotUtils.GetSlotPath(buttonPath))
        args['takePercent'] = self.takePercent
        args['position'] = self.position
        args['dimensionId'] = self.dimensionId
        args['playerId'] = playerId
        args['blockName'] = self.blockName
        self.clientSystem.NotifyToServer(WorkbenchSlotItemSwapEvent, args)
        self.stateMachine.ResetToDefault(buttonPath)

    def _HandleKeepSelect(self, buttonPath):
        """处理长按按钮"""
        self._HandleSelected(buttonPath)
        inventoryPanelPos = self.GetBaseUIControl(self.inventoryPanelPath).GetPosition()
        self.progressiveBarControl.SetPosition((
            self.lastTouchPosition[0] - inventoryPanelPos[0] - 8,
            self.lastTouchPosition[1] - inventoryPanelPos[1] - 4
        ))
        self.progressiveBarControl.SetVisible(True)

    def _HandleKeepSelectComplete(self, buttonPath):
        """处理长按按钮分堆结束"""
        self.holdTime = None

    def _HandleKeepSelectCancel(self, buttonPath):
        """处理取消长按后分堆"""
        self.stateMachine.ResetToDefault(buttonPath)

    def _HandleCoalesce(self, buttonPath):
        # type: (str) -> None
        """处理合堆"""
        # FIXME 并没有触发合堆操作
        slotName = self.slotMgr.GetSlotName(slotUtils.GetSlotPath(buttonPath))
        if slotUtils.IsResultSlot(slotName):
            self.stateMachine.ResetToDefault(buttonPath)

        itemDict = self.slotMgr.GetSlotItem(slotPath = slotUtils.GetSlotPath(buttonPath))
        itemInfo = self._GetItemBasicInfoFromSlotItemDict(itemDict)
        maxStackSize = itemInfo.get('maxStackSize')

        if maxStackSize > 1 and maxStackSize < itemDict.get('count'):
            itemName = itemDict.get("newItemName")
            for path in self.slotMgr.GetAllSlotPath():
                if slotUtils.GetSlotPath(buttonPath) == path or slotUtils.IsResultSlot(itemName):
                    continue
                currentItem = self.slotMgr.GetSlotItem(slotPath = path)
                if itemUtils.IsSameItem(currentItem, itemDict):
                    if currentItem.get("count") == maxStackSize:
                        break
                    self.lastSelectedPath = path
                    self._HandleSwap(buttonPath)

        self.GetBaseUIControl(slotUtils.GetSlotPath(buttonPath) + "/selected_image").SetVisible(False)
        self.stateMachine.ResetToDefault(buttonPath)

    def _CanSelect(self, path, eventType):
        # type: (str, int) -> bool
        """判断是否可选"""
        if not path:
            return False
        item = self.slotMgr.GetSlotItem(slotPath = slotUtils.GetSlotPath(path))
        return item and eventType == EventType.Clicked
    
    def _CanUnSelected(self, path, eventType):
        # type: (str, int) -> bool
        """判断不被选中"""
        return path and slotUtils.GetSlotPath(path) == self.lastSelectedPath and eventType == EventType.Clicked
    
    def _CanSwap(self, path, eventType):
        # type: (str, int) -> bool
        """判断可以交换"""
        return path and slotUtils.GetSlotPath(path) != self.lastSelectedPath and eventType == EventType.Clicked
    
    def _CanCoalesce(self, path, eventType):
        # type: (str, int) -> bool
        """判断能否合并"""
        return eventType == EventType.DoubleClick
    
    def _CanKeepSelect(self, path, eventType):
        # type: (str, int) -> bool
        """判断可以长按分堆"""
        if not path:
            return False
        itemDict = self.slotMgr.GetSlotItem(slotPath = slotUtils.GetSlotPath(path))
        if not itemDict or eventType != EventType.Pressed:
            return False
        itemInfo = self._GetItemBasicInfoFromSlotItemDict(itemDict)
        if not itemInfo:
            return False
        maxStackSize = itemInfo.get("maxStackSize")
        return maxStackSize > 1
    
    def _CanProgressiveCancel(self, path, eventType):
        # type: (str, int) -> bool
        """判断取消长按分堆"""
        return not path and eventType == EventType.Released

    def _CanProgressiveComplete(self, path, eventType):
        # type: (str, int) -> bool
        """判断完成长按分堆"""
        return path and eventType == EventType.Released
    
    def _ShowItemDetail(self, itemDict):
        # type: (dict) -> None
        """显示物品详细信息 UI"""
        detailText = itemComp.GetItemFormattedHoverText(
            itemDict["newItemName"], itemDict["newAuxValue"], True,
            itemDict.get("userData"))
        self.itemDetailTextControl.SetText(detailText)
        self.itemDetailBgControl.SetPosition((0, 50))
        self.detailAlpha = 2.0

    def SetSlotUI(self, slotPath, itemDict):
        # type: (str, dict) -> None
        """设置 slotPath 槽物品的UI"""
        if itemDict and itemDict.get('count'):
            if 'result_ware_slot' not in slotPath:
                self.__SetDurabilityUI(slotPath, itemDict)
            self.__SetItemRendererUI(slotPath, itemDict, 'result_ware_slot' not in slotPath)
        else:
            if 'result_ware_slot' not in slotPath:
                self.GetBaseUIControl(slotPath + "/count_label").SetVisible(False)
                self.GetBaseUIControl(slotPath + "/durability_bar").SetVisible(False)
            self.GetBaseUIControl(slotPath + "/item_renderer").SetVisible(False)
        if 'result_ware_slot' in slotPath:
            self.__SetResultWareUI(slotPath, itemDict)

    def __SetDurabilityUI(self, slotPath, itemDict):
        # 计算耐久值
        durabilityRatio = 1
        basicInfo = self._GetItemBasicInfoFromSlotItemDict(itemDict)
        currentDurability = itemDict.get("durability")
        maxDurability = basicInfo.get("maxDurability", 0)
        if maxDurability != 0:
            durabilityRatio = currentDurability * 1.0 / maxDurability

        # 设置耐久条
        barImagePath = slotPath + "/durability_bar/bar_mask"
        barImageControl = self.GetBaseUIControl(barImagePath).asImage()
        barControl = self.GetBaseUIControl(slotPath + "/durability_bar")
        if durabilityRatio != 1:
            barImageControl.SetSpriteColor(
                (1 - durabilityRatio, durabilityRatio, 0))
            barImageControl.SetSpriteClipRatio(1 - durabilityRatio)
            barControl.SetVisible(True)
        else:
            barControl.SetVisible(False)

    def __SetResultWareUI(self, slotPath, itemDict):
        # 设置容器结果槽 UI
        maxResultWareCount = maxResultWareMap.get(self.blockName)
        if not maxResultWareCount:
            logger.error('{}不存在容器结果槽'.format(self.blockName))
        maskPath = slotPath + "/item_cell_mask"
        maskControl = self.GetBaseUIControl(maskPath).asImage()
        ratio = 1.0 if itemDict is None else 1 - itemDict.get('count') / maxResultWareCount
        maskControl.SetSpriteClipRatio(ratio)

    def __SetItemRendererUI(self, slotPath, itemDict, setCount = True):
        # 显示物品
        isEnchant = bool(itemDict.get('enchantData'))
        userData = itemDict.get('userData')
        itemRenderer = self.GetBaseUIControl(slotPath + "/item_renderer").asItemRenderer()
        itemRenderer.SetUiItem(itemDict["newItemName"],itemDict["newAuxValue"], isEnchant, userData)
        self.GetBaseUIControl(slotPath + "/item_renderer").SetVisible(True)

        # 显示数量
        if not setCount:
            return
        countLabelControl = self.GetBaseUIControl(slotPath + "/count_label").asLabel()
        countLabelControl.SetText(str(itemDict["count"]))
        countVisible = bool(itemDict["count"] > 1)
        countLabelControl.SetVisible(countVisible)

    def _GetItemBasicInfoFromSlotItemDict(self, itemDict):
        # type: (dict) -> dict
        newItemName = itemDict.get("newItemName", "")
        newAuxValue = itemDict.get("newAuxValue", 0)
        return itemComp.GetItemBasicInfo(newItemName, newAuxValue)

    def ShowUI(self, inventoryData):
        # BaseBlockScreen.ShowUI(self)
        self.UpdateInventoryUI(inventoryData)
        self.__RegisterButtonCallback()

    def __RegisterButtonCallback(self):
        for path in self.slotMgr.GetAllSlotPath():
            # 容器结果槽禁止交互
            if 'result_ware_slot' in path:
                continue
            buttonPath = strUtils.JoinPath(path, "item_button")
            buttonControl = self.GetBaseUIControl(buttonPath).asButton()
            buttonControl.AddTouchEventParams({"isSwallow": True})
            if slotUtils.IsResultSlot(self.slotMgr.GetSlotName(path)):
                buttonControl.SetButtonTouchDownCallback(self._OnResultButtonTouchDown)
            else:
                buttonControl.SetButtonTouchDownCallback(self._OnButtonTouchDown)
            buttonControl.SetButtonTouchUpCallback(self._OnButtonTouchUp)
            buttonControl.SetButtonTouchCancelCallback(self._OnButtonTouchCancel)
            buttonControl.SetButtonTouchMoveCallback(self._OnButtonTouchMove)
            buttonControl.SetButtonTouchMoveInCallback(self._OnButtonTouchMoveIn)
            buttonControl.SetButtonTouchMoveOutCallback(self._OnButtonTouchMoveOut)

    def _OnResultButtonTouchDown(self, args):
        touchPos = (args["TouchPosX"], args["TouchPosY"])
        self.lastTouchPosition = touchPos
        buttonPath = args["ButtonPath"]
        self.lastTouchButtonPath = buttonPath
        slotPath = slotUtils.GetSlotPath(buttonPath)
        slotName = self.slotMgr.GetSlotName(slotPath)
        itemDict = self.slotMgr.GetSlotItem(slotName = slotName) 
        if itemDict is None:
            return
        self._ShowItemDetail(itemDict)
        self.isDoubleClick = False
        args = self.clientSystem.CreateEventData()
        args['item'] = itemDict
        args['slotName'] = slotName
        args['position'] = self.position
        args['dimensionId'] = self.dimensionId
        args['playerId'] = playerId
        args['blockName'] = self.blockName
        self.clientSystem.NotifyToServer(WorkbenchOutSlotClickEvent, args)
        self.SetSlotUI(slotPath, None)

    def _OnButtonTouchDown(self, args):
        """按钮按下事件: 展示详细信息，判断是否双击，获取最后点击的按钮 path 与 position"""
        touchPos = args["TouchPosX"], args["TouchPosY"]
        buttonPath = args["ButtonPath"]
        slotPath = slotUtils.GetSlotPath(buttonPath)
        self.lastTouchButtonPath = args["ButtonPath"]
        self.lastTouchPosition = touchPos
        itemDict = self.slotMgr.GetSlotItem(slotPath=slotPath)
        if itemDict:
            self._ShowItemDetail(itemDict)
        if self.clickInterval > 0 and self.lastTouchButtonPath == args["ButtonPath"]:
            self.isDoubleClick = True
            return
        self.isDoubleClick = False
        self.holdTime = 0

    def _OnButtonTouchUp(self, args):
        """按钮弹起事件: 双击，长按，普通弹起，交由 stateMachine 处理"""
        if self.isDoubleClick:
            self.stateMachine.ReceiveEvent(args["ButtonPath"], EventType.DoubleClick)
        elif self.holdTime and self.holdTime < 10:
            self.stateMachine.ReceiveEvent(args["ButtonPath"], EventType.Clicked)
        else:
            self.stateMachine.ReceiveEvent(args["ButtonPath"], EventType.Released)
        self.holdTime = None
        self.clickInterval = 4

    def _OnButtonTouchCancel(self, args):
        """按钮取消事件: 长按时间归零"""
        self.holdTime = None
        self.stateMachine.ReceiveEvent(args["ButtonPath"], EventType.Released)

    def _OnButtonTouchMove(self, args):
        """按钮移走事件"""
        self.stateMachine.ReceiveEvent(args["ButtonPath"], EventType.Released)

    def _OnButtonTouchMoveIn(self, args):
        """按钮移入事件: 不做处理"""
        pass

    def _OnButtonTouchMoveOut(self, args):
        """按钮移入出事件：按钮 release"""
        self.holdTime = None
        self.stateMachine.ReceiveEvent(self.lastTouchButtonPath, EventType.Released)

    def CloseUI(self):
        if self.lastSelectedPath:
            lastSelectedItemRenderControl = self.GetBaseUIControl(
                self.lastSelectedPath + "/selected_image").asImage()
            lastSelectedItemRenderControl.SetVisible(False)
            self.lastSelectedPath = None
        self.stateMachine.ResetToDefault()

    def Update(self):
        if not self.isShow:
            return
        if self.holdTime is not None:
            self.holdTime += 1
            if self.holdTime == 10:
                self.stateMachine.ReceiveEvent(self.lastTouchButtonPath, EventType.Pressed)
            if self.stateMachine.IsCurrentNodeState(NodeState.KeepSelect):
                itemDict = self.slotMgr.GetSlotItem(slotPath = slotUtils.GetSlotPath(self.lastTouchButtonPath))
                # 计算长安状态下的分堆比例
                holdTime = self.holdTime - 10
                if holdTime > 20:
                    self.takePercent = 1
                    return
                itemCount = itemDict.get("count")
                takeNum = holdTime * itemCount / 20
                if takeNum == 0:
                    takeNum = 1
                    self.holdTime = takeNum * 20 / itemCount + 10
                self.takePercent = takeNum * 1.0 / itemCount
                self.progressiveBarImageControl.SetSpriteClipRatio(1 - self.takePercent)
        if self.clickInterval > 0:
            self.clickInterval -= 1
        if self.detailAlpha > 0:
            self.detailAlpha -= 0.04
        if self.detailAlpha >= 1:
            self.itemDetailBgControl.SetAlpha(1)
            self.itemDetailTextControl.SetAlpha(1)
        else:
            self.itemDetailBgControl.SetAlpha(self.detailAlpha)
            self.itemDetailTextControl.SetAlpha(self.detailAlpha)

    def UpdateInventoryUI(self, inventoryData):
        # type: (dict) -> None
        """更新 UI 的 Inventory 界面"""
        handGridList = self.GetChildrenName(self.handGridPath)
        bagGridList = self.GetChildrenName(self.bagGridPath)
        for index, inventoryGridSlot in enumerate(handGridList + bagGridList):
            gridPath = self.handGridPath if index < 9 else self.bagGridPath
            slotPath = strUtils.JoinPath(gridPath, inventoryGridSlot)
            itemDict = inventoryData.get(index, None)
            # 更新UI记录的信息
            self.slotMgr.SetSlotInfo(index, slotPath, itemDict)
            self.SetSlotUI(slotPath, itemDict)

    @abstractmethod
    def UpdateUI(self, slotData):
        """更新工作台界面"""
        pass