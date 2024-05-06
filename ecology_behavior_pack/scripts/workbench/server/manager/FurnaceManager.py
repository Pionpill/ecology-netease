import copy
import mod.server.extraServerApi as serverApi

from scripts.common import logger
from scripts.common.data.workbench import FUEL_DATA
from scripts.common.utils import itemUtils
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
        # FIXME 需要持久化，否则重启游戏会刷新数据
        self.burnTime = 0  # 剩余可燃烧时间，单位 tick
        self.burnDuration = 0  # 可燃烧总时间，单位 tick
        self.produceProgress = 0
        self.shouldRefresh = False
        if self.slotNum['liquid'] != 0 and self.blockEntityData['liquid'] is None:
            self.blockEntityData['liquid'] = 0

    def GetSlotData(self, slotName):
        # type: (str) -> int
        """从方块实体中获取指定槽的物品"""
        return self.blockEntityData[slotName]   # type: ignore

    def Tick(self):
        # type: () -> bool
        self.__ProduceTick()
        self.__MeterTick()
        self.__ResultWareTick()
        return self.shouldRefresh
    
    def __ProduceTick(self):
        # type: () -> None
        """燃料燃烧与生产"""
        self.shouldRefresh = False
        lastBurn = self.__IsBurning()
        # 更新燃烧进度
        if self.__IsBurning():
            self.burnTime -=1
        elif self.__CanBurn():
            self.shouldRefresh = self._Burn()
        # 更新生产进度
        if self.__IsBurning() and self.__CanProduce():
            self.produceProgress += 1
            if self.produceProgress == self.burnInterval:
                self.Consume()
                self.Produce()
                self.produceProgress = 0
                self.shouldRefresh = True
        elif self.produceProgress > 0:
            self.shouldRefresh = True
            self.produceProgress = 0
        # 燃料耗完
        if lastBurn != self.__IsBurning():
            self.shouldRefresh = True

    def __MeterTick(self):
        """液体更新"""
        liquidMaterialDict = self.blockEntityData['liquid_slot0']
        if self.slotNum['liquid'] == 0 or liquidMaterialDict is None or self.blockEntityData['liquid'] == 20:
            return
        
        liquidCount = self.GetSlotData('liquid')
        if not isinstance(liquidCount, int):
            return
        if self.blockName == 'ham:fryer' and liquidMaterialDict['newItemName'] == 'ham:cooking_oil':
            # 油表更新
            if liquidMaterialDict['count'] + liquidCount <= 20:
                self._SetItem('liquid_slot0', None)
                self.blockEntityData['liquid'] = liquidCount + liquidMaterialDict['count']
            else:
                liquidMaterialDict['count'] = liquidMaterialDict['count'] + liquidCount - 20
                self._SetItem('liquid_slot0', liquidMaterialDict)
                self.blockEntityData['liquid'] = 20
            self.shouldRefresh = True
        if self.blockName in ['ham:food_steamer', 'ham:stew_pot'] and liquidMaterialDict['newItemName'] == 'minecraft:water_bucket' and self.blockEntityData['liquid_slot1'] is None and liquidCount <= 15:
            # 水表更新
            self.blockEntityData['liquid'] = liquidCount + 5
            self._SetItem('liquid_slot0', None)
            self._SetItem('liquid_slot1', itemUtils.GetItemDict('minecraft:bucket'))
            self.shouldRefresh = True

    def __ResultWareTick(self):
        resultWareItem = self.blockEntityData['result_ware_slot']
        wareItem = self.blockEntityData['ware_slot']
        if not self.resultWareCount or not resultWareItem or not wareItem:
            return
        resultItem = self.blockEntityData['result_slot0']

        maxStackSize = itemComp.GetItemBasicInfo(resultItem["newItemName"], resultItem["newAuxValue"]).get("maxStackSize") if resultItem else 64
        if resultItem and resultItem['count'] >= maxStackSize:
            return
        produceCount = min(wareItem['count'], resultWareItem['count'], maxStackSize - resultWareItem['count'])
        if resultItem:
            self.IncreaseItem('result_slot0', produceCount)
        else:
            realResultWareItem = copy.deepcopy(resultWareItem)
            realResultWareItem['count'] = produceCount
            self._SetItem('result_slot0', realResultWareItem)
        self.ReduceItem('result_ware_slot', produceCount)
        self.ReduceItem('ware_slot', produceCount)
        self.shouldRefresh = True

    def __IsBurning(self):
        """判断是否处于燃烧状态"""
        return self.burnTime > 0

    def __CanProduce(self):
        """判断是否可以继续生产"""
        # 是否存在原材料
        if self.slotNum['liquid'] != 0 and self.blockEntityData['liquid'] == 0:
            return False
        materialItems = self.GetAllSlotData('material')
        if all(item is None for item in materialItems.values()):
            return False
        return self.__CanAddResultItems()

    def __CanBurn(self):
        # type: () -> bool
        """燃料耗尽后是否继续燃烧"""
        # 是否存在燃料
        if self.slotNum['liquid'] != 0 and self.blockEntityData['liquid'] == 0:
            return False
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
        if all(item is None for item in matchResultItems.values()):
            return False
        # 如果使用容器结果槽，只有一个
        resultItems = self.GetAllSlotData('result_ware') if self.resultWareCount else self.GetAllSlotData('result')
        for slotName, resultItem in resultItems.items():
            matchResultItem = matchResultItems.get('result_slot0' if self.resultWareCount else slotName)
            if resultItem is None or matchResultItem is None:
                continue
            if not itemUtils.IsSameItem(resultItem, matchResultItem):
                return False
            maxStackSize = self.resultWareCount or itemComp.GetItemBasicInfo(resultItem["newItemName"], resultItem["newAuxValue"]).get("maxStackSize")
            if matchResultItem.get('count') + resultItem.get('count') > maxStackSize:
                return False
        return True

    def _Burn(self):
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
            self.ReduceItem('fuel_slot0')
            self.burnDuration = burnDuration * 20
            self.burnTime = burnDuration * 20
            return True
        return False

    def Consume(self):
        """消耗原材料"""
        materialSlotItemDict = self.recipeManager.GetLastUsedRecipeMaterial()
        if materialSlotItemDict is None:
            return
        for slotName, itemDict in materialSlotItemDict.items():
            if itemDict is None:
                continue
            count = itemDict.get("count", 1)
            self.ReduceItem(slotName, count)

    def Produce(self):
        """生产物品"""
        matchedRecipeResult = self.recipeManager.GetLastUsedRecipeResult()
        if matchedRecipeResult is None:
            return
        resultItems = self.GetAllSlotData('result_ware') if self.resultWareCount else self.GetAllSlotData('result')
        for slotName, recipeResultItem in matchedRecipeResult.items():
            realSlotName = 'result_ware_slot' if self.resultWareCount else slotName
            resultItem = resultItems.get(realSlotName)
            if resultItem is None:
                self._SetItem(realSlotName, recipeResultItem)
            else:
                recipeResultItem['count'] = recipeResultItem.get('count', 1) + resultItem.get('count')
                self._SetItem(realSlotName, recipeResultItem)
        if self.slotNum['liquid'] != 0:
            self.blockEntityData['liquid'] = self.GetSlotData('liquid') - 1
    
    def GetBurnData(self):
        burnData = {
            'burnDuration': self.burnDuration,
            'burnProgress': int((self.burnDuration - self.burnTime) * 3 / 2),
            'isBurning': self.burnTime > 0,
            'isProducing': self.burnTime > 0 and self.__CanProduce(),
            'produceProgress': int(self.produceProgress * 3 / 2),
        }
        if self.slotNum['liquid'] != 0:
            burnData['liquid'] = self.blockEntityData['liquid']
        return burnData

    def __GetFuels(self, blockName):
        if blockName in ["ham:mill"]:
            return FUEL_DATA.get('gold', {})
        else:
            return FUEL_DATA.get('coal', {})