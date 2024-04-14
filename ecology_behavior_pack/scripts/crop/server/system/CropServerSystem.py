import mod.server.extraServerApi as serverApi

from scripts.common.modConfig import __DEV__
from scripts.common.data.crop.seed import SEED_LIST
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

    def OnServerItemUse(self, args):
        if not engineUtils.coolDown(args['entityId']):
            return
        # 作物种植
        if args['itemDict']['newItemName'] in SEED_LIST:
            self.__HandlePlantCrop(args)

    def OnBlockNeighborChanged(self, args):
        # 植被下方作物变化
        if cropUtils.IsCrop(args['blockName']) and args['posX'] == args['neighborPosX'] and args['posY'] == args['neighborPosY'] + 1 and args['posZ'] == args['neighborPosZ']:
            self.__HandleCropBelowBlockChange(args)

    def OnBlockRandomTick(self, args):
        # 作物生长
        if cropUtils.IsCrop(args['blockName']):
            self.__HandleCropStageTick(args)

    def __HandlePlantCrop(self, args):
        """种植作物"""
        landPosition = (args["x"], args["y"], args["z"])    # type: tuple[int, int, int]
        dimensionId = args["dimensionId"]   # type: int
        
        # 判断能否种植
        blockName = args['blockName']   # type: str
        itemName = args['itemDict']['newItemName']  # type: str
        entityId = args['entityId']     # type: str
        canPlantResult = CropService.CanPlant(itemName, landPosition, dimensionId)
        if canPlantResult is not True:
            msgComp = engineCompFactory.CreateMsg(entityId)
            if canPlantResult == 'air':
                msgComp.NotifyOneMessage(entityId, '{} 不能种植在空气上'.format(itemName), '§e')
            if canPlantResult == 'fertility':
                msgComp.NotifyOneMessage(entityId, '{} 土地肥力不足'.format(blockName), '§e')
            if canPlantResult == 'landType':
                msgComp.NotifyOneMessage(entityId, '{} 土地类型无法种植 {}'.format(blockName, itemName), '§e')
            if canPlantResult == 'land':
                msgComp.NotifyOneMessage(entityId, '{} 不能种植在 {} 上'.format(itemName, blockName), '§e')
            if canPlantResult == 'temperature':
                msgComp.NotifyOneMessage(entityId, '{} 种植温度不适宜'.format(itemName), '§e')
            if canPlantResult == 'rainfall':
                msgComp.NotifyOneMessage(entityId, '{} 种植湿度不适宜'.format(itemName), '§e')
            return
        
        # 种植作物
        itemComp = engineCompFactory.CreateItem(entityId)
        slotId = itemComp.GetSelectSlotId()
        carriedItemCount = itemComp.GetPlayerItem(minecraftEnum.ItemPosType.CARRIED, 0).get("count") # type: int | None
        if carriedItemCount is None:
            msgComp = engineCompFactory.CreateMsg(entityId)
            msgComp.NotifyOneMessage(entityId, '玩家手上不存在种子，这是一个系统 bug，请报告给开发者群：712936357', '§c')
            return
        plantBlockDict = cropUtils.GetBlockStageDict(itemName, 0)
        abovePosition = positionUtils.GetAbovePosition(landPosition)
        result = blockInfoComp.SetBlockNew(abovePosition, plantBlockDict, dimensionId = dimensionId)
        if not result:
            msgComp = engineCompFactory.CreateMsg(entityId)
            msgComp.NotifyOneMessage(entityId, '种植作物失败', '§c')
            return
        itemComp.SetInvItemNum(slotId, carriedItemCount - 1)

    def __HandleCropBelowBlockChange(self, args):
        position = (args['posX'], args['posY'], args['posZ'])
        dimensionId = args["dimensionId"]
        canPlantOnLand = CropService.CanPlantOnLand(args['blockName'], args['toBlockName'], args['auxValue'])
        logger.debug(canPlantOnLand)
        if isinstance(canPlantOnLand, str):
            blockInfoComp.SetBlockNew(position, {'name': 'minecraft:air', 'aux': 0}, dimensionId=dimensionId)
            CropService.DeleteCropManager(position, dimensionId)
        else:
            cropManager = CropService.GetCropManager(position, dimensionId)
            cropManager.RenewLandInfo()

    def __HandleCropStageTick(self, args):
        """作物tick生长"""
        position = (args['posX'], args['posY'], args['posZ']) # type: tuple[int, int, int]
        dimensionId = args['dimensionId']   # type: int
        cropManager = CropService.GetCropManager(position, dimensionId)
        cropManager.Grow()
