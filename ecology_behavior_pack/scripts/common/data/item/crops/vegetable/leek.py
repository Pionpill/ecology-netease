from scripts.common.enum import BiomeTag
from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

LEEK = {
  "quality": ItemQuality.COMMON,
  "source": {
    ItemSource.CROP: ("ham:leek",),
    ItemSource.WILD: (BiomeTag.PLAINS,)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.VEGETABLE, ItemTag.GREEN),
  "hidden_effect": None,
  "food": {
    "nutrition": 1,
    "saturation": FoodSaturation.POOR,
    "can_eat": True
  }
}
