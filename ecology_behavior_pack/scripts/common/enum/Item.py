from scripts.common.enum import FormatColor


class ItemCategory(object):
    CROPS = 'crops'

class ItemTag(object):
    CROP = 'crop', # 粮食
    VEGETABLE = 'vegetable', # 蔬菜
    FUNGI = 'fungi', # 菌类
    SEASONING = 'seasoning', # 调料
    CEREAL = 'cereal', # 谷物
    SOLANUM = 'solanum', # 茄属
    CAPSICUM = 'capsicum', # 辣椒属
    GREEN = 'green', # 青菜
    ALLIUM = 'allium' # 葱属
    WATER = 'water' # 水生

class ItemSource(object):
    BLOCK = 'block', # 方块掉落
    WORKBENCH = 'workbench', # 工作台合成

class FoodSaturation(object):
    POOR = 'poor',
    LOW = 'low',
    NORMAL = 'normal',
    GOOD = 'good',
    MAX = 'max',
    SUPERNATURAL = 'supernatural'

class ItemQuality(object):
    COMMON = 1, # 常见
    UNCOMMON = 2, # 少见
    RARE = 3, # 稀有
    EPIC = 4, # 史诗
    LEGENDARY = 5, # 传奇
    UNKNOWN = 10, # 未知
    DANGER = 11, # 危险

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