import math
import mod.client.extraClientApi as clientApi
from mod.client.plugin.illustratedBook.comp.baseComp import BaseComp
from mod.client.ui.controls.baseUIControl import BaseUIControl

from scripts.common import logger

bookManager = clientApi.GetBookManager()
bookConfig = bookManager.GetBookConfig()
ImageComp = bookManager.GetImageCompCls()
TextComp = bookManager.GetTextCompCls()
HighlightComp = bookManager.GetHighlightCompCls()

class SlotComp(BaseComp):
    """基于 ImageComp 和 HighlightComp 封装的合成台槽组件"""
    def __init__(self):
        # type: () -> None
        object.__init__(self)
        self.__bgImg = ImageComp()
        self.__items = HighlightComp()
        self.__count = TextComp(bookConfig.TextAlign.Right)

    def __iter__(self):
        return iter((self.__bgImg, self.__items, self.__count))

    def Show(self):
        self.__bgImg.Show()
        self.__count.Show()
        self.__items.Show()
        return self
    
    def ShowItem(self):
        self.__items.Show()
        return self

    def Hide(self):
        self.__bgImg.Hide()
        self.__items.Hide()
        self.__count.Hide()
        return self
    
    def HideItem(self):
        self.__items.Hide()
        return self

    def Reset(self):
        self.__bgImg.Reset()
        self.__items.Reset()
        self.__count.Reset()
        return self

    def GetPosition(self):    
        return self.__items.GetPosition()
    
    def SetPosition(self, newPosition):    
        return self.__items.SetPosition(newPosition)

    def AlignPosition(self, pos):    
        self._InitAllSize()
        self._InitDefaultStyle()
        self._SetDefaultLayer()
        self.__items.AlignLeftToX(pos[0]).AlignTopToY(pos[1])
        self._ResetRelativePosition()
        return self

    def _InitAllSize(self):
        self.__bgImg.SetSize((16, 16))
        self.__items.SetSize((16, 16))
        self.__count.SetSize((10, 9))

    def _InitDefaultStyle(self):
        self.SetColor((1.0,1.0,1.0,1.0))

    def _ResetRelativePosition(self):
        center = self.__items.Center()
        size = self.__items.GetSize()
        countX = center[0] + math.floor(size[0]/2)
        countY = center[1] + math.floor(size[1]/2)
        self.__bgImg.AlignCenterToX(center[0])
        self.__bgImg.AlignCenterToY(center[1])
        self.__count.AlignRightToX(countX)
        self.__count.AlignBottomToY(countY + 1)

    def _SetDefaultLayer(self):
        # type: () -> BaseComp
        self.SetLayer(7)
        return self

    def GetSize(self):
        return self.__items.GetSize()

    def SetSize(self, newSize):
        # type: (tuple[int,int]) -> BaseComp
        self.__items.SetSize(newSize)
        self.__bgImg.SetSize(newSize)
        return self
    
    def Center(self):
        return self.__items.Center()

    def Left(self):
        return self.__items.Left()

    def Right(self):
        return self.__items.Right()
    
    def Top(self):
        return self.__items.Top()
    
    def Bottom(self):
        return self.__items.Bottom()

    def MoveToX(self, x):
        # type: (int) -> BaseComp
        self.__items.MoveToX(x) 
        return self

    def MoveToY(self, y):
        # type: (int) -> BaseComp
        self.__items.MoveToX(y)  
        return self

    def MoveX(self, x):
        # type: (int) -> BaseComp
        self.__items.MoveX(x)    
        return self

    def MoveY(self, y):
        # type: (int) -> BaseComp
        self.__items.MoveY(y)      
        return self

    def AlignCenterToX(self, x):
        # type: (int) -> BaseComp
        self.__items.AlignCenterToX(x)  
        return self

    def AlignCenterToY(self, y):
        # type: (int) -> BaseComp
        self.__items.AlignCenterToY(y)    
        return self

    def AlignCenterToPosition(self, position):
        # type: (tuple[int, int]) -> BaseComp
        self.__items.AlignCenterToPosition(position)
        return self

    def AlignLeftToX(self, x):
        # type: (int) -> BaseComp
        self.__items.AlignLeftToX(x)      
        return self

    def AlignRightToX(self, x):
        # type: (int) -> BaseComp
        self.__items.AlignRightToX(x)      
        return self

    def AlignTopToY(self, y):
        # type: (int) -> BaseComp
        self.__items.AlignTopToY(y)      
        return self

    def AlignBottomToY(self, y):
        # type: (int) -> BaseComp
        self.__items.AlignBottomToY(y)    
        return self

    def GetRootUINode(self):
        return self.__items.GetRootUINode()    

    def HasRootUINode(self):
        # type: () -> bool
        return self.__items.HasRootUINode()    
    
    def SetNodeOffset(self, node, offset):
        # type: (BaseUIControl, tuple[int, int]) -> BaseComp
        self.__items.SetNodeOffset(node, offset)
        return self
    
    def SetNodeSize(self, node, newSize):
        # type: (BaseUIControl, tuple[int, int]) -> BaseComp
        self.__items.SetNodeSize(node, newSize)
        return self
    
    def SetNodeText(self, node, text):
        # type: (BaseUIControl, str) -> BaseComp
        self.__items.SetNodeText(node, text)
        return self

    def SetNodeTextFontSize(self, node, originFontSize, newFontSize):
        # type: (BaseUIControl, int, int) -> BaseComp
        self.__items.SetNodeTextFontSize(node, originFontSize, newFontSize)
        return self
    
    def GetNodeCenterGlobal(self, node):
        # type: (BaseUIControl) -> tuple[int, int]
        return self.__items.GetNodeCenterGlobal(node)
    
    def SetLayer(self, layer):
        # type: (int) -> BaseComp
        self.__bgImg.SetLayer(layer)
        self.__items.SetLayer(layer + 1)
        self.__count.SetLayer(layer + 10)
        return self
    
    def Call(self, callbackDict):
        # type: (dict) -> object
        return self.__items.Call(callbackDict)
    
    def GetPage(self):
        return self.__items.GetPage()

    def SetBgAlpha(self, alpha):
        return self.__bgImg.SetAlpha(alpha)
    
    def SetCountAlpha(self, alpha):
        return self.__count.SetAlpha(alpha)
    
    def SetColor(self, color):
        return self.__count.SetColor(color)

    def SetDataBeforeShow(self, itemData, count):
        self.__bgImg.SetDataBeforeShow('textures/ui/item_cell')
        self.__items.SetDataBeforeShow(itemData)
        self.__count.SetDataBeforeShow(str(count), 7)
