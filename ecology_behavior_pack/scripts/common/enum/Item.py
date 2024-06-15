from scripts.common.enum import FormatColor


class ItemCategory(object):
    CROPS = 'crops'

    cnNameDict = {
        CROPS: '作物',
    }

    @staticmethod
    def GetChinese(quality):
        return ItemCategory.cnNameDict.get(quality) or '未知分类'

class ItemTag(object):
    CROP = 'crop' # 粮食
    VEGETABLE = 'vegetable' # 蔬菜
    FUNGI = 'fungi' # 菌类
    SEASONING = 'seasoning' # 调料
    CEREAL = 'cereal' # 谷物
    SOLANUM = 'solanum' # 茄属
    CAPSICUM = 'capsicum' # 辣椒属
    GREEN = 'green' # 青菜
    ALLIUM = 'allium' # 葱属
    WATER = 'water' # 水生

    cnNameDict = {
        CROP: '粮食',
        VEGETABLE: '蔬菜',
        FUNGI: '菌类',
        SEASONING: '调料',
        CEREAL: '谷物',
        SOLANUM: '茄属',
        CAPSICUM: '辣椒属',
        GREEN: '青菜',
        ALLIUM: '葱属',
        WATER: '水生',
    }

    @staticmethod
    def GetChinese(quality):
        return ItemTag.cnNameDict.get(quality) or '未知标签'

class ItemSource(object):
    BLOCK = 'block' # 方块掉落
    CROP = 'crop' # 植株
    WORKBENCH = 'workbench' # 工作台合成
    WILD = 'wild' # 野生

    cnNameDict = {
        BLOCK: '方块',
        CROP: '植株',
        WORKBENCH: '工作台',
        WILD: '野生',
    }

    @staticmethod
    def GetChinese(quality):
        return ItemSource.cnNameDict.get(quality) or '未知来源'

class FoodSaturation(object):
    POOR = 'poor' # 0.2
    LOW = 'low' # 0.6
    NORMAL = 'normal' # 1.2
    GOOD = 'good' # 1.6
    MAX = 'max' # 2.0
    SUPERNATURAL = 'supernatural' # 2.4

    cnNameDict = {
        POOR: '贫瘠',
        LOW: '低',
        NORMAL: '一般',
        GOOD: '好',
        MAX: '极佳',
        SUPERNATURAL: '超自然',
    }

    @staticmethod
    def GetChinese(quality):
        return FoodSaturation.cnNameDict.get(quality) or '未知来源'

class ItemQuality(object):
    COMMON = 1 # 常见
    UNCOMMON = 2 # 少见
    RARE = 3 # 稀有
    EPIC = 4 # 史诗
    LEGENDARY = 5 # 传奇
    UNKNOWN = 10 # 未知
    DANGER = 11 # 危险

    formatColorDict = {
        COMMON: FormatColor.WHITE,
        UNCOMMON: FormatColor.YELLOW,
        RARE: FormatColor.AQUA,
        EPIC: FormatColor.LIGHT_PURPLE,
        LEGENDARY: FormatColor.GOLD,
        UNKNOWN: FormatColor.GREY,
        DANGER: FormatColor.RED
    }

    cnNameDict = {
        COMMON: '常见',
        UNCOMMON: '少见',
        RARE: '稀有',
        EPIC: '史诗',
        LEGENDARY: '传奇',
        UNKNOWN: '未知',
        DANGER: '危险'
    }

    @staticmethod
    def GetFormatColor(quality):
        return ItemQuality.formatColorDict.get(quality) or FormatColor.WHITE

    @staticmethod
    def GetChinese(quality):
        return ItemQuality.cnNameDict.get(quality) or '常见'