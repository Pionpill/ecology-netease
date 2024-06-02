import mod.client.extraClientApi as clientApi

from scripts.book.common.events import BookFirstInitEvent
from scripts.book.client.ui import BakeRecipePage, CookRecipePage, FryerRecipePage, GrillRecipePage, MillRecipePage, PanRecipePage, SqueezerRecipePage, SteamerRecipePage, StewRecipePage, CropGrowPage
from scripts.common import logger

ClientSystem = clientApi.GetClientSystemCls()
bookManager = clientApi.GetBookManager()
levelId = clientApi.GetLevelId()
playerId = clientApi.GetLocalPlayerId()
compFactory = clientApi.GetEngineCompFactory()
configComp = compFactory.CreateConfigClient(levelId)

class BookClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        bookManager.AddPageType("ham:bakeRecipePage", BakeRecipePage)
        bookManager.AddPageType("ham:cookRecipePage", CookRecipePage)
        bookManager.AddPageType("ham:fryerRecipePage", FryerRecipePage)
        bookManager.AddPageType("ham:grillRecipePage", GrillRecipePage)
        bookManager.AddPageType("ham:millRecipePage", MillRecipePage)
        bookManager.AddPageType("ham:panRecipePage", PanRecipePage)
        bookManager.AddPageType("ham:squeezerRecipePage", SqueezerRecipePage)
        bookManager.AddPageType("ham:steamerRecipePage", SteamerRecipePage)
        bookManager.AddPageType("ham:stewRecipePage", StewRecipePage)
        bookManager.AddPageType("ham:cropGrowPage", CropGrowPage)
        self.ListenEvents()

    def ListenEvents(self):
        engineNamespace = clientApi.GetEngineNamespace()
        engineSystemName = clientApi.GetEngineSystemName()
        self.ListenForEvent(engineNamespace, engineSystemName,
                            "LoadClientAddonScriptsAfter", self,
                            self.OnClientLoadAddonsFinish)
        
    def OnClientLoadAddonsFinish(self, _):
        ecologyLocalData = configComp.GetConfigData("ham:ecology")
        if ecologyLocalData.get('book') is None:
            ecologyLocalData['book'] = True
            args = self.CreateEventData()
            args['playerId'] = playerId
            self.NotifyToServer(BookFirstInitEvent, args)
            configComp.SetConfigData("ham:ecology", ecologyLocalData)