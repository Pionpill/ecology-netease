from scripts.common.enum import BiomeTag
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

WHEAT_PLANT = {
  "quality": ItemQuality.COMMON,
  "source": {
    ItemSource.CROP: ("ham:wheat",),
    ItemSource.WILD: (BiomeTag.FOREST, BiomeTag.BIRCH)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.CROP, ItemTag.CEREAL),
  "hidden_effect": None,
  "food": {
    "nutrition": 3,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": False,
    "effect": None
  }
}
