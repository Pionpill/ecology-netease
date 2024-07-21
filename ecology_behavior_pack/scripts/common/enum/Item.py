from scripts.common.enum import FormatColor


class ItemCategory(object):
    CROPS = 'crops'
    MATERIAL = 'material'
    FOOD = 'food'

    cnNameDict = {
        CROPS: '作物',
        MATERIAL: '材料',
        FOOD: '食物',
    }

    @staticmethod
    def GetChinese(quality):
        return ItemCategory.cnNameDict.get(quality) or '未知分类'

class ItemTag(object):
    CROP = 'crop' # 粮食
    VEGETABLE = 'vegetable' # 蔬菜
    FRUIT = 'fruit' # 水果
    FUNGI = 'fungi' # 菌类
    SPICES = 'spices' # 香料
    SEASONING = 'seasoning' # 调料
    CEREAL = 'cereal' # 谷物
    SOLANUM = 'solanum' # 茄属
    CAPSICUM = 'capsicum' # 辣椒属
    GREEN = 'green' # 青菜
    ALLIUM = 'allium' # 葱属
    WATER = 'water' # 水生
    ORE = 'ore' # 矿物质
    PRODUCT = 'product' # 农产品
    DAIRY = 'dairy' # 乳制品
    OIL = 'oil' # 油
    SOY = 'soy' # 黄豆制品
    BEAN = 'bean' # 豆制品
    WHEAT = 'wheat' # 小麦制品
    PORK = 'pork' # 猪肉制品
    MEAT = 'meat' # 肉食
    SAUCES = 'sauces' # 酱料
    FUEL = 'fuel' # 燃料
    RICE = 'rice' # 米饭
    SIMPLE = 'simple' # 简易食品
    BAKE = 'bake' # 烘焙工艺
    RAW_PIE = 'raw_pie' # 生派
    PIE = 'pie' # 派
    RAW = 'raw' # 生食
    FAST = 'fast' # 快餐
    BURGER = 'burger' # 汉堡
    FRY = 'fry' # 炒菜
    PORRIDGE = 'porridge' # 粥
    NOODLE = 'noodle' # 面食
    CARROT = 'carrot' # 萝卜
    FISH = 'fish' # 鱼
    COOKED_FISH = 'cooked_fish' # 熟鱼

    cnNameDict = {
        CROP: '粮食',
        VEGETABLE: '蔬菜',
        FRUIT: '水果',
        FUNGI: '菌类',
        SPICES: '香料',
        SEASONING: '调料',
        CEREAL: '谷物',
        SOLANUM: '茄属',
        CAPSICUM: '辣椒属',
        GREEN: '青菜',
        ALLIUM: '葱属',
        WATER: '水生',
        ORE: '矿物质',
        PRODUCT: '农产品',
        DAIRY: '乳制品',
        SOY: '黄豆制品',
        BEAN: '豆制品',
        OIL: '油',
        WHEAT: '谷物制品',
        MEAT: '肉制品',
        SAUCES: '酱料',
        FUEL: '燃料',
        RICE: '米饭',
        SIMPLE: '简易',
        BAKE: '烘焙',
        RAW_PIE: '生派',
        PIE: '派',
        RAW: '生食',
        FAST: '快餐',
        BURGER: '汉堡',
        FRY: '炒菜',
        PORRIDGE: '粥',
        NOODLE: '面食',
        CARROT: '萝卜',
        FISH: '鱼',
        COOKED_FISH: '熟鱼',
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