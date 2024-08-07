from scripts.common.enum import BiomeTag
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

SORGHUM = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.CROP: ("ham:corn",),
    ItemSource.WILD: (BiomeTag.PLAINS, BiomeTag.FLOWER_FOREST)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.CROP, ItemTag.CEREAL),
  "hidden_effect": None,
  "food": {
    "nutrition": 3,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": True,
    "effect": None
  }
}
