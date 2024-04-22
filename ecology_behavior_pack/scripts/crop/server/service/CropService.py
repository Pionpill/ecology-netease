import mod.server.extraServerApi as serverApi

from scripts.common import logger
from scripts.common.entity import Crop, GetCrop, GetLand
from scripts.common.error import AddonDevelopError
from scripts.common.utils import mathUtils
from scripts.crop.server.manager import CropManager, CropMsgManager
from scripts.crop.server.service.enum import PlantFailReason
from scripts.crop.server.utils import cropUtils
from scripts.ecology.server.entity.Ecology import DynamicEcology
from scripts.ecology.server.facade import EcologyFacade

levelId = serverApi.GetLevelId()
engineCompFactory = serverApi.GetEngineCompFactory()
blockInfoComp = engineCompFactory.CreateBlockInfo(levelId)

class CropService(object):
    cropMgrDict = {} # type: dict[tuple[int, int, int, int], CropManager]
    msgMgrDict = {} # type: dict[str, CropMsgManager]

    @staticmethod
    def GetCropManager(position, dimensionId, crop = None, ecology = None):
        # type: (tuple[int, int, int], int, Crop | None, DynamicEcology | None) -> CropManager
        posKey = position + (dimensionId,)
        cropMgr = CropService.cropMgrDict.get(posKey)
        if cropMgr is not None:
            return cropMgr
        cropMgr = CropManager(position, dimensionId, crop, ecology)
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
    def CanPlant(itemName, landPosition, dimensionId, playerId = None):
        # type: (str, tuple[int, int, int], int, str | None) -> str | bool
        landBlockInfo = blockInfoComp.GetBlockNew(landPosition, dimensionId)
        landName = landBlockInfo.get('name')
        if landName is None:
            return False
        if not CropService.CanPlantOnLand(itemName, landName, landBlockInfo.get('aux', 0), playerId):
            return False
        crop = CropService.__GetCrop(itemName)
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
    def CanPlantOnLand(blockOrItemName, landBlockName, blockAux = 0, playerId = None):
        # type: (str, str, int, str | None) -> str | bool
        """判断某个作物(块)能否种植在方块上"""
        crop = CropService.__GetCrop(blockOrItemName)
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