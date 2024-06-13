from scripts.common.enum.EffectType import EffectType
from scripts.common.error import AddonDataError


class Effect(object):
    def __init__(self, data):
        # type: (dict) -> None
        self.__data = data

    def GetName(self):
        # type: () -> str
        name = self.__data.get('name')
        if name is None:
            raise AddonDataError('效果不存在name字段')
        return name

    def GetChance(self):
        # type: () -> float
        chance = self.__data.get('chance')
        if chance is None:
            raise AddonDataError('效果不存在chance字段')
        return chance

    def GetDuration(self):
        # type: () -> int
        duration = self.__data.get('duration')
        if duration is None:
            raise AddonDataError('效果不存在duration字段')
        return duration
    
    def GetAmplifier(self):
        # type: () -> int
        amplifier = self.__data.get('amplifier')
        if amplifier is None:
            raise AddonDataError('效果不存在amplifier字段')
        return amplifier
    
    def GetTags(self):
        # type: () -> tuple[str, ...] | None
        return self.__data.get('tag')
    
    def GetChinese(self):
        return EffectType.GetChinese(self.GetName())