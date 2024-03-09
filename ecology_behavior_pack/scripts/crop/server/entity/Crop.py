from scripts.common.data.crop.crop import CROP_DATA
from scripts.common import logger

class Crop(object):
    def __init__(self, plantInfo, growInfo):
        # type: (dict, dict) -> None 
        self.plantInfo = plantInfo
        self.growInfo = growInfo

    @staticmethod
    def FromSeedKey(seedKey):
        # type: (str) -> Crop
        data = CROP_DATA.get(seedKey)
        if not data:
            logger.error('{}: 不存在对应的作物数据'.format(seedKey))
            return
        return Crop(data.get('plant'), data.get('grow'))
