import mod.server.extraServerApi as serverApi

from scripts.common.modConfig import __DEV__
from scripts.common import logger
from scripts.common.utils import engineUtils, positionUtils
from scripts.crop.server.service import CropService
from scripts.crop.server.utils import cropUtils

minecraftEnum = serverApi.GetMinecraftEnum()
ServerSystem = serverApi.GetServerSystemCls()
levelId = serverApi.GetLevelId()
engineCompFactory = serverApi.GetEngineCompFactory()
blockInfoComp = engineCompFactory.CreateBlockInfo(levelId)
weatherComp = engineCompFactory.CreateWeather(levelId)
blockEntityDataComp = engineCompFactory.CreateBlockEntityData(levelId)

blockRemoveCoolDownDict = {} # type: dict[tuple[int, int, int, int], float]
cropCoolDownDict = {} # type: dict[tuple[int, int, int, int], float]

class CropServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        self.ListenEvents()

    def ListenEvents(self):
        engineNamespace = serverApi.GetEngineNamespace()
        engineSystemName = serverApi.GetEngineSystemName()
        self.ListenForEvent(engineNamespace, engineSystemName, "ServerItemUseOnEvent", self, self.OnServerItemUse)
        self.ListenForEvent(engineNamespace, engineSystemName, "BlockNeighborChangedServerEvent", self, self.OnBlockNeighborChanged)
        self.ListenForEvent(engineNamespace, engineSystemName, "BlockRandomTickServerEvent", self, self.OnBlockRandomTick)
        self.ListenForEvent(engineNamespace, engineSystemName, "BlockRemoveServerEvent", self, self.OnBlockRemove)
        self.ListenForEvent(engineNamespace, engineSystemName, "ServerBlockUseEvent", self, self.OnServerBlockUse)

    def OnServerItemUse(self, args):
        if not engineUtils.coolDown(args['entityId'], 0.2, cropCoolDownDict):
            return
        
        blockName = args['blockName'] # type: str
        itemName = args['itemDict']['newItemName'] # type: str
        position = (args["x"], args["y"], args["z"]) # tuple[int, int, int]
        dimensionId = args["dimensionId"]
        playerId = args['entityId']

        # 作物种植
        if cropUtils.IsSeed(itemName):
            params = {
                'position': position,
                'dimensionId': dimensionId,
                'seedName': itemName,
                'playerId': playerId
            }
            self.__HandlePlantCrop(params)

        # 放大镜显示作物生长信息
        if itemName == "ham:magnifier" and cropUtils.IsCropBlock(blockName):
            cropManager = CropService.GetCropManager(position, dimensionId)
            msgComp = engineCompFactory.CreateMsg(playerId)
            msgComp.NotifyOneMessage(playerId, cropManager.GetGrowInfo(), "§2")

    def OnBlockNeighborChanged(self, args):
        position = (args['posX'], args['posY'], args['posZ']) # type: tuple[int, int, int]
        neighPosition = (args['neighborPosX'], args['neighborPosY'], args['neighborPosZ']) # type: tuple[int, int, int]
        if cropUtils.IsCropBlock(args['blockName']) and positionUtils.IsOnSameLocation(position, neighPosition):
            if args['posY'] == args['neighborPosY'] + 1:
                # 植被土地变化
                self.__HandleCropLandChange(args)
            if args['neighborPosY'] > args['posY']:
                # 植被上方方块变化
                self.__HandleCropAboveBlockChange(args)

    def OnBlockRandomTick(self, args):
        # 作物生长
        if cropUtils.IsCropBlock(args['fullName']):
            self.__HandleCropStageTick(args)

    def OnBlockRemove(self, args):
        position = (args['x'], args['y'], args['z'])
        dimension = args['dimension']
        posKey = position + (dimension,) # type: tuple[int, int, int, int]
        if not engineUtils.coolDown(posKey, 0.2, blockRemoveCoolDownDict):
            return
        cropManager = CropService.GetCropManager(position, dimension)
        if cropManager.growBlockRemove:
            cropManager.growBlockRemove = False
            return
        # 作物销毁
        if cropUtils.IsCropBlock(args['fullName']):
            self.__HandleCropRemove(args)

    def OnServerBlockUse(self, args):
        if not engineUtils.coolDown(args['playerId']):
            return
        blockName = args['blockName']
        # 作物收获
        if cropUtils.IsCropBlock(blockName):
            self.__HandleHarvestCrop(args)
        # 种植在自定义可替换方块上
        if cropUtils.GetSeedByReplaceBlock(blockName):
            params = {
                'position': (args["x"], args["y"], args["z"]),
                'dimensionId': args["dimensionId"],
                'seedName': args['itemDict']['newItemName'],
                'playerId': args['playerId']
            }
            self.__HandlePlantCrop(params)

    def __HandlePlantCrop(self, params):
        """种植作物，需包含特定的参数"""
        selectPosition = params["position"]    # type: tuple[int, int, int]
        dimensionId = params["dimensionId"]   # type: int
        seedName = params['seedName']  # type: str
        playerId = params['playerId']     # type: str
        if not CropService.CanPlant(seedName, selectPosition, dimensionId, playerId):
            return
        CropService.Plant(seedName, selectPosition, dimensionId, playerId)

    def __HandleCropLandChange(self, args):
        position = (args['posX'], args['posY'], args['posZ'])
        dimensionId = args["dimensionId"]
        canPlantOnLand = CropService.CanPlantOnLand(args['blockName'], args['toBlockName'], args['auxValue'])
        if isinstance(canPlantOnLand, str) or not canPlantOnLand:
            blockInfoComp.SetBlockNew(position, {'name': 'minecraft:air', 'aux': 0}, dimensionId=dimensionId)
            CropService.DeleteCropManager(position, dimensionId)
        else:
            cropManager = CropService.GetCropManager(position, dimensionId)
            cropManager.RenewLandInfo()

    def __HandleCropAboveBlockChange(self, args):
        neighPosition = (args['neighborPosX'], args['neighborPosY'], args['neighborPosZ'])
        dimensionId = args["dimensionId"] # type: int
        blockName = blockInfoComp.GetBlockNew(neighPosition, dimensionId).get('name')
        if blockName is None or blockName == 'minecraft:air':
            return
        position = (args['posX'], args['posY'], args['posZ']) # type: tuple[int, int, int]
        crop = CropService.GetCropManager(position, dimensionId)
        if not crop.CanGrowToStage():
            result = blockInfoComp.SetBlockNew(position, {'name': 'minecraft:air', 'aux': 0}, dimensionId = dimensionId)
            if not result:
                logger.error('删除位置：{} 的作物失败，这是一个系统 bug'.format(position))
            CropService.DeleteCropManager(position, dimensionId)

    def __HandleCropStageTick(self, args):
        """作物tick生长"""
        position = (args['posX'], args['posY'], args['posZ']) # type: tuple[int, int, int]
        dimensionId = args['dimensionId']   # type: int
        blockName = blockInfoComp.GetBlockNew(position, dimensionId).get('name')
        if blockName == 'minecraft:air':
            return
        cropManager = CropService.GetCropManager(position, dimensionId)
        cropManager.Grow()

    def __HandleCropRemove(self, args):
        """作物被销毁"""
        position = (args['x'], args['y'], args['z']) # type: tuple[int, int, int]
        dimensionId = args['dimension']   # type: int
        cropManager = CropService.GetCropManager(position, dimensionId)
        if cropManager.Harvest(True):
            CropService.DeleteCropManager(position, dimensionId)

    def __HandleHarvestCrop(self, args):
        """作物收获"""
        position = (args['x'], args['y'], args['z']) # type: tuple[int, int, int]
        dimensionId = args['dimensionId']   # type: int
        cropManager = CropService.GetCropManager(position, dimensionId)
        if cropManager.Harvest(False) and blockInfoComp.GetBlockNew(position, dimensionId).get('name') == 'minecraft:air':
            CropService.DeleteCropManager(position, dimensionId)