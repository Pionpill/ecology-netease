from abc import abstractmethod
import copy
import mod.server.extraServerApi as serverApi
from scripts.common.utils import itemUtils
from scripts.workbench.common.enum import WorkbenchType
from scripts.common import logger
from scripts.workbench.server.data.recipes import WORKBENCH_MAP
from scripts.workbench.server.proxy import RecipeProxy

minecraftEnum = serverApi.GetMinecraftEnum()
compFactory = serverApi.GetEngineCompFactory()
levelId = serverApi.GetLevelId()
blockEntityComp = compFactory.CreateBlockEntityData(levelId)

class BaseWorkbenchManager(object):
    def __init__(self, blockName, position, dimensionId):
        # type: (str, tuple[int, int, int], int) -> None
        object.__init__(self)
        self.blockName = blockName
        self.position = position
        self.dimensionId = dimensionId
        self.proxy = RecipeProxy(blockName)
        self.blockType = WORKBENCH_MAP[blockName]['type']
        self.slotNum = {
            'material': WORKBENCH_MAP[blockName]['material'],
            'fixed_material': len(WORKBENCH_MAP[blockName].get('fixed_material_items', ())),
            'liquid': WORKBENCH_MAP[blockName].get('liquid', 0),
            'fuel': WORKBENCH_MAP[blockName].get('fuel', 0),
            'result': WORKBENCH_MAP[blockName]['result']
        }
        self.blockEntityData = blockEntityComp.GetBlockEntityData(self.dimensionId, self.position)

    def GetAllSlotData(self, slotTypes = ['material', 'fuel', 'result', 'liquid']):
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
        return slotData
    
    def GetSlotData(self, slotName):
        # type: (str) -> dict
        """从方块实体中获取指定槽的物品"""
        return self.blockEntityData[slotName]

    def _ItemReduce(self, slotName, count = 1):
        # type: (str, int) -> None
        """物品消耗"""
        itemDict = self.GetSlotData(slotName)
        if not itemDict:
            logger.warn("槽 {} 没有物品".format(slotName))
        elif itemDict["count"] < count:
            logger.error("物品自减失败，实际物品数量小于需要减去的数量")
        elif itemDict["count"] == count:
            self.blockEntityData[slotName] = None
        else:
            self.blockEntityData[slotName]['count'] -= count
    
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
            if toItemDict.get('count') == maxStackSize:
                return
            if (swapCount + toItemDict.get('count')) > maxStackSize:
                fromItemCount = fromItemDict['count'] + toItemDict.get('count') - maxStackSize
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

    def _GetItem(self, slotName, playerId):
        """
        获取实体物品
        客户端传来的物品数据并不准备，需要调用该方法获取真实物品数据
        """
        if isinstance(slotName, str):
            return self.GetSlotData(slotName)
        itemComp = compFactory.CreateItem(playerId)
        return itemComp.GetPlayerItem(minecraftEnum.ItemPosType.INVENTORY, slotName)

    def _SetItem(self, slotName, itemDict, playerId = None):
        # type: (str | int, dict, int) -> None
        """设置实体物品"""
        if isinstance(slotName, str):
            if itemDict is None or itemDict.get('count') == 0:
                self.blockEntityData[slotName] = None
            else:
                self.blockEntityData[slotName] = itemDict
        else:
            itemComp = compFactory.CreateItem(playerId)
            itemsDictMap = {
                (minecraftEnum.ItemPosType.INVENTORY, slotName): itemDict
            }
            itemComp.SetPlayerAllItems(itemsDictMap)

    @abstractmethod
    def Consume(self):
        """消耗原材料合成/烧制物品"""
        raise NotImplementedError

    @abstractmethod
    def GetRecipeResultSlotItemDict(self):
        """通过配方获取结果槽物品"""
        raise NotImplementedError

    @abstractmethod
    def Reset(self, playerId):
        """关闭 UI 时重置一些物品"""
        raise NotImplementedError
    
    @abstractmethod
    def GetBurnData(self):
        """获取熔炉数据"""
        raise NotImplementedError
    
    @abstractmethod
    def Tick(self):
        """进行 tick"""
        raise NotImplementedError