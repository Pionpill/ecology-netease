import mod.server.extraServerApi as serverApi

from scripts.common import logger
from scripts.common.entity import Crop, GetCrop, GetLand
from scripts.common.error import AddonDevelopError
from scripts.common.utils import positionUtils, mathUtils
from scripts.crop.server.manager import CropManager
from scripts.crop.server.utils import cropUtils
from scripts.ecology.server.entity.Ecology import DynamicEcology
from scripts.ecology.server.facade import EcologyFacade

levelId = serverApi.GetLevelId()
engineCompFactory = serverApi.GetEngineCompFactory()
blockInfoComp = engineCompFactory.CreateBlockInfo(levelId)

class CropService(object):
    cropMgrDict = {} # type: dict[tuple[int, int, int, int], CropManager]

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
        del CropService.cropMgrDict[posKey]

    @staticmethod
    def CanPlant(itemName, landPosition, dimensionId):
        # type: (str, tuple[int, int, int], int) -> str | bool
        landBlockInfo = blockInfoComp.GetBlockNew(landPosition, dimensionId)
        landName = landBlockInfo.get('name')
        if landName is None:
            return 'air'
        landCheckResult = CropService.CanPlantOnLand(itemName, landName, landBlockInfo.get('aux', 0))
        if isinstance(landCheckResult, str):
            return landCheckResult
        crop = CropService.__GetCrop(itemName)
        ecology = EcologyFacade.GetEcologyInfo(landPosition, dimensionId)
        if not mathUtils.between(ecology.GetAdjustTemperature(), crop.GetGrowTemperature('can')):
            return 'temperature'
        if not mathUtils.between(ecology.GetAdjustRainfall(), crop.GetGrowRainfall('can')):
            return 'rainfall'
        return True

    @staticmethod
    def CanPlantOnLand(blockOrItemName, landBlockName, blockAux = None):
        # type: (str, str, int | None) -> str | bool
        """判断某个作物(块)能否种植在方块上"""
        crop = CropService.__GetCrop(blockOrItemName)
        land = GetLand(landBlockName)
        if land is None:
            return 'land'
        fertility = land.GetFertility(blockAux)
        tags = land.GetTags()
        if crop.GetGrowFertilityMin() > fertility:
            return 'fertility'
        if not mathUtils.hasCommonElements(tags, crop.GetGrowLandType()):
            return 'landType'
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