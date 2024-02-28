import mod.server.extraServerApi as serverApi
from scripts.workbench.server.data.fuel import FUEL_DATA
from scripts.common.utils import itemUtils
from scripts.common import logger
from scripts.workbench.server.manager.base import BaseWorkbenchManager

compFactory = serverApi.GetEngineCompFactory()
levelId = serverApi.GetLevelId()
itemComp = compFactory.CreateItem(levelId)

class FurnaceManager(BaseWorkbenchManager):
    def __init__(self, blockName, position, dimensionId):
        # type: (str, tuple[int, int, int], int) -> None
        BaseWorkbenchManager.__init__(self, blockName, position, dimensionId)
        self.fuels = self.__GetFuels(blockName)
        self.burnInterval = 5 * 20
        self.burnTime = 0  # 剩余可燃烧时间，单位 tick
        self.burnDuration = 0  # 可燃烧总时间，单位 tick
        self.produceProgress = 0

    def Tick(self):
        # type: () -> None
        shouldRefresh = False
        lastBurn = self.__IsBurning()
        # 更新燃烧进度
        if self.__IsBurning():
            self.burnTime -=1
        elif self.__CanBurn():
            shouldRefresh = self.Burn()
        # 更新生产进度
        if self.__IsBurning() and self.__CanProduce():
            self.produceProgress += 1
            if self.produceProgress == self.burnInterval:
                self.Consume()
                self.produceProgress = 0
                shouldRefresh = True
        elif self.produceProgress > 0:
            shouldRefresh = True
            self.produceProgress = 0
        # 燃料耗完
        if lastBurn != self.__IsBurning():
            shouldRefresh = True
        return shouldRefresh

    def __IsBurning(self):
        """判断是否处于燃烧状态"""
        return self.burnTime > 0

    def __CanProduce(self):
        """判断是否可以继续生产"""
        # 是否存在原材料
        materialItems = self.GetAllSlotData('material')
        if all(item is None for item in materialItems.values()):
            return False
        return self.__CanAddResultItems()

    def __CanBurn(self):
        # type: () -> bool
        """燃料耗尽后是否继续燃烧"""
        # 是否存在燃料
        fuelItems = self.GetAllSlotData('fuel')
        if all(item is None or (item.get('newItemName') not in self.fuels.keys()) for item in fuelItems.values()):
            return False
        # 是否仍在烧制物品中
        if self.burnTime != 0:
            return False
        # 是否存在原材料
        materialItems = self.GetAllSlotData('material')
        if all(item is None for item in materialItems.values()):
            return False
        # 有匹配的配方
        return self.__CanAddResultItems()

    def __CanAddResultItems(self):
        """原材料是否可以匹配结果"""
        matchResultItems = self.GetRecipeResultSlotItemDict()
        resultItems = self.GetAllSlotData('result')
        for slotName, resultItem in resultItems.items():
            matchResultItem = matchResultItems.get(slotName)
            if resultItem is None:
                continue
            if not itemUtils.IsSameItem(resultItem, matchResultItem):
                return False
            maxStackSize = itemComp.GetItemBasicInfo(resultItem["newItemName"], resultItem["newAuxValue"]).get("maxStackSize")
            if matchResultItem.get('count') + resultItem.get('count') > maxStackSize:
                return False
        return True

    def Burn(self):
        """燃烧原材料"""
        # type: () -> bool
        # 目前所有的工作台只有一个燃料槽
        # TODO 后续增强为多个燃料槽轮流燃烧
        fuelItemDict = self.GetAllSlotData('fuel').get('fuel_slot0')
        if not fuelItemDict:
            return False
        fuelName = fuelItemDict.get('newItemName')
        burnDuration = self.fuels.get(fuelName)
        if burnDuration:
            self._ItemReduce('fuel_slot0')
            self.burnDuration = burnDuration * 20
            self.burnTime = burnDuration * 20
            return True
        return False

    def Consume(self):
        """熔炉烧制物品"""
        materialSlotItemDict = self.proxy.matchedRecipeMaterial
        if materialSlotItemDict is None:
            return
        for slotName, itemDict in materialSlotItemDict.items():
            if itemDict is None:
                continue
            count = itemDict.get("count")
            self._ItemReduce(slotName, count)
        matchedRecipeResult = self.proxy.matchedRecipeResult
        resultItems = self.GetAllSlotData('result')
        for slotName, recipeResultItem in matchedRecipeResult.items():
            resultItem = resultItems.get(slotName)
            if resultItem is None:
                self._SetItem(slotName, recipeResultItem)
            else:
                recipeResultItem['count'] = recipeResultItem.get('count') + resultItem.get('count')
                self._SetItem(slotName, recipeResultItem)

    def GetRecipeResultSlotItemDict(self):
        """获取匹配的物品"""
        materialSlotItemDict = self.GetAllSlotData('material')
        if len(materialSlotItemDict) == 0 or all(value is None for value in materialSlotItemDict.values()):
            return {'material_slot' + str(i): None for i in range(self.slotNum['result'])}
        return self.proxy.MatchRecipe(materialSlotItemDict)
    
    def GetBurnData(self):
        return {
            'burnDuration': self.burnDuration,
            'burnProgress': int((self.burnDuration - self.burnTime) * 3 / 2),
            'isBurning': self.burnTime > 0,
            'isProducing': self.burnTime > 0 and self.__CanProduce(),
            'produceProgress': int(self.produceProgress * 3 / 2),
        }

    def Reset(self, playerId):
        pass

    def __GetFuels(self, blockName):
        if blockName in ["ham:mill"]:
            return FUEL_DATA.get('gold')
        else:
            return FUEL_DATA.get('coal')