import math
import random
from collections import Counter

import mod.server.extraServerApi as serverApi

from scripts.ecology.server.service import FrameService
from scripts.common import logger
from scripts.common.utils import positionUtils
from scripts.common.entity import Biome, GetBiome
from scripts.ecology.server.entity import DynamicEcology, FixedEcology

levelId = serverApi.GetLevelId()
engineCompFactory = serverApi.GetEngineCompFactory()
biomeComp = engineCompFactory.CreateBiome(levelId)
blockInfoComp = engineCompFactory.CreateBlockInfo(levelId)
weatherComp = engineCompFactory.CreateWeather(levelId)
blockStateComp = engineCompFactory.CreateBlockState(levelId)

# 温度偏移帧，将每日最低温设置在早上 7 时，最高温设置在，下午 1 时
TEMPERATURE_ADJUST_FRAME = 1000
# 每日温度变化量，白天热，晚上凉
TEMPERATURE_RANGE_DAY = 10
# MC 生存模式中间高度
MIDDLE_HEIGHT = 128

class EcologyManager(object):
    """生态类管理类"""
    def __init__(self, position, dimensionId):
        # type: (tuple[int, int, int], int) -> None
        object.__init__(self)
        self.biomeName = biomeComp.GetBiomeName(position, dimensionId)
        biome = GetBiome(self.biomeName)
        if biome is None:
            logger.error('未查找到 {} 相关的数据，这是一个程序 bug，请报告给开发者群：712936357'.format(self.biomeName))
            return
        self.biome = biome
        self.position = position
        self.dimensionId = dimensionId
        self.adjustTemperatureOfAltitude = self.__GetAdjustTemperatureOfAltitude()
        self.fixedEcologyInfo = self.__GetFixedEcologyInfo()

    def GetBiomeInfo(self):
        """获取生物群系信息"""
        return self.biome
    
    def GetDynamicEcology(self):
        """获取动态生态信息"""
        adjustTemperature = self.fixedEcologyInfo.GetAvgTemperature() + self.__CalculateAdjustTemperature()
        adjustRainfall = max(self.fixedEcologyInfo.GetAvgRainfall(), self.__CalculateAdjustRainfall())
        data = {
            'name': self.biomeName,
            'name_cn': self.biome.GetCNName(),
            'temperature': self.biome.GetTemperature(),
            'temperature_adjust': adjustTemperature,
            'rainfall': self.biome.GetRainfall(),
            'rainfall_adjust': adjustRainfall,
            'tags': self.biome.GetTags()
        }
        return DynamicEcology(data)

    def __GetFixedEcologyInfo(self):
        """获取静态生态信息"""
        avgTemperature, avgRainfall = self.__ExpandAndCalculateMeanBiomeInfo()
        data = {
            'name': self.biomeName,
            'name_cn': self.biome.GetCNName(),
            'temperature': self.biome.GetTemperature(),
            'temperature_avg': avgTemperature,
            'rainfall': self.biome.GetRainfall(),
            'rainfall_avg': avgRainfall,
            'tags': self.biome.GetTags()
        }
        fixedEcology = FixedEcology(data)
        self.fixedEcologyInfo = fixedEcology
        return fixedEcology

    def __ExpandAndCalculateMeanBiomeInfo(self):
        """差异扩展均值算法"""
        neighborBiomes = self.__GetNeighborBiomeName(16, True)
        neighborBiomes[self.biomeName] = 1 if self.biomeName not in neighborBiomes else neighborBiomes[self.biomeName] + 1
        avgTuple = (0, 0) # type: tuple[float, float]
        if len(neighborBiomes) == 1:
            avgTuple = self.__GetAvgBiomeInfo(neighborBiomes)
        farNeighborBiomes = self.__GetNeighborBiomeName(32, True)
        nearCounter = Counter(neighborBiomes)
        farCounter = Counter(farNeighborBiomes)
        counter = nearCounter + farCounter
        avgTuple = self.__GetAvgBiomeInfo(dict(counter))
        return avgTuple

    def __CalculateAdjustTemperature(self):
        """获取调整温度: 相加"""
        # self.adjustTemperatureOfAltitude
        DayAdjust = self.__GetAdjustTemperatureOfDay()
        WeatherAdjust = self.__GetAdjustTemperatureOfWeather()
        RandomAdjust = self.__GetAdjustTemperatureOfRandom()
        return self.adjustTemperatureOfAltitude + DayAdjust + WeatherAdjust + RandomAdjust
    
    def __CalculateAdjustRainfall(self):
        """获取调整温度: 取最大值"""
        landAdjust = self.__GetAdjustRainfallOfLand()
        weatherAdjust = self.__GetAdjustRainfallOfWeather()
        return float(max(landAdjust, weatherAdjust))


    def __GetAvgBiomeInfo(self, biomesDict):
        # type: (dict[str, int]) -> tuple[float, float]
        """多个群落计算一些属性均值，主要是温度和降水"""
        temperatureSum = 0.0
        rainfallSum = 0.0
        biomeCount = 0
        for biomeName, count in biomesDict.items():
            biome = Biome.FromBiomeName(biomeName)
            temperatureSum += biome.GetTemperature() * count
            rainfallSum += biome.GetRainfall() * count
            biomeCount += count
        return (temperatureSum / biomeCount,  rainfallSum / biomeCount)

    def __GetNeighborBiomeName(self, distance, detail = False):
        # type: (int, bool) -> dict[str, int]
        """
        获取附近 distance 距离的群系名称

        :param key: distance 距离
        :param detail: distance 为 True 获取点与顶点，False 仅获得平面点
        返回字段，key: 生态名 value: 个数
        """
        neighborPosArray = None
        if (detail == False):
            neighborPosArray = positionUtils.GetNearbyPosition(self.position, distance, 'cube', 'point')
        else:
            pointNeighborArray = positionUtils.GetNearbyPosition(self.position, distance, 'cube', 'point')
            vertexNeighborArray = positionUtils.GetNearbyPosition(self.position, distance, 'cube', 'vertex')
            neighborPosArray = pointNeighborArray + vertexNeighborArray
        biomeMap = {}
        for neighborPos in neighborPosArray:
            biomeName = biomeComp.GetBiomeName(neighborPos, self.dimensionId)
            biomeMap[biomeName] = 1 if biomeName not in biomeMap else biomeMap[biomeName] + 1
        return biomeMap

    def __GetAdjustTemperatureOfDay(self):
        """根据当前时间获取温度偏移量，晚上冷，中午热"""
        # FIXME 编译器bug，需要深入一层
        dayFrame = FrameService.FrameService.GetDayFrame(self.dimensionId)
        sinValue = math.sin((2 * math.pi) *  ((dayFrame + TEMPERATURE_ADJUST_FRAME) / float(FrameService.FrameService.FRAME_PER_MC_DAY)))
        return TEMPERATURE_RANGE_DAY * sinValue
    
    def __GetAdjustTemperatureOfWeather(self):
        """根据天气获取温度偏移量，目前仅下雨降温"""
        return -5 if weatherComp.IsRaining() else 0
    
    def __GetAdjustTemperatureOfAltitude(self):
        """根据海拔获取温度偏移量，海拔每偏移1，温度上升0.1"""
        return (MIDDLE_HEIGHT - self.position[1]) * 0.05

    def __GetAdjustTemperatureOfRandom(self):
        """温度随机偏移"""
        return 2 * random.uniform(-1, 1)
    
    def __GetAdjustRainfallOfLand(self):
        """根据底部方块获取湿度"""
        belowPosition = positionUtils.GetBelowPosition(self.position)
        blockState = blockStateComp.GetBlockStates(belowPosition, self.dimensionId)
        if blockState.get("name") == 'minecraft:farmland' and blockState.get("axu") == 1:
            return 0.6
        return 0
    
    def __GetAdjustRainfallOfWeather(self):
        """根据天气获取湿度"""
        return 0.8 if weatherComp.IsRaining() else 0