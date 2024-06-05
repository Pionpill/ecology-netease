import mod.server.extraServerApi as serverApi

from scripts.common import logger
from scripts.common.base.service.manager import BaseMsgManager
from scripts.common.enum import LandTag
from scripts.crop.server.service.enum import PlantFailReason

engineCompFactory = serverApi.GetEngineCompFactory()

class CropMsgManager(BaseMsgManager):
    def __init__(self, playerId):
        # type: (str) -> None
        BaseMsgManager.__init__(self, playerId)

    def NotifyPlantFailMessage(self, reason, params = {}):
        # type: (str, dict) -> None
        if reason == PlantFailReason.REPLACE_BLOCK:
            self._NotifyOneWarningMessage('必须种植在 {} 上'.format(params.get('crop')))
            return
        if reason == PlantFailReason.LAND_UNABLE:
            self._NotifyOneWarningMessage('方块不可种植任何作物')
            return
        if reason == PlantFailReason.LAND_FERTILITY:
            self._NotifyOneWarningMessage('土地肥力不足\n土壤肥力: {}\n作物最低肥力要求: {}'.format(params.get('land'), params.get('crop')))
            return
        if reason == PlantFailReason.LAND_TYPE:
            landTagCnTuple = LandTag.GetChinese(params.get('land', 'dirt'))
            cropTagCnTuple = LandTag.GetChinese(params.get('crop', 'dirt'))
            self._NotifyOneWarningMessage('土地无法种植\n土壤可生长: {}\n作物需要: {}'.format(landTagCnTuple, cropTagCnTuple))
            return
        if reason == PlantFailReason.ECOLOGY_TEMPERATURE:
            self._NotifyOneWarningMessage('温度不适宜\n生态温度: {}\n作物可生长温度: {}'.format(round(params.get('ecology', 0), 2), params.get('crop', 0)))
            return
        if reason == PlantFailReason.ECOLOGY_RAINFALL:
            self._NotifyOneWarningMessage('湿度不适宜\n生态湿度: {}\n作物可生长湿度: {}'.format(round(params.get('ecology', 0), 2), params.get('crop')))
            return
