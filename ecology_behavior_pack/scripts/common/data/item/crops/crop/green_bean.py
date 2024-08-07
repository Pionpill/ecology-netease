from scripts.common.enum import BiomeTag
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

GREEN_BEAN = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.CROP: ("ham:green_bean",),
    ItemSource.WILD: (BiomeTag.MOUNTAIN, BiomeTag.MOUNTAINS, BiomeTag.HILLS, BiomeTag.SWAMP)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.CROP, ItemTag.CEREAL, ItemTag.BEAN),
  "hidden_effect": None,
  "food": {
    "nutrition": 1,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": False,
    "effect": None
  }
}
