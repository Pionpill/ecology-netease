from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

PORK_EGGPLANT = {
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
        "name": EffectType.REGENERATION,
        "chance": 1,
        "duration": 60,
        "amplifier": 1
      },
      {
        "name": EffectType.HASTE,
        "chance": 1,
        "duration": 200,
        "amplifier": 1
      },
    )
  }
}
