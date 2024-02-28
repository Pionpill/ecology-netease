import math
import random
import mod.server.extraServerApi as serverApi

from scripts.common import logger
from scripts.common.params import EcologyInfo
from scripts.common.utils import positionUtils
from scripts.ecology.server.service import TimeService
from scripts.ecology.server.entity import Biome
from scripts.ecology.server.proxy import BiomeProxy
    
levelId = serverApi.GetLevelId()
biomeComp = serverApi.GetEngineCompFactory().CreateBiome(levelId)
weatherComp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
blockStateComp = serverApi.GetEngineCompFactory().CreateBlockState(levelId)
blockInfoComp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)


class BiomeService(object):
    # 温度偏移帧，将每日最低温设置在早上 7 时，最高温设置在，下午 1 时
    TEMPERATURE_ADJUST_FRAME = 1000
    # 每日温度变化量，白天热，晚上凉
    TEMPERATURE_RANGE_DAY = 10
    # MC 生存模式中间高度
    MIDDLE_HEIGHT = 128

    @staticmethod
    def GetBiomeInfo(position, dimensionId):
        # type: (tuple[int, int, int], int) -> Biome
        return BiomeProxy(position, dimensionId).GetBiomeInfo()
    
    @staticmethod
    def GetEcologyInfo(position, dimensionId, biomeInfo = None):
        # type: (tuple[int, int, int], int, Biome) -> EcologyInfo
        """获取生态信息，在生物群系基础上做出了一些调整"""
        if biomeInfo is None:
            biomeInfo = BiomeService.GetBiomeInfo(position, dimensionId)
            
        temperature_adjust_day = BiomeService.__GetDayAdjustTemperature(dimensionId)
        temperature_adjust_weather = BiomeService.__GetWeatherAdjustTemperature()
        temperature_adjust_altitude = BiomeService.__GetAltitudeAdjustTemperature(position[1])
        temperature_adjust_random = BiomeService.__GetRandomAdjustTemperature()
        temperature_adjust = int(biomeInfo.temperature + temperature_adjust_day + temperature_adjust_weather + temperature_adjust_altitude + temperature_adjust_random)
        rainfall_adjust = BiomeService.__GetRainfallAdjust(position, dimensionId)
        if (not rainfall_adjust) or rainfall_adjust < biomeInfo.rainfall:
            rainfall_adjust = biomeInfo.rainfall
            
        return EcologyInfo(biomeInfo.name, biomeInfo.name_cn, biomeInfo.temperature, temperature_adjust, rainfall_adjust, biomeInfo.tags)
        
    @staticmethod
    def __GetDayAdjustTemperature(dimensionId):
        # type: (int) -> float
        """根据当前时间获取温度偏移量，晚上冷，中午热"""
        # FIXME MC启动器将 TimeService 被误识别为 module
        dayFrame = TimeService.TimeService.GetDayFrame(dimensionId)
        sinValue = math.sin((2 * math.pi) *  ((dayFrame + BiomeService.TEMPERATURE_ADJUST_FRAME) / float(TimeService.TimeService.FRAME_PER_MC_DAY)))
        return BiomeService.TEMPERATURE_RANGE_DAY * sinValue
    
    @staticmethod
    def __GetWeatherAdjustTemperature():
        # type: () -> float
        """根据天气获取温度偏移量，目前仅下雨降温"""
        return -5 if weatherComp.IsRaining() else 0
        
    @staticmethod
    def __GetAltitudeAdjustTemperature(altitude):
        # type: (int) -> float
        """根据海拔获取温度偏移量，海拔每偏移1，温度上升0.1"""
        return (BiomeService.MIDDLE_HEIGHT - altitude) * 0.05
    
    @staticmethod
    def __GetRandomAdjustTemperature():
        # type: () -> float
        """温度随机偏移"""
        return 3 * random.uniform(-1, 1)
    
    @staticmethod
    def __GetRainfallAdjust(position, dimensionId):
        # type: (tuple[int, int, int], int) -> float | None
        """获取湿度"""
        belowPosition = positionUtils.GetBelowPosition(position)
        blockState = blockStateComp.GetBlockStates(belowPosition, dimensionId)
        if blockState.get("name") == 'minecraft:farmland' and blockState.get("axu") == 1:   
            # TODO 判断湿润土壤，则返回 0.8
            return 0.8
        return None