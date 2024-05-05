import mod.client.extraClientApi as clientApi
from mod.client.plugin.illustratedBook.comp.preset.imageComp import ImageComp

bookManager = clientApi.GetBookManager()
bookConfig = bookManager.GetBookConfig()
ImageComp = bookManager.GetImageCompCls()

class ArrowImgComp(ImageComp):
    def __init__(self, imageResizeRule = bookConfig.ImageReszieRule.Ninesliced):
        ImageComp.__init__(self, imageResizeRule)

    def AlignPosition(self, pos):
        self.SetSize((16, 13))
        self.SetAlpha(0.5)
        self.AlignLeftToX(pos[0]).AlignTopToY(pos[1])
        return self
    
    def SetDataBeforeShow(self):
        return ImageComp.SetDataBeforeShow(self, 'textures/ui/arrow')