from scripts.ecology.server.entity import Biome
from scripts.common import logger

class FixedEcology():
    """静态生态数据"""
    def __init__(self, biomeName, data):
        # type: (str, dict) -> None
        """静态生态数据，仅包含位置相关的信息"""
        self.__biome = Biome.FromBiomeName(biomeName)
        self.__data = data

    def GetBiome(self):
        # type: () -> Biome
        return self.__biome

    def GetAvgTemperature(self):
        # type: () -> float
        return self.__data["temperature_avg"]

    def GetAvgRainfall(self):
        # type: () -> float
        return self.__data["rainfall_avg"]

    def __str__(self):
        return "固定生态: {0}\n温度: {1}℃\n湿度: {2}％".format(self.__biome.GetBiomeCnName(), round(self.GetAvgTemperature(),2), round(self.GetAvgRainfall(),2))

class DynamicEcology():
    """动态生态数据"""
    def __init__(self, biomeName, data):
        # type: (str, dict) -> None
        """动态生态数据，即当前时间生态信息"""
        self.__biome = Biome.FromBiomeName(biomeName)
        self.__data = data

    def GetBiome(self):
        # type: () -> Biome
        return self.__biome

    def GetAdjustTemperature(self):
        # type: () -> float
        return self.__data["temperature_adjust"]

    def GetAdjustRainfall(self):
        # type: () -> float
        return self.__data["rainfall_adjust"]
    
    def __str__(self):
        return "生态: {0}\n温度: {1}℃\n湿度: {2}％".format(self.__biome.GetBiomeCnName(), round(self.GetAdjustTemperature(),2), round(self.GetAdjustRainfall(), 2))