from scripts.common.enum import BiomeTag
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

POTATO = {
  "quality": ItemQuality.COMMON,
  "source": {
    ItemSource.CROP: ("ham:potato",),
    ItemSource.WILD: (BiomeTag.TAIGA, BiomeTag.FOREST)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.CROP),
  "hidden_effect": None,
  "food": {
    "nutrition": 2,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": True,
    "effect": None
  }
}
