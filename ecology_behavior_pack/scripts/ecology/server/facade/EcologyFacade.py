from scripts.common.entity.Biome import Biome
from scripts.ecology.server.entity.Ecology import DynamicEcology
from scripts.ecology.server.service import BiomeService, FrameService

class EcologyFacade():
    @staticmethod
    def GetBiomeInfo(position, dimensionId):
        # type: (tuple[int, int, int], int) -> Biome
        """获取生态的固定信息"""
        return BiomeService.GetBiomeInfo(position, dimensionId)
    
    @staticmethod
    def GetEcologyInfo(position, dimensionId):
        # type: (tuple[int, int, int], int) -> DynamicEcology
        """获取某一位置的生态信息"""
        return BiomeService.GetDynamicEcologyInfo(position, dimensionId)
    
    @staticmethod
    def GetFormatDayTime(dimensionId):
        # type: (int) -> str
        """获取当前天的格式化时间"""
        return FrameService.GetFormatDayTime(dimensionId)
    
    @staticmethod
    def HasSun(dimensionId):
        """判断是否出太阳"""
        # type: (int) -> bool
        return FrameService.HasSun(dimensionId)
    
    @staticmethod
    def HasMoon(dimensionId):
        """判断是否出月亮"""
        # type: (int) -> bool
        return FrameService.HasMoon(dimensionId)