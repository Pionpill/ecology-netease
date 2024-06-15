class BiomeTag(object):
    FOREST = 'forest'
    BEE_HABITAT = 'bee_habitat'
    COLD = 'cold'
    TAIGA = 'taiga'
    OCEAN = 'ocean'
    HILLS = 'hills'
    EXTREME_HILLS = 'extreme_hills'
    BIRCH = 'birch'
    MESA = 'mesa'
    PLATEAU = 'plateau'
    FROZEN = 'frozen'
    RIVER = 'river'
    EDGE = 'edge'
    CAVES = 'caves'
    RARE = 'rare'
    BEACH = 'beach'
    ICE_PLAINS = 'ice_plains'
    DESERT = 'desert'
    JUNGLE = 'jungle'
    MUSHROOM_LAND = 'mushroom_land'
    WARM = 'warm'
    MUTATED = 'mutated'
    BAMBOO = 'bamboo'
    MOUNTAINS = 'mountains'
    MOUNTAIN = 'mountain'
    MEGA = 'mega'
    GROVE = 'grove'
    LUSH_CAVES = 'lush_caves'
    STONE = 'stone'
    BASALT_DELTAS = 'basalt_deltas'
    FLOWER_FOREST = 'flower_forest'
    NETHERWART_FOREST = 'netherwart_forest'
    ICE = 'ice'
    LUKEWARM = 'lukewram'
    NO_LEGACY_WORLDGEB = 'no_legacy_worldgen'
    ROOFED = 'roofed'
    PLAINS = 'plains'
    DEEP = 'deep'
    DESSERT = 'dessert'
    FROZEN_PEAKS = 'frozen_peaks'
    DRIPSTONE_CAVES= 'dripstone_caves'
    SHORE = 'shore'
    SAVANNA = 'savanna'

    cnNameDict = {
        FOREST: '森林',
        BEE_HABITAT: '蜜蜂',
        COLD: '寒带',
        TAIGA: '针叶林',
        OCEAN: '海洋',
        HILLS: '山区',
        EXTREME_HILLS: '极端山区',
        BIRCH: '桦木林',
        MESA: '恶地',
        PLATEAU: '高原',
        FROZEN: '冰封',
        RIVER: '河流',
        EDGE: '边缘',
        CAVES: '洞穴',
        RARE: '稀有',
        BEACH: '海滩',
        ICE_PLAINS: '冰封高原',
        DESERT: '沙漠',
        JUNGLE: '热带雨林',
        MUSHROOM_LAND: '恶魔岛',
        WARM: '温带',
        MUTATED: '变种',
        BAMBOO: '竹林',
        MOUNTAINS: '高山',
        MOUNTAIN: '高山',
        MEGA: '巨型',
        GROVE: '雪林',
        LUSH_CAVES: '繁茂洞穴',
        STONE: '石林',
        BASALT_DELTAS: '玄武岩三角洲',
        FLOWER_FOREST: '繁花森林',
        NETHERWART_FOREST: '地狱疣森林',
        ICE: '冰',
        LUKEWARM: '温水',
        NO_LEGACY_WORLDGEB: '',
        ROOFED: '黑森林',
        PLAINS: '平原',
        DEEP: '森',
        FROZEN_PEAKS: '冰封山峰',
        DRIPSTONE_CAVES: '溶洞',
        SHORE: '岸边',
        SAVANNA: '沼泽',
    }

    @staticmethod
    def GetChinese(quality):
        return BiomeTag.cnNameDict.get(quality) or '未知标签'