from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

CHEESE = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.WORKBENCH: ("ham:squeezer",),
  },
  "category": ItemCategory.MATERIAL,
  "tag": (ItemTag.PRODUCT, ItemTag.DAIRY),
  "hidden_effect": (EffectType.HASTE,),
  "food": {
    "nutrition": 3,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": False,
    "effect": None
  }
}
