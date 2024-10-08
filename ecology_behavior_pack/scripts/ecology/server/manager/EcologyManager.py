import math
import random
from collections import Counter

import mod.server.extraServerApi as serverApi

from scripts.ecology.server.service.FrameService import FrameService
from scripts.common import logger
from scripts.common.utils import positionUtils
from scripts.ecology.server.entity import Biome, DynamicEcology, FixedEcology

levelId = serverApi.GetLevelId()
gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
engineCompFactory = serverApi.GetEngineCompFactory()
biomeComp = engineCompFactory.CreateBiome(levelId)
blockInfoComp = engineCompFactory.CreateBlockInfo(levelId)
weatherComp = engineCompFactory.CreateWeather(levelId)
blockStateComp = engineCompFactory.CreateBlockInfo(levelId)

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
        self.__biomeName = biomeComp.GetBiomeName(position, dimensionId)
        self.__biome = Biome.FromBiomeName(self.__biomeName)
        self.__position = position
        self.__dimensionId = dimensionId
        self.__fixedEcologyInfo = self.__GetFixedEcologyInfo()

    def GetBiomeInfo(self):
        """获取生物群系信息"""
        return self.__biome

    def GetDynamicEcology(self):
        """获取动态生态信息"""
        adjustTemperature = self.__fixedEcologyInfo.GetAvgTemperature() + self.__CalculateAdjustTemperature()
        adjustRainfall = max(self.__fixedEcologyInfo.GetAvgRainfall(), self.__CalculateAdjustRainfall())
        data = {
            'temperature_adjust': adjustTemperature,
            'rainfall_adjust': adjustRainfall
        }
        return DynamicEcology(self.__biomeName, data)

    def __GetFixedEcologyInfo(self):
        """获取静态生态信息"""
        avgTemperature, avgRainfall = self.__ExpandAndCalculateMeanBiomeInfo()
        data = {
            'temperature_avg': avgTemperature,
            'rainfall_avg': avgRainfall
        }
        fixedEcology = FixedEcology(self.__biomeName, data)
        return fixedEcology

    def __ExpandAndCalculateMeanBiomeInfo(self):
        """⚡差异扩展均值算法"""
        neighborBiomes = self.__GetNeighborBiomeName(16, True)
        neighborBiomes[self.__biomeName] = 1 if self.__biomeName not in neighborBiomes else neighborBiomes[self.__biomeName] + 1
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
        altitudeAdjust = self.__GetAdjustTemperatureOfAltitude()
        DayAdjust = self.__GetAdjustTemperatureOfDay()
        WeatherAdjust = self.__GetAdjustTemperatureOfWeather()
        RandomAdjust = self.__GetAdjustTemperatureOfRandom()
        return altitudeAdjust + DayAdjust + WeatherAdjust + RandomAdjust
    
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
            neighborPosArray = positionUtils.GetNearbyPosition(self.__position, distance, 'cube', 'point')
        else:
            pointNeighborArray = positionUtils.GetNearbyPosition(self.__position, distance, 'cube', 'point')
            vertexNeighborArray = positionUtils.GetNearbyPosition(self.__position, distance, 'cube', 'vertex')
            neighborPosArray = pointNeighborArray + vertexNeighborArray
        biomeMap = {}
        for neighborPos in neighborPosArray:
            biomeName = biomeComp.GetBiomeName(neighborPos, self.__dimensionId)
            biomeMap[biomeName] = 1 if biomeName not in biomeMap else biomeMap[biomeName] + 1
        return biomeMap

    def __GetAdjustTemperatureOfDay(self):
        """根据当前时间获取温度偏移量，晚上冷，中午热"""
        dayFrame = FrameService.GetDayFrame(self.__dimensionId)
        sinValue = math.sin((2 * math.pi) *  ((dayFrame + TEMPERATURE_ADJUST_FRAME) / float(FrameService.FRAME_PER_MC_DAY)))
        return TEMPERATURE_RANGE_DAY * sinValue
    
    def __GetAdjustTemperatureOfWeather(self):
        """根据天气获取温度偏移量，目前仅下雨降温"""
        return -5 if weatherComp.IsRaining() else 0
    
    def __GetAdjustTemperatureOfAltitude(self):
        """根据海拔获取温度偏移量，海拔每偏移1，温度上升0.05"""
        return (MIDDLE_HEIGHT - self.__position[1]) * 0.05

    def __GetAdjustTemperatureOfRandom(self):
        """
        温度随机偏移
        TODO 统一到风力计算中
        """
        return 2 * random.uniform(-1, 1)
    
    def __GetAdjustRainfallOfLand(self):
        """根据底部方块获取湿度"""
        belowPosition = positionUtils.GetBelowPosition(self.__position)
        blockState = blockStateComp.GetBlockNew(belowPosition, self.__dimensionId)
        if blockState is None:
            return 0
        aux = blockState.get("aux") or 0
        if blockState.get("name") == 'minecraft:farmland' and aux > 1:
            return 60
        return 0
    
    def __GetAdjustRainfallOfWeather(self):
        """根据天气获取湿度"""
        return 0.8 if weatherComp.IsRaining() else 0