import math
import mod.client.extraClientApi as clientApi

from scripts.common import logger
from scripts.common.enum import Period, LandTag
from scripts.common.entity import Crop, GetCrop
from scripts.common.error import AddonDataError

bookManager = clientApi.GetBookManager()
bookConfig = bookManager.GetBookConfig()
TextComp = bookManager.GetTextCompCls()
TitlePage = bookManager.GetTitlePageCls()
HighlightComp = bookManager.GetHighlightCompCls()

class CropInfoPage(TitlePage):
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
        self._content.SetDataBeforeShow(self.__GetContent(), bookConfig.TextSize.content)

    def __GetContent(self):
        """❗️根据数据获取描述"""
        seedKey = self.data.get('seedKey')
        self._crop = GetCrop(seedKey) # type: Crop # type: ignore
        if not self._crop:
            raise AddonDataError('不存在作物数据{}，这是一个程序BUG'.format(seedKey))
        
        content = self.__GetContentOfDay()
        content += self.__GetContentOfRange('temperature')
        content += self.__GetContentOfRange('rainfall')
        content += self.__GetContentOfRange('bright')
        content += self.__GetContentOfLand()
        content += self.__GetContentOfWeather()
        return content

    def __GetContentOfDay(self):
        period = self._crop.GetGrowPeriod()
        tickPerDay = 24
        if period in [Period.DAY, Period.NIGHT]:
            tickPerDay = 12
        elif period in [Period.SUN, Period.MOON]:
            tickPerDay = 14

        growStageTuple = self._crop.GetGrowStageTuple()
        tickSum = sum(x.tick or 0 for x in growStageTuple)
        growDay = tickSum / tickPerDay
        minGrowDay, maxGrowDay = int(math.floor(growDay)), int(math.ceil(growDay))
        growContent = str(minGrowDay) if minGrowDay == maxGrowDay else '{0}-{1}'.format(minGrowDay, maxGrowDay)

        regrowDay = 0
        returnStage = self._crop.GetGrowHarvestReturn()
        if returnStage >= 0:
            regrowTickSum = sum(x.tick or 0 for x in growStageTuple[returnStage:])
            regrowDay = round(regrowTickSum / tickPerDay, 0)
        
        periodInfo  = Period.GetChinese(period)

        harvestCount = self._crop.GetGrowHarvestCount()
        harvestCountInfo = '收获·§8次数§r: {0}\n'.format(harvestCount) if harvestCount > 1 else ''

        return '生长·§8最佳§r: §r{0}天{1}({2})\n'.format(growContent, '+' + str(regrowDay) + '天' if regrowDay != 0 else '', periodInfo) + harvestCountInfo

    def __GetContentOfRange(self, type):
        # type: (str) -> str
        typeDict = {
            'temperature': {
                'cn': '温度',
                'rangeFunc': self._crop.GetGrowTemperature,
                'symbol': '℃',
            },
            'rainfall': {
                'cn': '湿度',
                'rangeFunc': self._crop.GetGrowRainfall,
                'symbol': '％',
            },
            'bright': {
                'cn': '光照',
                'rangeFunc': self._crop.GetGrowBrightness,
                'symbol': ''
            }
        }
        name = typeDict[type]['cn']
        getRangeFunc = typeDict[type]['rangeFunc']
        suitTuple = getRangeFunc('suit')
        canTuple = getRangeFunc('can')
        symbol = typeDict[type]['symbol']
        suitText = '{0}·§8适宜§r: {1}{3}—{2}{3}\n'.format(name, suitTuple[0], suitTuple[1], symbol)
        canText = '{0}·§8可行§r: {1}{3}—{2}{3}\n'.format(name, canTuple[0], canTuple[1], symbol)
        return suitText + canText

    def __GetContentOfLand(self):
        min = self._crop.GetGrowFertilityMin()
        sensitivity = self._crop.GetGrowFertilitySensitivity()
        type = LandTag.GetChinese(self._crop.GetGrowLandType())
        return '土壤·§8类型§r: {0}\n土壤·§8基础§r: {1}\n土壤·§8敏感§r: {2}\n'.format(type, min, sensitivity)

    def __GetContentOfWeather(self):
        rainMulti = self._crop.GetGrowRainMultiply() * 100
        return '降雨·§8加速§r: {0}％\n'.format(int(rainMulti)) if rainMulti != 100 else ''

    def __SetShowPosition(self):
        contentTop = self.LayoutTitle()
        self._content.SetSize((self.GetSize()[0], 160)).SetPosition((20, contentTop + 5)).AlignLeftToX(self.Left()).AlignTopToY(contentTop + 5)