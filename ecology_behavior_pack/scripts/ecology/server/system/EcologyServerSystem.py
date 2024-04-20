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
        self.ListenEvents()
        
    def ListenEvents(self):
        engineNamespace = serverApi.GetEngineNamespace()
        engineSystemName = serverApi.GetEngineSystemName()
        self.ListenForEvent(engineNamespace, engineSystemName, "ServerBlockUseEvent", self, self.OnServerBlockUse)
        
    def OnServerBlockUse(self, args):
        """玩家持有剪刀右键作物时显示生态信息"""
        if not engineUtils.coolDown(args['playerId'], 1):
            return
        
        playerId = args["playerId"]
        itemComp = engineCompFactory.CreateItem(playerId)
        carriedItem = itemComp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.CARRIED)
        if not carriedItem or carriedItem.get('newItemName') != 'minecraft:shears':
            return

        position = (args["x"], args["y"], args["z"])
        ecologyInfo = BiomeService.GetDynamicEcologyInfo(position, args["dimensionId"])
        msgComp = engineCompFactory.CreateMsg(args["playerId"])
        msgComp.NotifyOneMessage(playerId, str(ecologyInfo), "§2")
