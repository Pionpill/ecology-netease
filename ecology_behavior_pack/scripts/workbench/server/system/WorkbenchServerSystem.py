import mod.server.extraServerApi as serverApi

from scripts.workbench.common.enum import WorkbenchType
from scripts.workbench.common.events import WorkbenchOutSlotClickEvent, WorkbenchSlotItemSwapEvent, WorkbenchBlockUICloseEvent, WorkbenchBlockUseEvent, WorkbenchUIRefreshEvent
from scripts.common import modConfig
from scripts.common import logger
from scripts.common.utils import engineUtils
from scripts.workbench.server.service import WorkbenchService

compFactory = serverApi.GetEngineCompFactory()
levelId = serverApi.GetLevelId()
ServerSystem = serverApi.GetServerSystemCls()
blockEntityComp = compFactory.CreateBlockEntityData(levelId)

blockBenchCoolDownDict = {}

class WorkbenchServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        self.ListenEvents()

    def ListenEvents(self):
        engineNamespace = serverApi.GetEngineNamespace()
        engineSystemName = serverApi.GetEngineSystemName()
        # 监听原生事件
        self.ListenForEvent(engineNamespace, engineSystemName, 'ServerBlockUseEvent', self, self.OnServerBlockUse)
        self.ListenForEvent(engineNamespace, engineSystemName, "ServerBlockEntityTickEvent", self, self.OnBlockEntityTick)
        # TEST 待测试
        self.ListenForEvent(engineNamespace, engineSystemName, 'PlayerDieEvent', self, self.OnPlayerDie)
        self.ListenForEvent(engineNamespace, engineSystemName, 'BlockRemoveServerEvent', self, self.OnBlockRemove)
        # 监听客户端事件
        self.ListenForEvent(modConfig.ADDON_NAME, modConfig.WORKBENCH_CLIENT_NAME, WorkbenchBlockUICloseEvent, self, self.OnWorkbenchBlockUIClose)
        self.ListenForEvent(modConfig.ADDON_NAME, modConfig.WORKBENCH_CLIENT_NAME, WorkbenchSlotItemSwapEvent, self, self.OnSlotItemSwap)
        self.ListenForEvent(modConfig.ADDON_NAME, modConfig.WORKBENCH_CLIENT_NAME, WorkbenchOutSlotClickEvent, self, self.OnOutSlotClick)

    def OnServerBlockUse(self, args):
        """自定义工作台使用"""
        blockName = args['blockName']
        playerId = args['playerId']
        if (not WorkbenchService.IsWorkbenchBlock(blockName)) or WorkbenchService.GetPlayerUsingBlock(playerId):
            return
        if not engineUtils.coolDown(playerId, 1, blockBenchCoolDownDict):
            return
        
        logger.info('打开工作台: {}'.format(blockName))
        position = (args['x'], args['y'], args['z'])
        dimensionId = args['dimensionId']
        WorkbenchService.SetPlayerUsingBlock(playerId, position, dimensionId)

        workbenchMgr = WorkbenchService.GetWorkbenchMgr(position, dimensionId, blockName)
        args = self.CreateEventData()
        args['position'] = position
        args['dimensionId'] = dimensionId
        args['playerId'] = playerId
        args['blockName'] = blockName
        args['slotData'] = workbenchMgr.GetAllSlotData()
        args['blockType'] = workbenchMgr.blockType
        if workbenchMgr.blockType is WorkbenchType.Furnace:
            args['burnData'] = workbenchMgr.GetBurnData()
        self.NotifyToClient(playerId, WorkbenchBlockUseEvent, args)

    def OnBlockEntityTick(self, args):
        blockName = args["blockName"]
        if not WorkbenchService.IsWorkbenchBlock(blockName, WorkbenchType.Furnace):
            return
        position = (args["posX"], args["posY"], args["posZ"])
        dimensionId = args["dimension"]
        workbenchMgr = WorkbenchService.GetWorkbenchMgr(position, dimensionId, blockName)
        if workbenchMgr.Tick():
            self.__RefreshWorkbenchUI(position, dimensionId, blockName)

    def OnWorkbenchBlockUIClose(self, args):
        """
        关闭工作台
        1. 重置管理类与实体数据
        2. 如果是 craftingTable 返回材料
        """
        WorkbenchService.DeletePlayerUsingBlock(args['playerId'], args['position'], args['dimensionId'])
        blockType = args["blockType"]
        if blockType == WorkbenchType.Furnace:
            return
        position, dimensionId, blockName = args["position"], args["dimensionId"], args["blockName"]
        workbenchMgr = WorkbenchService.GetWorkbenchMgr(position, dimensionId, blockName)
        workbenchMgr.Reset(args['playerId'])

    def OnSlotItemSwap(self, args):
        position, dimensionId, blockName = args["position"], args["dimensionId"], args["blockName"]
        workbenchMgr = WorkbenchService.GetWorkbenchMgr(position, dimensionId, blockName)
        workbenchMgr.SwapItem(args)
        self.__RefreshWorkbenchUI(position, dimensionId, blockName)

    def OnOutSlotClick(self, args):
        position, dimensionId, playerId = args["position"], args["dimensionId"], args["playerId"]
        slotName, blockName = args["slotName"], args["blockName"]
        workbenchMgr = WorkbenchService.GetWorkbenchMgr(position, dimensionId)
        resultItemDict = None
        # 工作台消耗原材料
        if workbenchMgr.blockType == WorkbenchType.Crafting:
            resultItemDict = workbenchMgr.GetRecipeResultSlotItemDict().get(slotName)
            workbenchMgr.Consume()
        # 熔炉更新数据
        if workbenchMgr.blockType == WorkbenchType.Furnace:
            resultItemDict = workbenchMgr._GetItem(slotName, playerId)
            workbenchMgr.ReduceItem(slotName, resultItemDict.get('count'))
        # 物品更新到背包
        itemComp = compFactory.CreateItem(playerId)
        itemComp.SpawnItemToPlayerInv(resultItemDict, playerId)
        self.__RefreshWorkbenchUI(position, dimensionId, blockName)

    def OnPlayerDie(self, args):
        """关闭UI，清空记录"""
        playerId = args["id"]
        blockInfo = WorkbenchService.GetPlayerUsingBlock(playerId)
        args = self.CreateEventData()
        if blockInfo:
            self.NotifyToClient(playerId, WorkbenchBlockUICloseEvent, args)
            WorkbenchService.DeletePlayerUsingBlock(playerId, blockInfo['position'], blockInfo['dimensionId'])

    def OnBlockRemove(self, args):
        blockName = args['fullName']
        if not WorkbenchService.IsWorkbenchBlock(blockName):
            return
        position = (args['x'], args['y'], args['z'])
        dimensionId = args['dimension']
        playerList = WorkbenchService.GetBlockUsingPlayerList(position, dimensionId)
        args = self.CreateEventData()
        if playerList:
            self.NotifyToMultiClients(playerList, WorkbenchBlockUICloseEvent, args)
            for playerId in playerList:
                WorkbenchService.DeletePlayerUsingBlock(playerId, position, dimensionId)
        workbenchMgr = WorkbenchService.GetWorkbenchMgr(position, dimensionId, blockName)
        slotData = workbenchMgr.GetAllSlotData(['material', 'fuel', 'result', 'liquid', 'ware'])
        if (slotData is not None) and any(item is not None for item in slotData.values()):
            itemComp = compFactory.CreateItem(levelId)
            for itemDict in slotData.values():
                if itemDict:
                    itemComp.SpawnItemToLevel(itemDict, dimensionId, position)
        WorkbenchService.DeleteWorkbenchManager(position, dimensionId)

    def __RefreshWorkbenchUI(self, position, dimensionId, blockName):
        # type: (tuple, int, str) -> None
        """更新UI，会匹配配方"""
        workbenchMgr = WorkbenchService.GetWorkbenchMgr(position, dimensionId, blockName)
        args = self.CreateEventData()
        args['position'] = position
        args['dimensionId'] = dimensionId
        args['blockName'] = blockName
        args['slotData'] = workbenchMgr.GetAllSlotData()
        args['blockType'] = workbenchMgr.blockType

        # 工作台更新结果槽
        if workbenchMgr.blockType is WorkbenchType.Crafting:
            resultItemDict = workbenchMgr.GetRecipeResultSlotItemDict()
            args['slotData'].update(resultItemDict)
        args['burnData'] = workbenchMgr.GetBurnData() if workbenchMgr.blockType is WorkbenchType.Furnace else {}

        playerList = WorkbenchService.GetBlockUsingPlayerList(position, dimensionId)
        if playerList:
            self.NotifyToMultiClients(playerList, WorkbenchUIRefreshEvent, args)
