import mod.client.extraClientApi as clientApi

from scripts.common.modConfig import __DEV__
from scripts.common.entity import Effect
from scripts.common.enum import BiomeTag, EffectType
from scripts.common.enum.Item import ItemCategory, ItemQuality, ItemSource, ItemTag
from scripts.common.error import AddonDataError
from scripts.book.client.ui.base import BaseTextPage
from scripts.common import logger
from scripts.common.entity import Item, GetItem

levelId = clientApi.GetLevelId()
engineCompFactory = clientApi.GetEngineCompFactory()
gameComp = engineCompFactory.CreateGame(levelId)
bookManager = clientApi.GetBookManager()
HighlightComp = bookManager.GetHighlightCompCls()

class ItemInfoPage(BaseTextPage):
    def __init__(self, size=None, position=None):
        # type: (tuple[int, int] | None, tuple[int, int] | None) -> None
        """
        物品信息页，传入物品名称即可
        """
        BaseTextPage.__init__(self, size, position) # type: ignore
        self._itemComp = HighlightComp()
        self.AddComps(self._itemComp)

    def _SetDataBeforeShow(self):
        itemName = self.data.get('itemName') # type: str
        self._itemName = itemName
        self._item = GetItem(itemName) # type: Item # type: ignore
        if not self._item:
            raise AddonDataError('不存在作物数据{}，这是一个程序BUG'.format(itemName))
        
        self._itemComp.SetDataBeforeShow([{"item": itemName, "data": 0}]) # type: ignore
        BaseTextPage._SetDataBeforeShow(self)

    def _SetPositionAfterShow(self):
        BaseTextPage._SetPositionAfterShow(self)
        self._itemComp.SetSize((30, 30)).SetPosition((self.Left() + 40, 45))
        self._content.SetPosition((self.Left(), 80))

    def _GetContent(self):
        """❗️根据物品信息"""
        basic = self.__GetContentOfBasic()
        food = self.__GetContentOfFood()
        source = self.__GetContentOfSource()
        return basic + food + source
        
    def __GetContentOfBasic(self):
        quality = self._item.GetQuality()
        qualityInfo = '品质: {0} ({1}{2}§r)\n'.format('' * quality, ItemQuality.GetFormatColor(quality), ItemQuality.GetChinese(quality))

        # category = ItemCategory.GetChinese(self._item.GetCategory())
        # categoryInfo = '类别: {0}\n'.format(category)

        tags = (ItemTag.GetChinese(tag) for tag in self._item.GetTags())
        tagInfo = '标签: {0}\n'.format('、'.join(tags))

        return qualityInfo + tagInfo
    
    def __GetContentOfSource(self):
        cnFuncDict = {
            ItemSource.BLOCK: self.__GetItemOrBlockCn,
            ItemSource.WORKBENCH: self.__GetItemOrBlockCn,
            ItemSource.WILD: BiomeTag.GetChinese,
            ItemSource.CROP: self.__GetItemOrBlockCn,
        }

        sourceText = ''
        source = self._item.GetSource()
        if source is None:
            return ''
        for (sourceType, sources) in source.items():
            sourceText += "{}: ".format(ItemSource.GetChinese(sourceType))
            cnFunc = cnFuncDict.get(sourceType, self.__GetItemOrBlockCn)
            cnDict = [cnFunc(item) for item in sources]
            sourceText += '、'.join(cnDict)
            sourceText += '\n'
        return sourceText
    
    def __GetContentOfFood(self):
        levelList = ['Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ']
        food = self._item.GetFood()
        foodText = ''
        if food:
            nutrition = food.GetNutrition() if __DEV__ else food.GetEatNutrition()
            if food.CanEat and nutrition != 0:
                foodText += '饥饿:  X {0}\n'.format(nutrition)
            effects = food.GetEffects() or []
            for index, effect in enumerate(effects):
                foodText += '效果: ' if index == 0 else '      '
                foodText += effect.GetChinese() + levelList[effect.GetAmplifier()] + ' ' + str(effect.GetDuration()) + 's\n'
        hiddenEffect = self._item.GetHiddenEffects()
        if hiddenEffect:
            cnEffects = [EffectType.GetChinese(effect) for effect in hiddenEffect]
            foodText += '隐藏: {0}\n'.format('、'.join(cnEffects))
        return foodText
    
    def __GetItemOrBlockCn(self, itemOrBlock):
        # (str) -> str
        blockName = gameComp.GetChinese('tile.' + itemOrBlock + '.name')
        itemName = gameComp.GetChinese('item.' + itemOrBlock + '.name')
        return itemName if blockName.find('tile') == 0 else blockName