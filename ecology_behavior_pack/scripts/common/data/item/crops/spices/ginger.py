from scripts.common.enum import BiomeTag
from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

GINGER = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.CROP: ("ham:ginger",),
    ItemSource.WILD: (BiomeTag.MOUNTAIN, BiomeTag.MOUNTAINS, BiomeTag.HILLS, BiomeTag.EXTREME_HILLS, BiomeTag.TAIGA)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.SEASONING, ItemTag.SPICES),
  "hidden_effect": (EffectType.SPEED,),
  "food": {
    "nutrition": 0,
    "saturation": FoodSaturation.POOR,
    "can_eat": False,
  }
}
