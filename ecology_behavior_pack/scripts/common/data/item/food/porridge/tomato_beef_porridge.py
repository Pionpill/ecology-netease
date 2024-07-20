from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

TOMATO_BEEF_PORRIDGE = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:stew_pot",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.PORRIDGE,),
  "hidden_effect": None,
  "food": {
    "nutrition": 6,
    "saturation": FoodSaturation.GOOD,
    "can_eat": True,
    "effect": (
      {
        "name": EffectType.STRENGTH,
        "chance": 1,
        "duration": 25,
        "amplifier": 0
      },
      {
        "name": EffectType.INSTANT_HEALTH,
        "chance": 1,
        "duration": 10,
        "amplifier": 0
      }
    )
  }
}
