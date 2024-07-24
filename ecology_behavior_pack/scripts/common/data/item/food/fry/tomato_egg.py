from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

TOMATO_EGG = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:pan",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.FRY,),
  "hidden_effect": None,
  "food": {
    "nutrition": 10,
    "saturation": FoodSaturation.GOOD,
    "can_eat": True,
    "effect": ({
      "name": EffectType.REGENERATION,
      "chance": 1,
      "duration": 15,
      "amplifier": 0
    },)
  }
}
