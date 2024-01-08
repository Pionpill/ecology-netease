import mod.server.extraServerApi as serverApi

from scripts.common.utils import engineUtils
from scripts.ecology.server.service import BiomeService
from scripts.common import logger

ServerSystem = serverApi.GetServerSystemCls()
levelId = serverApi.GetLevelId()
engineCompFactory = serverApi.GetEngineCompFactory()

class EcologyServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        self.InitEvents()
        self.ListenEvents()
        
    def InitEvents(self):
        self.__InitServerBlockUseEvent()
        
    def __InitServerBlockUseEvent(self):
        blockUseEventWhiteList = engineCompFactory.CreateBlockUseEventWhiteList(levelId)
        blockUseEventWhiteList.AddBlockItemListenForUseEvent("minecraft:grass")
        
    def ListenEvents(self):
        engineNamespace = serverApi.GetEngineNamespace()
        engineSystemName = serverApi.GetEngineSystemName()
        self.ListenForEvent(engineNamespace, engineSystemName, "ServerBlockUseEvent", self, self.OnServerBlockUse)
        
    def OnServerBlockUse(self, args):
        """玩家持有剪刀右键草地时显示生态信息"""
        if not engineUtils.coolDown(args['playerId'], 1):
            return
        
        playerId = args["playerId"]
        itemComp = engineCompFactory.CreateItem(playerId)
        carriedItem = itemComp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.CARRIED)
        if not carriedItem:
            return
        if carriedItem.get('newItemName') != 'minecraft:shears':
            return

        x,y,z = args["x"], args["y"], args["z"]
        ecologyInfo = BiomeService.GetEcologyInfo((x,y,z), args["dimensionId"])
        msgComp = engineCompFactory.CreateMsg(args["playerId"])
        msgComp.NotifyOneMessage(playerId, str(ecologyInfo), "§2")
