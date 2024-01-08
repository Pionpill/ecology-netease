from scripts.common.params import BiomeInfo, EcologyInfo
from scripts.ecology.server.entity import Biome
from scripts.ecology.server.service import BiomeService, TimeService

class EcologyFacade():
    @staticmethod
    def GetBiomeInfo(position, dimensionId):
        # type: (tuple[int, int, int], int) -> BiomeInfo
        """获取生态的固定信息"""
        return BiomeService.GetBiomeInfo(position, dimensionId)
    
    @staticmethod
    def GetBiomeInfoFromData(biomeData, biomeName = None):
        # type: (dict, str) -> Biome
        """从数据构造 Biome 对象"""
        return Biome.FromData(biomeData, biomeName)
    
    @staticmethod
    def GetEcologyInfo(position, dimensionId, basicBiome = None):
        # type: (tuple[int, int, int], int, BiomeInfo) -> EcologyInfo
        """获取某一位置的生态信息"""
        return BiomeService.GetEcologyInfo(position, dimensionId, basicBiome)
    
    @staticmethod
    def GetFormatDayTime(dimensionId):
        # type: (int) -> str
        """获取当前天的格式化时间"""
        return TimeService.GetFormatDayTime(dimensionId)
    
    @staticmethod
    def HasSun(dimensionId):
        """判断是否出太阳"""
        # type: (int) -> bool
        return TimeService.HasSun(dimensionId)
    
    @staticmethod
    def HasMoon(dimensionId):
        """判断是否出月亮"""
        # type: (int) -> bool
        return TimeService.HasMoon(dimensionId)