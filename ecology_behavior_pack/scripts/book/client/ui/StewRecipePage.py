from scripts.book.client.ui.base import BaseRecipePage

class StewRecipePage(BaseRecipePage):
    def __init__(self, size=None, position=None):
        # type: (tuple[int, int] | None, tuple[int, int] | None) -> None
        BaseRecipePage.__init__(self, 'ham:stew_pot', size, position)
        self._offsetDict = {
            'material': (
                (0,0), (16,0), (32,0), 
                (0,16), (16,16), (32,16)
            ),
            'result': ((72,8),)
        }
        self._arrowOffset = (52,8)
        self._contentOffset = 40
