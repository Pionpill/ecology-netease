from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

ONION_RING = {
  "quality": ItemQuality.COMMON,
  "source": {
    ItemSource.WORKBENCH: ("ham:fryer",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.FAST,),
  "hidden_effect": None,
  "food": {
    "nutrition": 5,
    "saturation": FoodSaturation.GOOD,
    "can_eat": True,
  }
}