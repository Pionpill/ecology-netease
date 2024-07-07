from scripts.common.enum import BiomeTag
from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

GARLIC = {
  "quality": ItemQuality.COMMON,
  "source": {
    ItemSource.CROP: ("ham:garlic",),
    ItemSource.WILD: (BiomeTag.PLAINS, BiomeTag.MOUNTAINS, BiomeTag.HILLS)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.SEASONING, ItemTag.SPICES),
  "hidden_effect": None,
  "food": {
    "nutrition": 0,
    "saturation": FoodSaturation.POOR,
    "can_eat": False,
  }
}
