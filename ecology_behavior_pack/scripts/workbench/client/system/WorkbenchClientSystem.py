import mod.client.extraClientApi as clientApi
from scripts.common import logger
from scripts.workbench.client.events import WorkbenchBlockUICloseClientEvent
from scripts.workbench.common.events import WorkbenchBlockUICloseEvent, WorkbenchBlockUseEvent, WorkbenchUIRefreshEvent
from scripts.workbench.client.ui.base import BaseBlockScreen

from scripts.common import modConfig
from scripts.workbench.client.manager import UIManager

ClientSystem = clientApi.GetClientSystemCls()
playerId = clientApi.GetLocalPlayerId()
compFactory = clientApi.GetEngineCompFactory()
itemComp = compFactory.CreateItem(playerId)
gameComp = compFactory.CreateGame(clientApi.GetLevelId())

class WorkbenchClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        self.ListenEvents()

    def ListenEvents(self):
        engineNamespace = clientApi.GetEngineNamespace()
        engineSystemName = clientApi.GetEngineSystemName()
        # 监听原生事件
        self.ListenForEvent(engineNamespace, engineSystemName, 'UiInitFinished', self, self.OnUiInitFinished)
        self.ListenForEvent(engineNamespace, engineSystemName, 'ActorAcquiredItemClientEvent', self, self.OnActorAcquiredItem)
        # 监听客户端事件
        self.ListenForEvent(modConfig.ADDON_NAME, modConfig.WORKBENCH_CLIENT_NAME, WorkbenchBlockUICloseClientEvent, self, self.OnClientWorkbenchBlockUIClose)
        # 监听服务端事件
        self.ListenForEvent(modConfig.ADDON_NAME, modConfig.WORKBENCH_SERVER_NAME, WorkbenchBlockUseEvent, self, self.OnWorkbenchBlockUse)
        self.ListenForEvent(modConfig.ADDON_NAME, modConfig.WORKBENCH_SERVER_NAME, WorkbenchUIRefreshEvent, self, self.OnWorkbenchUIRefresh)
        self.ListenForEvent(modConfig.ADDON_NAME, modConfig.WORKBENCH_SERVER_NAME, WorkbenchBlockUICloseEvent, self, self.OnServerWorkbenchUIClose)

    def OnUiInitFinished(self, args):
        UIManager.Init()

    def OnActorAcquiredItem(self, args):
        usingBlock = UIManager.currentUsingBlock
        if usingBlock is None:
            return
        inventoryData = self.__GetInventoryData()
        blockUINode = UIManager.GetUINode(usingBlock)
        blockUINode.UpdateInventoryUI(inventoryData)

    def OnWorkbenchBlockUse(self, args):
        """工作台使用事件"""
        blockName = args['blockName']
        blockUINode = UIManager.GetUINode(blockName)
        # 延迟一帧执行，确保UI初始化完成
        gameComp.AddTimer(0.05, self.__ShowUI, blockUINode, args)

    def __ShowUI(self, blockUINode, args):
        # type: ( BaseBlockScreen, dict ) -> None
        inventoryData = self.__GetInventoryData()
        blockUINode.ShowUI(inventoryData, args)

    def OnWorkbenchUIRefresh(self, args):
        usingBlockName = UIManager.GetCurrentUsingBlock()
        if usingBlockName is None:
            return
        inventoryData = self.__GetInventoryData()
        blockUINode = UIManager.GetUINode(usingBlockName)
        blockUINode.UpdateInventoryUI(inventoryData)
        # TODO slotData 不再从服务端获取，而是在客户端从 blockEntityData 中获取
        blockUINode.UpdateUI(args['slotData'], args['burnData'])

    def OnClientWorkbenchBlockUIClose(self, args):
        """工作台UI关闭事件"""
        UIManager.ResetUINode()
        clientApi.PopScreen()
        self.NotifyToServer(WorkbenchBlockUICloseEvent, args)

    def OnServerWorkbenchUIClose(self, args):
        if UIManager.currentUsingBlock is not None:
            UIManager.ResetUINode()
            clientApi.PopScreen()

    def __GetInventoryData(self):
        # type: () -> dict
        minecraftEnum = clientApi.GetMinecraftEnum()
        return {
            i: itemComp.GetPlayerItem(minecraftEnum.ItemPosType.INVENTORY, i, True)
            for i in range(36)
        }