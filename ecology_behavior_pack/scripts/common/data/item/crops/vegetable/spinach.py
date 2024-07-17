from scripts.common.enum import BiomeTag
from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

SPINACH = {
  "quality": ItemQuality.COMMON,
  "source": {
    ItemSource.CROP: ("ham:spinach",),
    ItemSource.WILD: (BiomeTag.PLAINS, BiomeTag.TAIGA)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.VEGETABLE, ItemTag.GREEN),
  "hidden_effect": [EffectType.ABSORPTION],
  "food": {
    "nutrition": 1,
    "saturation": FoodSaturation.POOR,
    "can_eat": True
  }
}
