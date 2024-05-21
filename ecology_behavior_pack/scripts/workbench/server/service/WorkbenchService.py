from scripts.workbench.common.enum import WorkbenchType
from scripts.common import logger
from scripts.common.data.workbench.slot import SLOT_DATA
from scripts.workbench.server.manager import CraftingManager, FurnaceManager
from scripts.workbench.server.manager.base import BaseWorkbenchManager

class WorkbenchService(object):
    blockUsingMap = {} # key: (x,y,z,dimensionId) value: [playId]
    playerUsingMap = {} # key: playerId value: {position, dimensionId}
    workbenchMgrMap = {} # key: (x,y,z,dimensionId) value: workbenchMgr

    @staticmethod
    def IsWorkbenchBlock(blockName, type = None):
        # type: (str, None | str) -> bool
        if type is None:
            return blockName in SLOT_DATA.keys()
        blockInfo = SLOT_DATA.get(blockName)
        if blockInfo:
            return blockInfo['type'] == type
        return False
    
    @staticmethod
    def SetPlayerUsingBlock(playerId, position, dimensionId):
        # type: (int, tuple, int) -> None
        if not WorkbenchService.playerUsingMap.get(playerId):
            WorkbenchService.playerUsingMap[playerId] = {
                'position': position,
                'dimensionId': dimensionId,
            }
        posKey = position + (dimensionId,)
        if not WorkbenchService.blockUsingMap.get(posKey):
            WorkbenchService.blockUsingMap[posKey] = [playerId]
        else:
            WorkbenchService.blockUsingMap[posKey].append(playerId)

    @staticmethod
    def GetPlayerUsingBlock(playerId):
        # type: (int) -> dict | None
        return WorkbenchService.playerUsingMap.get(playerId)
    
    @staticmethod
    def DeletePlayerUsingBlock(playerId, position, dimensionId):
        # type: (int, tuple, int) -> None
        WorkbenchService.playerUsingMap[playerId] = None
        posKey = position + (dimensionId,)
        playerList = WorkbenchService.blockUsingMap.get(posKey)
        playerList.remove(playerId)
        if len(playerList) == 0:
            del WorkbenchService.blockUsingMap[posKey]
        del WorkbenchService.playerUsingMap[playerId]
        
    @staticmethod
    def DeleteWorkbenchManager(position, dimensionId):
        # type: (tuple, int) -> None
        posKey = position + (dimensionId,)
        del WorkbenchService.workbenchMgrMap[posKey]
    
    @staticmethod
    def GetBlockUsingPlayerList(position, dimensionId):
        # type: (tuple, int) -> list[str]
        """获取正在使用工作台的用户列表"""
        posKey = position + (dimensionId,)
        return WorkbenchService.blockUsingMap.get(posKey)

    @staticmethod
    def GetWorkbenchMgr(position, dimensionId, blockName = None):
        # type: (tuple, int, str | None) -> BaseWorkbenchManager
        """获取工作台管理实例，如果不存在会通过 blockName 创建"""
        posKey = position + (dimensionId,)
        workbenchMgr = WorkbenchService.workbenchMgrMap.get(posKey)
        if workbenchMgr:
            return workbenchMgr
        
        if not blockName:
            logger.error('传入 blockName 以创建管理实例')
        
        
        if SLOT_DATA[blockName]['type'] == WorkbenchType.Crafting:
            workbenchMgr = CraftingManager(blockName, position, dimensionId)
        else:
            workbenchMgr = FurnaceManager(blockName, position, dimensionId)
        WorkbenchService.workbenchMgrMap[posKey] = workbenchMgr
        return workbenchMgr
