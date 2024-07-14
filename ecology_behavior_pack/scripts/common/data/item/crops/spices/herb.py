from scripts.common.enum import BiomeTag
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

HERB = {
  "quality": ItemQuality.COMMON,
  "source": {
    ItemSource.CROP: ("ham:herb",),
    ItemSource.WILD: (BiomeTag.PLAINS, BiomeTag.MOUNTAINS, BiomeTag.MOUNTAIN),
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.SEASONING, ItemTag.SPICES),
  "hidden_effect": None,
  "food": {
    "nutrition": 0,
    "saturation": FoodSaturation.POOR,
    "can_eat": False
  }
}
