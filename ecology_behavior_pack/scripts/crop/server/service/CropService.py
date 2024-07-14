import mod.server.extraServerApi as serverApi

from scripts.common import logger
from scripts.common.entity import Crop, GetCrop, GetLand
from scripts.common.error import AddonDevelopError
from scripts.common.utils import mathUtils, positionUtils
from scripts.crop.server.manager import CropManager, CropMsgManager
from scripts.crop.server.service.enum import PlantFailReason
from scripts.crop.server.utils import cropUtils
from scripts.ecology.server.facade import EcologyFacade

levelId = serverApi.GetLevelId()
minecraftEnum = serverApi.GetMinecraftEnum()
engineCompFactory = serverApi.GetEngineCompFactory()
blockInfoComp = engineCompFactory.CreateBlockInfo(levelId)

class CropService(object):
    cropMgrDict = {} # type: dict[tuple[int, int, int, int], CropManager]
    msgMgrDict = {} # type: dict[str, CropMsgManager]

    @staticmethod
    def GetCropManager(position, dimensionId):
        # type: (tuple[int, int, int], int) -> CropManager
        posKey = position + (dimensionId,)
        cropMgr = CropService.cropMgrDict.get(posKey)
        if cropMgr is not None:
            return cropMgr
        cropMgr = CropManager(position, dimensionId)
        CropService.cropMgrDict[posKey] = cropMgr
        return cropMgr
    
    @staticmethod
    def DeleteCropManager(position, dimensionId):
        # type: (tuple[int, int, int], int) -> None
        posKey = position + (dimensionId,)
        if CropService.cropMgrDict.get(posKey):
            del CropService.cropMgrDict[posKey]

    @staticmethod
    def GetMsgManager(playerId):
        # type: (str) -> CropMsgManager
        msgManger = CropService.msgMgrDict.get(playerId)
        if msgManger:
            return msgManger
        msgManger = CropMsgManager(playerId)
        CropService.msgMgrDict[playerId] = msgManger
        return msgManger

    @staticmethod
    def DeleteMsgManager(playerId):
        # type: (str) -> None
        if CropService.msgMgrDict.get(playerId):
            del CropService.msgMgrDict[playerId]

    @staticmethod
    def Plant(seedName, selectPosition, dimensionId, playerId):
        # type: (str, tuple[int, int, int], int, str) -> bool
        """
        种植作物：设置方块，减少种子数量

        :param seedName: 种子名称
        :param selectPosition: 右键点击的位置
        :param dimensionId: 位面
        :param playerId: 玩家id
        """
        itemComp = engineCompFactory.CreateItem(playerId)
        slotId = itemComp.GetSelectSlotId()
        carriedItemCount = itemComp.GetPlayerItem(minecraftEnum.ItemPosType.CARRIED, 0).get("count") # type: int | None
        if carriedItemCount is None:
            msgComp = CropService.GetMsgManager(playerId)
            msgComp.NotifyErrorMessage('玩家手上不存在种子。')
            return False
        blockPrefix = CropService.__GetCrop(seedName).GetBlockPrefix()
        plantBlockDict = cropUtils.GetBlockStageDict(blockPrefix)
        plantPosition = selectPosition if cropUtils.GetReplaceBlock(seedName) else positionUtils.GetAbovePosition(selectPosition) 
        plantResult = blockInfoComp.SetBlockNew(plantPosition, plantBlockDict, dimensionId = dimensionId)
        if not plantResult:
            msgComp = CropService.GetMsgManager(playerId)
            msgComp.NotifyErrorMessage('种植失败。')
            return False
        itemComp.SetInvItemNum(slotId, carriedItemCount - 1)
        return True     

    @staticmethod
    def CanPlant(seedName, selectPosition, dimensionId, playerId = None):
        # type: (str, tuple[int, int, int], int, str | None) -> str | bool
        """
        判断种子能否种植在指定位置上
        依此进行如下判断: 土地，土地类型，土地肥沃度，温度，湿度

        :param seedName: 种子名称
        :param selectPosition: 右键点击的位置
        :param dimensionId: 位面
        :param playerId: 玩家id，用于发消息
        """
        replaceBlockName = cropUtils.GetReplaceBlock(seedName)
        if replaceBlockName:
            # 判断是否为需替换的方块
            selectBlockName = blockInfoComp.GetBlockNew(selectPosition, dimensionId).get('name')
            if selectBlockName != replaceBlockName and selectBlockName and seedName != cropUtils.GetSeedKey(selectBlockName):
                return CropService.__NotifyPlantFailMsg(playerId, PlantFailReason.REPLACE_BLOCK, {'crop': replaceBlockName})
        landPosition = positionUtils.GetBelowPosition(selectPosition) if replaceBlockName else selectPosition
        landBlockInfo = blockInfoComp.GetBlockNew(landPosition, dimensionId)
        landName = landBlockInfo.get('name')
        if landName is None:
            return False
        if not CropService.CanPlantOnLand(seedName, landName, landBlockInfo.get('aux', 0), playerId):
            return False
        crop = CropService.__GetCrop(seedName)
        ecology = EcologyFacade.GetEcologyInfo(landPosition, dimensionId)
        ecologyTemperature = ecology.GetAdjustTemperature()
        cropTemperatureTuple = crop.GetGrowTemperature('can')
        if not mathUtils.between(ecologyTemperature, cropTemperatureTuple):
            return CropService.__NotifyPlantFailMsg(playerId, PlantFailReason.ECOLOGY_TEMPERATURE, {"crop": cropTemperatureTuple, 'ecology': ecologyTemperature})
        ecologyRainfall = ecology.GetAdjustRainfall()
        cropRainfallTuple = crop.GetGrowRainfall('can')
        if not mathUtils.between(ecologyRainfall, cropRainfallTuple):
            return CropService.__NotifyPlantFailMsg(playerId, PlantFailReason.ECOLOGY_RAINFALL, {"crop": cropRainfallTuple, 'ecology': ecologyRainfall})
        return True

    @staticmethod
    def CanPlantOnLand(blockOrSeedName, landBlockName, blockAux = 0, playerId = None):
        # type: (str, str, int, str | None) -> str | bool
        """
        判断某个作物(块)能否种植在方块上
        依此进行如下判断: 土地，土地类型，土地肥沃度

        :param blockOrSeedName: 作物方块或种子名
        :param landBlockName: 土地名称
        :param blockAux: 土地偏移值
        :param playerId: 玩家id，用于发消息
        """
        crop = CropService.__GetCrop(blockOrSeedName)
        land = GetLand(landBlockName)
        if land is None:
            return CropService.__NotifyPlantFailMsg(playerId, PlantFailReason.LAND_UNABLE)
        cropTags = crop.GetGrowLandType()
        landTags = land.GetTags()
        if not mathUtils.hasCommonElements(landTags, cropTags):
            return CropService.__NotifyPlantFailMsg(playerId, PlantFailReason.LAND_TYPE, {'crop': cropTags, 'land': landTags})
        fertility = land.GetFertility(blockAux)
        minFertility =  crop.GetGrowFertilityMin()
        if minFertility > fertility:
            return CropService.__NotifyPlantFailMsg(playerId, PlantFailReason.LAND_FERTILITY, {"crop": minFertility, 'land': fertility})
        return True

    @staticmethod
    def __GetCrop(blockOrItemName):
        # type: (str) -> Crop
        """获取 Crop 对象"""
        cropKey = cropUtils.GetSeedKey(blockOrItemName)
        crop = GetCrop(cropKey)
        if crop is None:
            raise AddonDevelopError('自定义作物 {} 未找到对应的数据'.format(blockOrItemName))
        return crop

    @staticmethod
    def __NotifyPlantFailMsg(playerId, reason, params = {}):
        # type: (str | None, str, dict) -> bool
        if playerId:
            msgMgr = CropService.GetMsgManager(playerId)
            msgMgr.NotifyPlantFailMessage(reason, params)
        return False