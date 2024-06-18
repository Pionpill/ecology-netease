from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

NOODLE = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.WORKBENCH: ("ham:cooking_table",),
  },
  "category": ItemCategory.MATERIAL,
  "tag": (ItemTag.PRODUCT,),
  "hidden_effect": None,
  "food": {
    "nutrition": 3,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": False,
    "effect": None
  }
}
