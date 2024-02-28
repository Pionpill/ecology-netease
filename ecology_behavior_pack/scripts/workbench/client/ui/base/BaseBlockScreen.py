import mod.client.extraClientApi as clientApi
from scripts.common import modConfig, logger

from scripts.workbench.client.events import WorkbenchBlockUICloseClientEvent

playerId = clientApi.GetLocalPlayerId()
levelId = clientApi.GetLevelId()
ScreenNode = clientApi.GetScreenNodeCls()
compFactory = clientApi.GetEngineCompFactory()
gameComp = compFactory.CreateGame(levelId)

"""
UI 必须包含如下结构
|- main
    |- main_panel
        |- close_button
"""

class BaseBlockScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        # type: (str, str, any) -> BaseBlockScreen
        ScreenNode.__init__(self, namespace, name, param)
        self.__InitPanelPath()
        self.__InitData()

    def __InitPanelPath(self):
        self.mainPanelPath = "/main_panel"
        self.closeBthPath = self.mainPanelPath + "/close_button"

    def __InitData(self):
        self.isShow = False
        self.dimensionId = None
        self.position = None
        self.blockName = None
        self.blockType = None

    def Create(self):
        closeBtnController = self.GetBaseUIControl(self.closeBthPath).asButton()
        closeBtnController.AddTouchEventParams({"isSallow": True})
        closeBtnController.SetButtonTouchUpCallback(self._OnCloseBthTouchUp)
        self.isShow = True

    def _OnCloseBthTouchUp(self, args):
        """关闭UI界面"""
        # 延迟 0.1s 关闭界面
        workbenchClientSystem = clientApi.GetSystem(modConfig.ADDON_NAME, modConfig.WORKBENCH_CLIENT_NAME)
        eventData = workbenchClientSystem.CreateEventData()
        eventData['playerId'] = playerId
        eventData['position'] = self.position
        eventData['dimensionId'] = self.dimensionId
        eventData['blockType'] = self.blockType
        eventData['blockName'] = self.blockName
        workbenchClientSystem.BroadcastEvent(WorkbenchBlockUICloseClientEvent, eventData)