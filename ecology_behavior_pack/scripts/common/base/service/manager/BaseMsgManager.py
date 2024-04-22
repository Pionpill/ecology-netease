import mod.server.extraServerApi as serverApi

from scripts.common.base.service.manager.enum import MsgColor

engineCompFactory = serverApi.GetEngineCompFactory()

class BaseMsgManager(object):
    """基础消息类型"""

    def __init__(self, playerId):
        # type: (str) -> None
        self.playerId = playerId
        self.msgComp = engineCompFactory.CreateMsg(playerId)

    def _NotifyOneMessage(self, msg, color):
        # type: (str, str) -> None
        self.msgComp.NotifyOneMessage(self.playerId, msg, color)
    
    def _NotifyOneCriticalMessage(self, msg):
        # type: (str) -> None
        self._NotifyOneMessage(msg, MsgColor.CRITICAL)

    def _NotifyOneErrorMessage(self, msg):
        # type: (str) -> None
        self._NotifyOneMessage(msg, MsgColor.ERROR)

    def _NotifyOneWarningMessage(self, msg):
        # type: (str) -> None
        self._NotifyOneMessage(msg, MsgColor.WARNING)
    
    def _NotifyOneInfoMessage(self, msg):
        # type: (str) -> None
        self._NotifyOneMessage(msg, MsgColor.INFO)

    def _NotifyOneDebugMessage(self, msg):
        # type: (str) -> None
        self._NotifyOneMessage(msg, MsgColor.DEBUG)