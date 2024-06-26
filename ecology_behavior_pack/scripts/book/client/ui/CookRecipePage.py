from scripts.book.client.ui.base import BaseRecipePage

class CookRecipePage(BaseRecipePage):
    def __init__(self, size=None, position=None):
        # type: (tuple[int, int] | None, tuple[int, int] | None) -> None
        BaseRecipePage.__init__(self, 'ham:cooking_table', size, position)
        self._offsetDict = {
            'material': (
                (0,8), (16,8), (32,8), 
                (0,24), (16,24), (32,24), 
                (0,40), (16,40), (32,40)
            ),
            'fixed_material': ((92,0), (92,16), (92,32), (92,48)),
            'result': ((72,24),)
        }
        self._arrowOffset = (52,24)
        self._contentOffset = 70
