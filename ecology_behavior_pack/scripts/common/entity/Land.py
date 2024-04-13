from scripts.common.error import AddonDataError
from scripts.common.enum.LandTag import LandTag
from scripts.common.utils import dataUtils
from scripts.common.data.land import LAND_DATA


class Land(object):
    def __init__(self, blockName):
        data = LAND_DATA.get(blockName)
        if data is None:
            raise AddonDataError('{}: 不存在自定义土地信息'.format(blockName))
        self.blockName = blockName
        self.__data = data

    def GetFertility(self, aux = None):
        # type: (int | None) -> int
        """获取土壤肥沃度"""
        key = ('aux', 'fertility') if aux else 'fertility'
        return self._GetField(key)

    def GetTags(self):
        # type: () -> tuple[LandTag]
        """获取土壤标签"""
        tag = self._GetField('tag')    
        return (tag,) if isinstance(tag, str) else tag  # type: ignore

    def _GetField(self, key, defaultValue = None, data = None):
        """获取字段值，支持递归获取
        
        :param key: 键, str 或可迭代 str 容器
        :param defaultValue: 默认值
        :param data: 数据集，任意类型
        """
        realData = data or self.__data
        return dataUtils.GetField(key, realData, self.blockName, defaultValue)