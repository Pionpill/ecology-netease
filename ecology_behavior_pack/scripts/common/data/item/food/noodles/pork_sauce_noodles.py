from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

PORK_SAUCE_NOODLES = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:stew_pot",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.NOODLE,),
  "hidden_effect": None,
  "food": {
    "nutrition": 8,
    "saturation": FoodSaturation.GOOD,
    "can_eat": True,
    "effect": ({
      "name": EffectType.STRENGTH,
      "chance": 1,
      "duration": 45,
      "amplifier": 0
    },)
  }
}
