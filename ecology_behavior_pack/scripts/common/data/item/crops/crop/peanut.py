from scripts.common.enum import BiomeTag
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

PEANUT = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.CROP: ("ham:peanut",),
    ItemSource.WILD: (BiomeTag.MOUNTAIN, BiomeTag.MOUNTAINS, BiomeTag.HILLS, BiomeTag.EXTREME_HILLS)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.CROP, ItemTag.CEREAL),
  "hidden_effect": None,
  "food": {
    "nutrition": 1,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": False,
    "effect": None
  }
}
