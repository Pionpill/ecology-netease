from scripts.common.enum import BiomeTag
from scripts.common.entity.Biome import Biome


class FixedEcology(Biome):
    """静态生态数据"""
    def __init__(self, data):
        # type: (dict) -> None
        """除了生物群系数据，还包含 temperature_avg rainfall_avg """
        Biome.__init__(self, data)

    def GetAvgTemperature(self):
        # type: () -> float
        return self._GetField('temperature_avg')

    def GetAvgRainfall(self):
        # type: () -> float
        return self._GetField('rainfall_avg')
    
    def __str__(self):
        return "=================\n固定生态: {0} ({1})\n温度: {2}\n湿度: {3}\n=================".format(self.biomeName, self.GetCNName(), self.GetAvgTemperature(), self.GetAvgRainfall())

class DynamicEcology(Biome):
    """动态生态数据"""
    def __init__(self, data):
        # type: (dict) -> None
        """除了生物群系数据，还包含 temperature_adjust rainfall_adjust"""
        Biome.__init__(self, data)

    def GetAdjustTemperature(self):
        # type: () -> float
        return self._GetField('temperature_adjust')

    def GetAdjustRainfall(self):
        # type: () -> float
        return self._GetField('rainfall_adjust')
    
    def __str__(self):
        return "=================\n生态: {0} ({1})\n温度: {2}\n湿度: {3}\n=================".format(self.biomeName, self.GetCNName(), self.GetAdjustTemperature(), self.GetAdjustRainfall())