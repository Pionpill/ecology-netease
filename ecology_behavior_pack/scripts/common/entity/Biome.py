from scripts.common.enum import BiomeTag
from scripts.common.enum import Dimension
from scripts.common.utils import dataUtils
from scripts.common.error import AddonDataError
from scripts.common.data.biome import BIOME_DATA
from scripts.common import logger


class Biome(object):
    cacheMap = {}

    def __init__(self, data):
        # type: (dict) -> None
        """
        通过数据字典创建
        数据字典包含: name, name_cn, temperature, rainfall, dimension, tags
        """
        self.biomeName = data.get('name')
        if data is None:
            raise AddonDataError('{}: 不存在对应的生态数据'.format(self.biomeName))
        self.__data = data

    def GetData(self):
        # type: () -> dict[str, str | float | tuple[BiomeTag]]
        return self.__data

    def GetCNName(self):
        # type: () -> str
        return self._GetField('name_cn')
    
    def GetTemperature(self):
        # type: () -> int
        return self._GetField('temperature')

    def GetRainfall(self):
        # type: () -> int
        return self._GetField('rainfall')
    
    def GetDimension(self):
        # type: () -> Dimension
        return self._GetField('dimension')
    
    def GetTags(self):
        # type: () -> tuple[BiomeTag, ...]
        return self._GetField('tags')

    def _GetField(self, key, defaultValue = None, data = None):
        """获取字段值，支持递归获取
        
        :param key: 键, str 或可迭代 str 容器
        :param defaultValue: 默认值
        :param data: 数据集，任意类型
        """
        realData = data or self.__data
        return dataUtils.GetField(key, realData, self.biomeName, defaultValue)

    def __str__(self):
        return "=================\n生物群系信息: {0} ({1})\n温度: {2}℃\n湿度: {3}％\n=================".format(self.biomeName, self.GetCNName(), self.GetTemperature(), self.GetRainfall())

    @staticmethod
    def FromData(biomeName):
        # type: (str) -> Biome
        """通过生态名从数据库中获取"""
        data = BIOME_DATA.get(biomeName)
        if data is None:
            logger.error('未查询到 {} 相关的生态数据')
            data = BIOME_DATA.get('plains')
        if data is None:
            raise AddonDataError('{}: 不存在对应的生态数据'.format(biomeName))
        data['name'] = biomeName
        return Biome(data)
    
    @staticmethod
    def FromBiomeName(biomeName):
        # type: (str) -> Biome | None
        """获取生态实例，单例模式"""
        biome = Biome.cacheMap.get(biomeName)
        if biome is not None:
            return biome
        try:
            biome = Biome.FromData(biomeName)
        except AddonDataError as e:
            logger.warn(e.message)
            return None
        Biome.cacheMap[biomeName] = biome
        return biome
