from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

DOUGH = {
  "quality": ItemQuality.COMMON,
  "source": {
    ItemSource.WORKBENCH: ("ham:cooking_table",),
  },
  "category": ItemCategory.MATERIAL,
  "tag": (ItemTag.PRODUCT, ItemTag.WHEAT),
  "hidden_effect": None,
  "food": {
    "nutrition": 4,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": False,
    "effect": None
  }
}
