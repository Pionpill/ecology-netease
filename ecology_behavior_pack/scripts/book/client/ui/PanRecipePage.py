from scripts.book.client.ui.base import BaseRecipePage

class PanRecipePage(BaseRecipePage):
    def __init__(self, size=None, position=None):
        # type: (tuple[int, int] | None, tuple[int, int] | None) -> None
        BaseRecipePage.__init__(self, 'ham:pan', size, position)
        self._offsetDict = {
            'material': (
                (0,16), (16,16), (32,16), 
                (0,32), (16,32), (32,32), 
            ),
            'fixed_material': ((92,0), (92,16), (92,32), (92,48)),
            'result': ((72,24),)
        }
        self._arrowOffset = (52,24)
        self._contentOffset = 70
