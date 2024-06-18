from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

SEASONING = {
  "quality": ItemQuality.COMMON,
  "source": {
    ItemSource.WORKBENCH: ("ham:cooking_table",),
  },
  "category": ItemCategory.MATERIAL,
  "tag": (ItemTag.SPICES,),
  "hidden_effect": None,
  "food": {
    "nutrition": 0,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": False,
    "effect": None
  }
}
