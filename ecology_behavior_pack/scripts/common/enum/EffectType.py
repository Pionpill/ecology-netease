from scripts.common.error import AddonDataError

class EffectType(object):
    SPEED = 'minecraft:speed' # 迅捷
    SLOWNESS = 'minecraft:slowness' # 缓慢
    HASTE = 'minecraft:haste' # 急迫
    MINING_FATIGUE = 'minecraft:mining_fatigue' # 挖掘疲劳
    STRENGTH = 'minecraft:strength' # 力量
    INSTANT_HEALTH = 'minecraft:instant_health' # 瞬间治疗
    INSTANT_DAMAGE = 'minecraft:instant_damage' # 瞬间伤害
    JUMP_BOOST = 'minecraft:jump_boost' # 跳跃升级
    NAUSEA = 'minecraft:nausea' # 反胃
    REGENERATION = 'minecraft:regeneration' # 生命恢复
    RESISTANCE = 'minecraft:resistance' # 抗性提升
    FIRE_RESISTANCE = 'minecraft:fire_resistance' # 抗火
    WATER_BREATHING = 'minecraft:water_breathing' # 水下呼吸
    INVISIBILITY = "minecraft:invisibility" # 隐身
    BLINDNESS = "minecraft:blindness" # 失明
    NIGHT_VISION = "minecraft:night_vision" # 夜视
    HUNGER = "minecraft:hunger" # 饥饿
    WEAKNESS = "minecraft:weakness" # 虚弱
    POISON = "minecraft:poison" # 中毒
    FATAL_POISON = "minecraft:fatal_poison" # 中毒(致命)
    WITHER = "minecraft:wither" # 凋零
    HEALTH_BOOST = "minecraft:health_boost" # 生命提升
    ABSORPTION = "minecraft:absorption" # 伤害吸收
    SATURATION = "minecraft:saturation" # 饱和
    LEVITATION = "minecraft:levitation" # 漂浮
    SLOW_FALLING = "minecraft:slow_falling" # 缓降
    CONDUIT_POWER = "minecraft:conduit_power" # 潮涌能量
    HERO_OF_THE_VILLAGE = "minecraft:hero_of_the_village" # 村庄英雄
    DARKNESS = "minecraft:darkness" # 黑暗

    cnNameDict = {
        SPEED: "迅捷",
        SLOWNESS: "缓慢",
        HASTE: "急迫",
        MINING_FATIGUE: "挖掘疲劳",
        STRENGTH: "力量",
        INSTANT_HEALTH: "瞬间治疗",
        INSTANT_DAMAGE: "瞬间伤害",
        JUMP_BOOST: "跳跃升级",
        NAUSEA: "反胃",
        REGENERATION: "生命恢复",
        RESISTANCE: "抗性提升",
        FIRE_RESISTANCE: "抗火",
        WATER_BREATHING: "水下呼吸",
        INVISIBILITY: "隐身",
        BLINDNESS: "失明",
        NIGHT_VISION: "夜视",
        HUNGER: "饥饿",
        WEAKNESS: "虚弱",
        POISON: "中毒",
        FATAL_POISON: "中毒(致命)",
        WITHER: "凋零",
        HEALTH_BOOST: "生命提升",
        ABSORPTION: "伤害吸收",
        SATURATION: "饱和",
        LEVITATION: "漂浮",
        SLOW_FALLING: "缓降",
        CONDUIT_POWER: "潮涌能量",
        HERO_OF_THE_VILLAGE: "村庄英雄",
        DARKNESS: "黑暗",
    }

    @staticmethod
    def GetChinese(quality):
        chinese = EffectType.cnNameDict.get(quality)
        if not chinese:
            raise AddonDataError('不存在 {} 效果的中文名'.format(quality))
        return chinese