from scripts.common.enum import BiomeTag
from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

SUGARCANE = {
  "quality": ItemQuality.COMMON,
  "source": {
    ItemSource.CROP: ("ham:sugarcane",),
    ItemSource.WILD: (BiomeTag.JUNGLE,)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.FRUIT, ),
  "hidden_effect": [EffectType.INSTANT_HEALTH],
  "food": {
    "nutrition": 0.5,
    "saturation": FoodSaturation.POOR,
    "can_eat": True
  }
}
