from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

PEPPER_PORK = {
  "quality": ItemQuality.EPIC,
  "source": {
    ItemSource.WORKBENCH: ("ham:pan",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.FRY,),
  "hidden_effect": None,
  "food": {
    "nutrition": 9,
    "saturation": FoodSaturation.GOOD,
    "can_eat": True,
    "effect": (
      {
        "name": EffectType.SPEED,
        "chance": 1,
        "duration": 180,
        "amplifier": 1
      },
      {
        "name": EffectType.STRENGTH,
        "chance": 1,
        "duration": 120,
        "amplifier": 0
      },
    )
  }
}
