from abc import abstractmethod
import copy
import mod.server.extraServerApi as serverApi

from scripts.common import logger
from scripts.common.data.workbench import SLOT_DATA
from scripts.common.utils import itemUtils
from scripts.workbench.server.manager.RecipeManager import RecipeManager

minecraftEnum = serverApi.GetMinecraftEnum()
compFactory = serverApi.GetEngineCompFactory()
levelId = serverApi.GetLevelId()
blockEntityComp = compFactory.CreateBlockEntityData(levelId)
itemComp = compFactory.CreateItem(levelId)

class BaseWorkbenchManager(object):
    def __init__(self, blockName, position, dimensionId):
        # type: (str, tuple[int, int, int], int) -> None
        object.__init__(self)
        blockEntityData = blockEntityComp.GetBlockEntityData(dimensionId, position)
        if blockEntityData is None:
            logger.error('工作台 {} 不存在实体数据，这是一个逻辑BUG'.format(blockName))
            return
        self.blockEntityData = blockEntityData
        self.blockName = blockName
        self.position = position
        self.dimensionId = dimensionId
        self.recipeManager = RecipeManager(blockName)
        self.blockType = SLOT_DATA[blockName]['type']
        self.slotNum = {
            'material': SLOT_DATA[blockName]['material'],
            'fixed_material': len(SLOT_DATA[blockName].get('fixed_material_items', ())),
            'liquid': SLOT_DATA[blockName].get('liquid', 0),
            'fuel': SLOT_DATA[blockName].get('fuel', 0),
            'result': SLOT_DATA[blockName]['result']
        }
        self.wareItem = SLOT_DATA[blockName].get('ware')
        self.resultWareCount = SLOT_DATA[blockName].get('result_ware_count')

    def GetAllSlotData(self, slotTypes = ['material', 'fuel', 'result', 'result_ware', 'liquid', 'ware']):
        # type：(list | str) => dict
        """
        从方块实体中获取所有物品
        material 包括所有 fixed_material
        """
        if isinstance(slotTypes, str):
            slotTypes = [slotTypes]
        if 'material' in slotTypes:
            slotTypes.append('fixed_material')
        slotData = {}
        for slotPrefix, slotNum in self.slotNum.items():
            if slotPrefix not in slotTypes:
                continue
            for i in range(slotNum):
                slotKey = slotPrefix + '_slot' + str(i)
                slotData[slotKey] = self.blockEntityData[slotKey]
        if self.wareItem and 'ware' in slotTypes:
            slotData['ware_slot'] = self.blockEntityData['ware_slot']
        if self.resultWareCount and 'result_ware' in slotTypes:
            slotData['result_ware_slot'] = self.blockEntityData['result_ware_slot']
        return slotData
    
    def GetSlotData(self, slotName):
        # type: (str) -> dict
        """从方块实体中获取指定槽的物品"""
        return self.blockEntityData[slotName]   # type: ignore

    def SwapItem(self, args):
        # type: (dict) -> None
        """
        1. 物品相同，takePercent 为1: 尝试合并
        2. 物品相同， takePercent 不为1: 尝试部分合并
        3. 物品不同: 交换
        """
        fromSlotName, toSlotName = args['fromSlotName'], args['toSlotName']
        playerId, takePercent = args['playerId'], args['takePercent']
        # 并发情况下，存在客户端物品数据失效问题，因此在服务端获取最新的物品数据
        fromItemDict = self._GetItem(fromSlotName, playerId)
        toItemDict = self._GetItem(toSlotName, playerId)
        # 物品相同，尝试合并
        if itemUtils.IsSameItem(fromItemDict, toItemDict):
            swapCount = int(fromItemDict.get('count') * takePercent)
            itemComp = compFactory.CreateItem(playerId)
            maxStackSize = itemComp.GetItemBasicInfo(toItemDict["newItemName"], toItemDict["newAuxValue"]).get("maxStackSize")
            if toItemDict.get('count', 0) >= maxStackSize:
                return
            if (swapCount + toItemDict.get('count', 0)) > maxStackSize:
                fromItemCount = fromItemDict['count'] + toItemDict.get('count', 0) - maxStackSize
                toItemDict['count'] = maxStackSize
                fromItemDict['count'] = fromItemCount
            else:
                toItemDict['count'] = toItemDict['count'] + swapCount
                fromItemDict['count'] = fromItemDict['count'] - swapCount

            self._SetItem(toSlotName, toItemDict, playerId)
            self._SetItem(fromSlotName, fromItemDict, playerId)
        elif toItemDict is None:
            swapCount = int(fromItemDict.get('count') * takePercent)
            toItemDict = copy.deepcopy(fromItemDict)
            toItemDict['count'] = swapCount
            fromItemDict['count'] = fromItemDict['count'] - swapCount
            self._SetItem(toSlotName, toItemDict, playerId)
            self._SetItem(fromSlotName, fromItemDict, playerId)
        # 物品不同，尝试交换
        else:
            self._SetItem(fromSlotName, toItemDict, playerId)
            self._SetItem(toSlotName, fromItemDict, playerId)

    def IncreaseItem(self, slotName, count = 1):
        # type: (str, int) -> None
        itemDict = self.GetSlotData(slotName)
        if itemDict is None:
            logger.warn("槽 {} 没有物品".format(slotName))
            return
        itemDict = self.GetSlotData(slotName)
        maxStackSize = itemComp.GetItemBasicInfo(itemDict["newItemName"], itemDict["newAuxValue"]).get("maxStackSize")
        if itemDict.get("count", 0) + count > maxStackSize:
            logger.error("物品增加失败，超过最大堆叠值")
        else:
            slotItem = self.GetSlotData(slotName)
            slotItem['count'] += count

    def ReduceItem(self, slotName, count = 1):
        # type: (str, int) -> None
        """物品消耗"""
        itemDict = self.GetSlotData(slotName)
        if itemDict is None:
            logger.warn("槽 {} 没有物品".format(slotName))
        elif itemDict["count"] < count:
            logger.error("物品自减失败，实际物品数量小于需要减去的数量")
        elif itemDict["count"] == count:
            self.blockEntityData[slotName] = None
        else:
            slotItem = self.GetSlotData(slotName)
            slotItem['count'] -= count

    def GetRecipeResultSlotItemDict(self):
        """获取匹配的物品"""
        materialSlotItemDict = self.GetAllSlotData('material')
        if len(materialSlotItemDict) == 0 or all(value is None for value in materialSlotItemDict.values()):
            return {'material_slot' + str(i): None for i in range(self.slotNum['result'])}
        return self.recipeManager.MatchRecipe(materialSlotItemDict)

    def _GetItem(self, slotName, playerId):
        # type: (str | int, str) -> dict
        """
        获取实体物品
        客户端传来的物品数据并不准备，需要调用该方法获取真实物品数据
        """
        if isinstance(slotName, str):
            return self.GetSlotData(slotName)
        itemComp = compFactory.CreateItem(playerId)
        return itemComp.GetPlayerItem(minecraftEnum.ItemPosType.INVENTORY, slotName)

    def _SetItem(self, slotName, itemDict, playerId = None):
        # type: (str | int, dict | None, str | None) -> None
        """设置实体物品"""
        if isinstance(slotName, str):
            if itemDict is None or itemDict.get('count') == 0:
                self.blockEntityData[slotName] = None
            else:
                self.blockEntityData[slotName] = itemDict
        elif playerId:
            itemComp = compFactory.CreateItem(playerId)
            itemsDictMap = {
                (minecraftEnum.ItemPosType.INVENTORY, slotName): itemDict
            }
            itemComp.SetPlayerAllItems(itemsDictMap)

    def GetBurnData(self):
        """获取熔炉数据"""
        return {}

    def Reset(self, playerId):
        """关闭 UI 时重置一些物品"""
        pass

    def Tick(self):
        """进行 tick"""
        pass

    @abstractmethod
    def Consume(self, playerId = None):
        """消耗原材料合成/烧制物品"""
        raise NotImplementedError
    
