from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

GROUND_PORK = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:mill",),
  },
  "category": ItemCategory.MATERIAL,
  "tag": (ItemTag.PRODUCT, ItemTag.MEAT, ItemTag.RAW),
  "hidden_effect": (EffectType.STRENGTH,),
  "food": {
    "nutrition": 3,
    "saturation": FoodSaturation.GOOD,
    "can_eat": False,
    "effect": None
  }
}
