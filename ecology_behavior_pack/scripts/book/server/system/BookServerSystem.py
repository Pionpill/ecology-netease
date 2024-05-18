import mod.server.extraServerApi as serverApi

from scripts.book.common.events import BookFirstInitEvent
from scripts.common import logger, modConfig
from scripts.common.utils import itemUtils

ServerSystem = serverApi.GetServerSystemCls()
compFactory = serverApi.GetEngineCompFactory()
levelId = serverApi.GetLevelId()
itemComp = compFactory.CreateItem(levelId)

class BookServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        self.ListenEvents()

    def ListenEvents(self):
        self.ListenForEvent(modConfig.ADDON_NAME, modConfig.BOOK_CLIENT_NAME, BookFirstInitEvent, self, self.OnFirstInit)

    def OnFirstInit(self, args):
        # 将三本书给玩家
        itemNameList = (
            "ham:guide_book",
            "ham:crop_book",
            "ham:cooking_book",
        )
        for itemName in itemNameList:
            itemDict = itemUtils.GetItemDict(itemName)
            itemComp.SpawnItemToPlayerInv(itemDict, args['playerId'])