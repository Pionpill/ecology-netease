from scripts.book.client.ui.base import BaseRecipePage

class SqueezerRecipePage(BaseRecipePage):
    def __init__(self, size=None, position=None):
        # type: (tuple[int, int] | None, tuple[int, int] | None) -> None
        BaseRecipePage.__init__(self, 'ham:squeezer', size, position)
        self._offsetDict = {
            'material': ((0,0),(16,0),(32,0)),
            'result': ((92,0),)
        }
        self._arrowOffset = (62,0)
        self._contentOffset = 20
