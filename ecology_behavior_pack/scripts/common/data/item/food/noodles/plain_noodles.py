from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

PLAIN_NOODLES = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.WORKBENCH: ("ham:stew_pot",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.NOODLE,),
  "hidden_effect": None,
  "food": {
    "nutrition": 5,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": True
  }
}
