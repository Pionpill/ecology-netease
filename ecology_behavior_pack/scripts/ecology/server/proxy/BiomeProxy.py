import mod.server.extraServerApi as serverApi
from scripts.common.utils import positionUtils
from scripts.ecology.server.data import BIOME_DATA
from scripts.ecology.server.entity import Biome
    
levelId = serverApi.GetLevelId()
biomeComp = serverApi.GetEngineCompFactory().CreateBiome(levelId)
weatherComp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
blockStateComp = serverApi.GetEngineCompFactory().CreateBlockState(levelId)

class BiomeProxy(object):
    """
    生态代理类
    通过位置信息获取生态的固定信息
    """
    def __init__(self, position, dimensionId):
        # type: (tuple[int, int, int], int) -> None
        object.__init__(self)
        self.position = position
        self.dimensionId = dimensionId
        biomeName = biomeComp.GetBiomeName(position, dimensionId)
        biomeInfo = self.__GetBlockBiomeInfo(biomeName)
        self.biome = Biome.FromData(biomeInfo, biomeName)

    def GetBiomeInfo(self):
        # type: () -> Biome
        """获取某一位置生态的基础信息，这些信息是永远不变的"""
        basicBiomeName = self.biome.name
        neighborBiomes = self.__GetNeighborBiomeName(16)
        neighborBiomes[basicBiomeName] = 1 if basicBiomeName not in neighborBiomes else neighborBiomes[basicBiomeName] + 1
        # 如果 16 格内存在不同的生态，延伸至 32 格并扩大数据集
        if len(neighborBiomes) != 1:
            farNeighborBiomes = self.__GetNeighborBiomeName(32, True)
            for biomeName in farNeighborBiomes:
                neighborBiomes[biomeName] = 1 if (biomeName not in neighborBiomes and biomeName not in farNeighborBiomes) else neighborBiomes.get(biomeName, 0) + farNeighborBiomes.get(biomeName, 0)
        return self.__GetAvgBiomeInfo(neighborBiomes)
    
    def __GetAvgBiomeInfo(self, neighborBiomes):
        # type: (dict[str, int]) -> Biome
        """多个群落计算一些属性均值，主要是温度和降水"""
        temperatureSum = 0
        rainfallSum = 0
        biomeCount = 0
        for biomeName in neighborBiomes:
            biomeInfo = self.__GetBlockBiomeInfo(biomeName)
            temperatureSum += biomeInfo.get("temperature") * neighborBiomes[biomeName]
            rainfallSum += biomeInfo.get("rainfall") * neighborBiomes[biomeName]
            biomeCount += neighborBiomes[biomeName]

        biomeData = {
            "name": self.biome.name,
            "name_cn": self.biome.name_cn,
            "temperature": temperatureSum / biomeCount,
            "rainfall": rainfallSum / biomeCount,
            "tags": self.biome.tags,
        }
        return Biome.FromData(biomeData)
    
    def __GetNeighborBiomeName(self, distance, detail = False):
        # type: (int, bool) -> dict[str, int]
        """
        获取附近 distance 距离的群系名称
        detail 为 False 仅获取点, 为 True 获取点与顶点
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

    def __GetBlockBiomeInfo(self, biomeName):
        # type (str) -> dict[str, any]
        """获取生态信息，默认采用主世界生态"""
        if (biomeName in BIOME_DATA):
            return BIOME_DATA.get(biomeName)
        if (self.dimensionId == 1):
            return BIOME_DATA.get("hell")
        if (self.dimensionId == 2):
            return BIOME_DATA.get("the_end")
        return BIOME_DATA.get("overworld")