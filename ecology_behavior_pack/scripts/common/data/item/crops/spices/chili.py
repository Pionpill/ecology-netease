from scripts.common.enum import BiomeTag, EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

CHILI = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.CROP: ("ham:chili",),
    ItemSource.WILD: (BiomeTag.FOREST,),
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.SEASONING, ItemTag.SPICES, ItemTag.CAPSICUM),
  "hidden_effect": (EffectType.SPEED,),
  "food": {
    "nutrition": 0,
    "saturation": FoodSaturation.POOR,
    "can_eat": True,
    "effect": (
      {
        "name": EffectType.INSTANT_DAMAGE,
        "chance": 1,
        "duration": 1,
        "amplifier": 0
      },
    )
  }
}
