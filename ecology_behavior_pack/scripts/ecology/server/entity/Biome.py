import mod.server.extraServerApi as serverApi
from scripts.common import logger

levelId = serverApi.GetLevelId()
engineCompFactory = serverApi.GetEngineCompFactory()
biomeComp = engineCompFactory.CreateBiome(levelId)

BIOME_CN_NAME_DICT = {
    "deep_lukewarm_ocean": "温水深海",
    "ice_mountains": "雪山",
    "swampland": "沼泽",
    "warm_ocean": "暖水海洋",
    "frozen_river": "冻河",
    "extreme_hills_edge": "山地边缘",
    "desert": "沙漠",
    "extreme_hills": "山地",
    "forest": "森林",
    "the_end": "末地",
    "hell": "下界荒地",
    "plains": "平原",
    "beach": "沙滩",
    "jungle": "丛林",
    "cold_beach": "积雪的沙滩",
    "jungle_edge": "丛林边缘",
    "stone_beach": "石岸",
    "cold_ocean": "冷水海洋",
    "savanna": "热带草原",
    "birch_forest": "桦木森林",
    "birch_forest_hills": "桦木森林丘陵",
    "cold_taiga": "积雪的针叶林",
    "mega_taiga": "巨型针叶林",
    "mega_taiga_hills": "巨型针叶林丘陵",
    "extreme_hills_plus_trees": "繁茂的山地",
    "jungle_hills": "丛林丘陵",
    "savanna_plateau": "热带高原",
    "bamboo_jungle": "竹林",
    "bamboo_jungle_hills": "竹林丘陵",
    "mesa_plateau": "恶地高原",
    "taiga_hills": "针叶林丘陵",
    "frozen_ocean": "冻洋",
    "ocean": "海洋",
    "mushroom_island": "蘑菇岛",
    "ice_plains": "积雪的冻原",
    "taiga": "针叶林",
    "desert_mutated": "沙漠湖泊",
    "extreme_hills_mutated": "沙砾山地",
    "taiga_mutated": "针叶林山地",
    "swampland_mutated": "沼泽山丘",
    "jungle_edge_mutated": "丛林边缘变种",
    "birch_forest_hills_mutated": "高大桦木丘陵",
    "roofed_forest_mutated": "黑森林丘陵",
    "legacy_frozen_ocean": "遗产冻洋",
    "river": "河流",
    "roofed_forest": "黑森林",
    "mesa": "恶地",
    "desert_hills": "沙漠丘陵",
    "extreme_hills_plus_trees_mutated": "沙砾山地+",
    "savanna_mutated": "破碎的热带草原",
    "savanna_plateau_mutated": "破碎的热带高原",
    "meadow": "草甸",
    "dripstone_caves": "溶洞",
    "lush_caves": "繁茂洞穴",
    "stony_peaks": "裸岩山峰",
    "snowy_slopes": "积雪的山坡",
    "frozen_peaks": "冰封山峰",
    "soulsand_valley": "灵魂沙峡谷",
    "crimson_forest": "绯红森林",
    "warped_forest": "诡异森林",
    "flower_forest": "繁花森林",
    "basalt_deltas": "玄武岩三角洲",
    "deep_ocean": "深海",
    "deep_warm_ocean": "暖水深海",
    "lukewarm_ocean": "温水海洋",
    "deep_cold_ocean": "冷水深海",
    "deep_frozen_ocean": "封冻深海",
    "mushroom_island_shore": "蘑菇岛岸",
    "forest_hills": "繁茂的丘陵",
    "cold_taiga_hills": "积雪的针叶林丘陵",
    "ice_plains_spikes": "冰刺平原",
    "mesa_plateau_stone": "繁茂的恶地高原",
    "sunflower_plains": "向日葵平原",
    "jungle_mutated": "丛林变种",
    "birch_forest_mutated": "高大桦木森林",
    "cold_taiga_mutated": "积雪的针叶林山地",
    "redwood_taiga_mutated": "巨型云杉针叶林",
    "redwood_taiga_hills_mutated": "巨型云杉针叶林丘陵",
    "mesa_bryce": "被风蚀的恶地",
    "mesa_plateau_stone_mutated": "繁茂的恶地高原变种",
    "mesa_plateau_mutated": "恶地高原变种",
    "jagged_peaks": "尖峭山峰",
    "grove": "雪林",
    "deep_dark": "黑暗之域",
    "mangrove_swamp": "红树林沼泽",
    "cherry_grove": "樱花树林",
    "overworld": "主世界"
}

class Biome():
    cacheMap = {} # type: dict[str, Biome]

    def __init__(self, biomeName):
        # type: (str) -> None
        self._biomeName = biomeName
        biome = biomeComp.GetBiomeInfo(biomeName)
        if biome is None:
            logger.warn("没有 {0} 对应的生态数据，使用平原生态代替，这可能是兼容性问题或程序 bug，请报告给开发者群：712936357")
            biome = biomeComp.GetBiomeInfo("plains")
        self._biome = biome

    def GetBiomeName(self):
        # type: () -> str
        return self._biomeName
    
    def GetBiomeCnName(self):
        # type: () -> str
        return BIOME_CN_NAME_DICT.get(self._biomeName, self._biomeName)

    def IsRain(self):
        # type: () -> bool
        return self._biome["isRain"]
    
    def GetSnowAccumulation(self):
        # type: () -> tuple[float, float]
        return self._biome["snow_accumulation"]
    
    def GetTemperature(self):
        """单位：摄氏度"""
        # type: () -> float
        return self._biome["temperature"] * 20
    
    def GetRainfall(self):
        # type: () -> float
        """单位：百分之"""
        return self._biome["downfall"] * 100
    
    def CanSnow(self):
        # type: () -> bool
        """判断是否降雪"""
        return self._biome["temperature"] <= 0.15
    
    @staticmethod
    def FromBiomeName(biomeName):
        """获取生态实例，单例模式"""
        biome = Biome.cacheMap.get(biomeName)
        if biome is not None:
            return biome
        biome = Biome(biomeName)
        Biome.cacheMap[biomeName] = biome
        return biome