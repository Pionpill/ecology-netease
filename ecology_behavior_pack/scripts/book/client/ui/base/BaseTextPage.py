import mod.client.extraClientApi as clientApi

from scripts.common import logger
from scripts.common.error import AddonDataError

bookManager = clientApi.GetBookManager()
bookConfig = bookManager.GetBookConfig()
TextComp = bookManager.GetTextCompCls()
TitlePage = bookManager.GetTitlePageCls()
HighlightComp = bookManager.GetHighlightCompCls()

class BaseTextPage(TitlePage):
    def __init__(self, size=None, position=None):
        # type: (tuple[int, int] | None, tuple[int, int] | None) -> None
        """
        抽象作物页，传入作物 key 即可
        """
        TitlePage.__init__(self, size, position) # type: ignore
        self._content = TextComp()
        self.AddComps(self._content)

    def SetData(self, data):
        self.data = data
        return self
    
    def Show(self):
        try:
            if not self.data:
                raise AddonDataError('页面不存在数据，这是一个程序BUG')
            self._SetDataBeforeShow()
            TitlePage.Show(self)
            self._SetPositionAfterShow()
        except AddonDataError as e:
            logger.error(e)

    def _SetDataBeforeShow(self):
        self.SetTitleData()
        self._content.SetDataBeforeShow(self._GetContent(), bookConfig.TextSize.content)

    def _SetPositionAfterShow(self):
        self.ResetCompsPosition()   
        contentTop = self.LayoutTitle()
        self._content.SetSize((self.GetSize()[0], 160)).SetPosition((20, contentTop + 5)).AlignLeftToX(self.Left()).AlignTopToY(contentTop + 5)

    def _GetContent(self):
        # 子类重载
        return ""