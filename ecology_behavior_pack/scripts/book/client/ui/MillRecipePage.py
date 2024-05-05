from scripts.book.client.ui.base import BaseRecipePage

class MillRecipePage(BaseRecipePage):
    def __init__(self, size=None, position=None):
        # type: (tuple[int, int] | None, tuple[int, int] | None) -> None
        BaseRecipePage.__init__(self, 'ham:mill', size, position)
        self._offsetDict = {
            'material': ((0,0),),
            'result': ((48,0),(64,0))
        }
        self._arrowOffset = (24,0)
        self._contentOffset = 20
