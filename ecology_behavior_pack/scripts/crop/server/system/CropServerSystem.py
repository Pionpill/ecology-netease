import mod.server.extraServerApi as serverApi

from scripts.common.modConfig import __DEV__
from scripts.common.data.crop.seed import SEED_LIST
from scripts.common import logger
from scripts.common.utils import engineUtils, positionUtils
from scripts.crop.server.service import CropService
from scripts.crop.server.utils import cropUtils, entityUtils
from scripts.ecology.server.facade import EcologyFacade

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
        # 判断土地上方是否为空气
        position = (args["x"], args["y"], args["z"])    # type: tuple[int, int, int]
        dimensionId = args["dimensionId"]   # type: int
        abovePosition = positionUtils.GetAbovePosition(position)
        aboveBlockName = blockInfoComp.GetBlockNew(abovePosition, dimensionId).get('name')  # type: str | None
        if aboveBlockName is None or aboveBlockName != "minecraft:air":
            return
        
        # 判断生态是否可以种植
        blockName = args['blockName']   # type: str
        itemName = args['itemDict']['newItemName']  # type: str
        entityId = args['entityId']     # type: str
        ecologyInfo = EcologyFacade.GetEcologyInfo(position, dimensionId)
        canPlantResult = CropService.CanPlant(itemName, blockName, ecologyInfo.temperature, ecologyInfo.rainfall)
        if canPlantResult is not True:
            msgComp = engineCompFactory.CreateMsg(entityId)
            if canPlantResult == 'block' and blockName in ["minecraft:grass"]:
                msgComp.NotifyOneMessage(entityId, '该作物不能种植在当前方块上', '§e')
            if canPlantResult == 'temperature':
                msgComp.NotifyOneMessage(entityId, '该作物种植温度不适宜', '§e')
            if canPlantResult == 'rainfall':
                msgComp.NotifyOneMessage(entityId, '该作物种植湿度不适宜', '§e')
            return
        
        # 种植作物
        itemComp = engineCompFactory.CreateItem(entityId)
        slotId = itemComp.GetSelectSlotId()
        carriedItemCount = itemComp.GetPlayerItem(minecraftEnum.ItemPosType.CARRIED, 0).get("count")
        if carriedItemCount is None:
            msgComp = engineCompFactory.CreateMsg(entityId)
            msgComp.NotifyOneMessage(entityId, '玩家手上不存在种子，这是一个系统 bug，请报告给开发者群：712936357', '§c')
            return
        plantBlockDict = cropUtils.GetBlockStageDict(itemName, 0)
        result = blockInfoComp.SetBlockNew(abovePosition, plantBlockDict, dimensionId = dimensionId)
        itemComp.SetInvItemNum(slotId, carriedItemCount - 1)

    def __HandleCropBelowBlockChange(self, args):
        if not CropService.CanPlantOnBlock(args['blockName'], args['toBlockName']):
            position = (args['posX'], args['posY'], args['posZ'])
            blockInfoComp.SetBlockNew(position, {'name': 'minecraft:air', 'aux': 0}, dimensionId=args["dimensionId"])

    def __HandleCropStageTick(self, args):
        """作物tick生长"""
        blockName = args['blockName']   # type: str
        position = (args['posX'], args['posY'], args['posZ']) # type: tuple[int, int, int]
        dimensionId = args['dimensionId']   # type: int

        # 从作物方块中获取生物群系信息，减少重复计算(空间换时间)
        blockEntityData = blockEntityDataComp.GetBlockEntityData(dimensionId, position)
        if blockEntityData is None:
            logger.error('不存在作物 {} 实体数据'.format(blockName))
            return
        tickCount = CropService.GetStageTickCount(blockName)
        if tickCount is None:
            return
        if blockEntityData['biome_name'] is None:
            biomeInfo = EcologyFacade.GetBiomeInfo(position, dimensionId)
            entityUtils.SetBiomeInfoToBlockEntityData(blockEntityData, biomeInfo)

        # 判断作物能否生长
        biomeInfo = entityUtils.GetBiomeInfoFromBlockEntityData(blockEntityData)
        ecologyInfo = EcologyFacade.GetEcologyInfo(position, dimensionId, biomeInfo)
        brightness = blockInfoComp.GetBlockLightLevel(position, dimensionId)
        belowPosition = positionUtils.GetBelowPosition(position)
        plantBlockName = blockInfoComp.GetBlockNew(belowPosition, dimensionId).get('name')
        if plantBlockName is None:
            blockInfoComp.SetBlockNew(position, {'name': 'minecraft:air', 'aux': 0}, dimensionId)
            return
        if not CropService.CanGrow(blockName, ecologyInfo, brightness, plantBlockName):
            return

        # 作物生长
        weather = 'rain' if weatherComp.IsRaining else None
        growTicks = CropService.CalculateGrowTick(blockName, ecologyInfo, brightness, weather)
        blockTick = blockEntityData['tick'] or 0
        nextTick = growTicks + blockTick
        if nextTick <= tickCount:
            blockEntityData['tick'] = nextTick
        elif not CropService.IsLastStage(blockName):
            entityBiomeInfo = entityUtils.GetBiomeInfoFromBlockEntityData(blockEntityData)
            blockNameList = blockName.split("_")
            blockNameList[-1] = str(int(blockNameList[-1]) + 1)
            nextBlock = {"name": "_".join(blockNameList), "aux": 0}
            blockInfoComp.SetBlockNew(position, nextBlock, dimensionId=dimensionId)
            newBlockEntityData = blockEntityDataComp.GetBlockEntityData(dimensionId, position)
            if newBlockEntityData is None:
                logger.error('生长后 {} 无法获取实体数据'.format(nextBlock.get('name', blockName)))
                return
            entityUtils.SetBiomeInfoToBlockEntityData(newBlockEntityData, entityBiomeInfo)
            newBlockEntityData['tick'] = nextTick - tickCount
