import mod.client.extraClientApi as clientApi

from scripts.book.client.ui import BakeRecipePage, CookRecipePage, FryerRecipePage, GrillRecipePage, MillRecipePage, PanRecipePage, SqueezerRecipePage, SteamerRecipePage, StewRecipePage

ClientSystem = clientApi.GetClientSystemCls()
bookManager = clientApi.GetBookManager()

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