from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

HERB = {
  "quality": ItemQuality.COMMON,
  "source": {
    ItemSource.BLOCK: ("ham:herb")
  },
  "category": (ItemCategory.CROPS),
  "tag": (ItemTag.SEASONING),
  "hidden_effect": None,
  "food": {
    "nutrition": 0,
    "saturation_modifier": FoodSaturation.POOR,
    "can_eat": False
  }
}
