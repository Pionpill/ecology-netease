import mod.server.extraServerApi as serverApi

from scripts.common.utils import engineUtils
from scripts.ecology.server.service.BiomeService import BiomeService
from scripts.common import logger

ServerSystem = serverApi.GetServerSystemCls()
levelId = serverApi.GetLevelId()
engineCompFactory = serverApi.GetEngineCompFactory()

ecologyCoolDownDict = {} # type: dict[tuple[int, int, int, int], float]

class EcologyServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        self.ListenEvents()
        
    def ListenEvents(self):
        engineNamespace = serverApi.GetEngineNamespace()
        engineSystemName = serverApi.GetEngineSystemName()
        self.ListenForEvent(engineNamespace, engineSystemName, "ServerItemUseOnEvent", self, self.OnServerItemUseOn)

    def OnServerItemUseOn(self, args):
        """玩家持有放大镜右键原版方块时展示生态信息"""
        playerId = args['entityId']
        if not engineUtils.coolDown(playerId, 0.2, ecologyCoolDownDict):
            return
        
        blockName = args['blockName'] # type: str
        itemName = args['itemDict']['newItemName'] # type: str
        if itemName == "ham:magnifier" and "minecraft" in blockName:
            position = (args["x"], args["y"], args["z"])
            ecologyInfo = BiomeService.GetDynamicEcologyInfo(position, args["dimensionId"])
            msgComp = engineCompFactory.CreateMsg(playerId)
            msgComp.NotifyOneMessage(playerId, str(ecologyInfo), "§2")