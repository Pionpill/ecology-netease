import mod.client.extraClientApi as clientApi

from scripts.common import logger
from scripts.common.entity import Crop, Land
from scripts.common.error import AddonDataError

bookManager = clientApi.GetBookManager()
bookConfig = bookManager.GetBookConfig()
TextComp = bookManager.GetTextCompCls()
TitlePage = bookManager.GetTitlePageCls()
HighlightComp = bookManager.GetHighlightCompCls()

class CropGrowPage(TitlePage):
    def __init__(self, size=None, position=None):
        # type: (tuple[int, int] | None, tuple[int, int] | None) -> None
        """
        抽象作物页，传入作物 key 即可
        """
        TitlePage.__init__(self, size, position) # type: ignore
        self.__InitComp()
        self.__fruitIndex = 1

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

    def __InitComp(self):
        """初始化组件"""
        self._seedHighlightComp = HighlightComp()    # 种子轮播
        self._seedText = TextComp()
        self._fruitHighlightComp1 = HighlightComp()   # 果实轮播
        self._fruitHighlightComp2 = HighlightComp()
        self._fruitHighlightComp3 = HighlightComp()
        self._fruitHighlightComp4 = HighlightComp()
        self._fruitText = TextComp()
        self._landHighlightComp1 = HighlightComp()   # 土地轮播
        self._landHighlightComp2 = HighlightComp()
        self._landHighlightComp3 = HighlightComp()
        self._landHighlightComp4 = HighlightComp()
        self._landText = TextComp()
        self._cropHighlightComp = HighlightComp()   # 作物轮播
        self._cropText = TextComp() 
        self.AddComps(self._seedHighlightComp, self._fruitHighlightComp1, self._fruitHighlightComp2, self._fruitHighlightComp3, self._fruitHighlightComp4, self._cropHighlightComp, self._seedText, self._fruitText, self._cropText, self._landHighlightComp1, self._landHighlightComp2, self._landHighlightComp3, self._landHighlightComp4, self._landText)

    def __SetDataBeforeShow(self):
        """数据与UI绑定"""
        if not self.data:
            raise AddonDataError('页面不存在数据，这是一个程序BUG')
        
        self.SetTitleData()
        seedKey = self.data.get('seedKey')
        self._crop = Crop.FromSeedKey(seedKey)
        if not self._crop:
            raise AddonDataError('不存在作物数据{}，这是一个程序BUG'.format(seedKey))

        self._seedText.SetDataBeforeShow('种子:', bookConfig.TextSize.content)
        seedName = self._crop.GetSeedName()
        seedData = [{"item": seedName, "data": 0}]
        self._seedHighlightComp.SetDataBeforeShow(seedData) # type: ignore

        loots = self._crop.GetLoots()
        if not loots:   # 理论上不可能走到这里
            raise AddonDataError('不存在作物凋落物{}，这是一个程序BUG'.format(seedKey))
        self._cropText.SetDataBeforeShow('生长过程', bookConfig.TextSize.content)
        self.__fruitIndex = 0
        lootData = []
        for loot in loots:
            itemData = {"item": loot.itemName, "data": 0}
            comp = getattr(self, '_fruitHighlightComp' + str(self.__fruitIndex + 1))
            if self.__fruitIndex < 3:
                comp.SetDataBeforeShow([itemData])
                self.__fruitIndex += 1
                continue
            lootData.append(itemData)
            if loot == loots[-1]:
                comp.SetDataBeforeShow(lootData)

        self._fruitText.SetDataBeforeShow('收获:', bookConfig.TextSize.content)
        cropData = [{"item": seedKey + '_stage_' + str(x), "data": 0} for x in range(self._crop.GetGrowStageLength())]
        self._cropHighlightComp.SetDataBeforeShow(cropData) # type: ignore

        self._landText.SetDataBeforeShow('土地:', bookConfig.TextSize.content)
        landTypeList = self._crop.GetGrowLandType()
        self.__landIndex = 0
        for landType in landTypeList:
            comp = getattr(self, '_landHighlightComp' + str(self.__landIndex + 1))
            landData = []
            for landName in Land.GetBlocksByTag(landType):
                land = Land.FromBlockName(landName)
                if land is None:
                    continue
                if land.GetFertility() >= self._crop.GetGrowFertilityMin():
                    landData.append({"item": landName, "data": 0})
            if len(landData) > 0:
                self.__landIndex += 1
            comp.SetDataBeforeShow(landData)

    def __SetShowPosition(self):
        contentTop = self.LayoutTitle()
        self._seedText.SetPosition((20, contentTop + 5))
        self._seedHighlightComp.SetSize((15, 15)).SetPosition((45, 42))

        self._fruitText.SetPosition((20, contentTop + 25))
        for i in range(self.__fruitIndex):
            comp = getattr(self, '_fruitHighlightComp' + str(i + 1))
            comp.SetSize((15, 15)).SetPosition((45 + i * 20, 63))
        for i in range(self.__fruitIndex, 4):
            comp = getattr(self, '_fruitHighlightComp' + str(i + 1))
            comp.Hide()

        self._landText.SetPosition((20, contentTop + 45))
        for i in range(self.__landIndex):
            comp = getattr(self, '_landHighlightComp' + str(i + 1))
            comp.SetSize((15, 15)).SetPosition((45 + i * 20, 83))
        for i in range(self.__landIndex, 4):
            comp = getattr(self, '_landHighlightComp' + str(i + 1))
            comp.Hide()

        self._cropHighlightComp.SetSize((60, 60))
        self._cropHighlightComp.SetPosition((40, 105))
        self._cropText.SetPosition((55, 170))