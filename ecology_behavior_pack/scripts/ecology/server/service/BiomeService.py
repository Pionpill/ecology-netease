import time
import mod.server.extraServerApi as serverApi

from scripts.ecology.server.entity.Ecology import DynamicEcology
from scripts.ecology.server.manager import EcologyManager
from scripts.common import logger
from scripts.common.entity import Biome
    
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

    ecologyMgrDict = {} # type: dict[tuple[int, int, int, int], tuple[EcologyManager, int]]

    @staticmethod
    def GetEcologyManager(position, dimensionId):
        # type: (tuple[int, int, int], int) -> EcologyManager
        posKey = position + (dimensionId,)
        ecologyMgrTuple = BiomeService.ecologyMgrDict.get(posKey)
        if ecologyMgrTuple is not None:
            BiomeService.ecologyMgrDict[posKey] = (ecologyMgrTuple[0], int(time.time()))
            BiomeService.__RefreshEcologyMgrDict()
            return ecologyMgrTuple[0]
        ecologyManager = EcologyManager(position, dimensionId)
        BiomeService.ecologyMgrDict[posKey] = (ecologyManager, int(time.time()))
        return ecologyManager
    
    @staticmethod
    def __RefreshEcologyMgrDict():
        """⚡刷新生态管理表"""
        for posKey, ecologyMgrTuple in BiomeService.ecologyMgrDict.items():
            now = int(time.time())
            lastGetTime = ecologyMgrTuple[1]
            # 超过 10 分钟就删除管理类
            if now - lastGetTime > 600 and BiomeService.ecologyMgrDict[posKey]:
                del BiomeService.ecologyMgrDict[posKey]

    @staticmethod
    def GetBiomeInfo(position, dimensionId):
        # type: (tuple[int, int, int], int) -> Biome
        biomeManager = BiomeService.GetEcologyManager(position, dimensionId)
        return biomeManager.GetBiomeInfo()
    
    @staticmethod
    def GetDynamicEcologyInfo(position, dimensionId):
        # type: (tuple[int, int, int], int) -> DynamicEcology
        """获取动态生态信息"""
        biomeManager = BiomeService.GetEcologyManager(position, dimensionId)
        return biomeManager.GetDynamicEcology()
