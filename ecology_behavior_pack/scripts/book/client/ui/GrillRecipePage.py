from scripts.book.client.ui.base import BaseRecipePage

class GrillRecipePage(BaseRecipePage):
    def __init__(self, size=None, position=None):
        # type: (tuple[int, int] | None, tuple[int, int] | None) -> None
        BaseRecipePage.__init__(self, 'ham:grill', size, position)
        self._offsetDict = {
            'material': ((0,0),),
            'result': ((72,0),)
        }
        self._arrowOffset = (36,0)
        self._contentOffset = 20
