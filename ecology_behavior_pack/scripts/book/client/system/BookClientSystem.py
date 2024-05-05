import mod.client.extraClientApi as clientApi

from scripts.book.client.ui import CookRecipePage
from scripts.common import logger

ClientSystem = clientApi.GetClientSystemCls()
bookManager = clientApi.GetBookManager()

class BookClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        bookManager.AddPageType("ham:cookRecipePage", CookRecipePage)