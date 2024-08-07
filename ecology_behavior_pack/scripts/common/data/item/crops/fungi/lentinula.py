from scripts.common.enum import BiomeTag, EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

LENTINULA = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.CROP: ("ham:lentinula",),
    ItemSource.WILD: (BiomeTag.SWAMP,),
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.FUNGI,),
  "effect": [EffectType.POISON],
  "hidden_effect": [EffectType.NAUSEA],
  "food": {
    "nutrition": 1,
    "saturation": FoodSaturation.POOR,
    "can_eat": False
  }
}
