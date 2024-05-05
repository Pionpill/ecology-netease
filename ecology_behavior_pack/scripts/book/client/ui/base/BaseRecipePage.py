import mod.client.extraClientApi as clientApi

from scripts.book.client.ui.components import ArrowImgComp, SlotComp
from scripts.common import logger
from scripts.common.entity import GetRecipe
from scripts.common.error import AddonDataError
from scripts.common.utils import mathUtils

bookManager = clientApi.GetBookManager()
bookConfig = bookManager.GetBookConfig()
TitlePage = bookManager.GetTitlePageCls()
TextComp = bookManager.GetTextCompCls()

class BaseRecipePage(TitlePage):
    def __init__(self, blockName, size=None, position=None):
        # type: (str, tuple[int, int] | None, tuple[int, int] | None) -> None
        """
        抽象配方页，子类必须传入以下数据
        1. 传入 blockName
        2. 重新赋值 _offsetDict, _arrowOffset, _contentOffset
        """
        TitlePage.__init__(self, size, position) # type: ignore
        self._blockName = blockName

        recipe = GetRecipe(self._blockName)
        if recipe is None:
            return
        self._recipe = recipe

        self._slotDict = {}  # type: dict[str, SlotComp]
        self.__InitSlotComp()

        self.arrow = ArrowImgComp()
        self.content = TextComp(bookConfig.TextAlign.Left)    
        self.AddComps(self.arrow, self.content)

        self.data = None
        self._offsetDict = {}   # type: dict[str, tuple]
        self._arrowOffset = (52,24)
        self._contentOffset = 70

    def __InitSlotComp(self):
        slotNumDict = self._recipe.GetSlotNum()
        for slotPrefix, slotNum in slotNumDict.items():
            if slotPrefix in ['liquid', 'fuel']:
                continue
            for i in range(slotNum):
                slotName = slotPrefix + '_slot' + str(i)
                setattr(self, slotName, SlotComp())
                slotComp = getattr(self, slotName)
                self._slotDict[slotName] = slotComp
                self.AddComps(slotComp)

    def SetData(self, data):
        self.data = data
        return self

    def Show(self):
        try:
            self.__SetDataBeforeShow()
            TitlePage.Show(self)
            self.ResetCompsPosition()   
            self.__SetShowPosition()
        except AddonDataError as e:
            logger.error(e)
    
    def __SetDataBeforeShow(self):
        """数据与UI绑定"""
        if not self.data:
            raise AddonDataError('页面不存在数据，这是一个程序BUG')

        self.SetTitleData()
        self.arrow.SetDataBeforeShow()
        self.content.SetDataBeforeShow(self.data.get('content'), bookConfig.TextSize.content)
        recipeId = self.data.get('recipeId')
        recipeSlotItems = self._recipe.GetFormatRecipe(recipeId)

        for key, slotComp in self._slotDict.items():
            itemDict = recipeSlotItems.get(key)
            itemData = [{"item": itemDict['newItemName'], "data": itemDict['newAuxValue']}] if itemDict else []
            count = (itemDict['count'] if itemDict['count'] > 1 else '') if itemDict else ''
            slotComp.SetDataBeforeShow(itemData, count)

    def __SetShowPosition(self):
        """UI定位"""
        contentTop = self.LayoutTitle()
        anchor = (self.Left(), contentTop + 8)

        for slotPrefix, offsetTuple in self._offsetDict.items():
            for i in range(len(offsetTuple)):
                slotName = slotPrefix + '_slot' + str(i)
                slotComp = getattr(self, slotName) # type: SlotComp
                slotComp.AlignPosition(mathUtils.addTuple(anchor, offsetTuple[i]))

        self.arrow.AlignPosition(mathUtils.addTuple(anchor, self._arrowOffset))
        pageSize = self.GetSize() 
        self.content.SetSize((pageSize[0], 100)).AlignLeftToX(anchor[0]).AlignTopToY(anchor[1] + self._contentOffset)