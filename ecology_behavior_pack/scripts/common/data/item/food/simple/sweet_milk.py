from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

SWEET_MILK = {
  "quality": ItemQuality.COMMON,
  "source": {
    ItemSource.WORKBENCH: ("ham:cooking_table",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.SIMPLE, ItemTag.DAIRY),
  "hidden_effect": None,
  "food": {
    "nutrition": 0.5,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": True,
    "effect": None
  }
}
