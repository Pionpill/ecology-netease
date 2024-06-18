from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

BURGER = {
  "quality": ItemQuality.EPIC,
  "source": {
    ItemSource.WORKBENCH: ("ham:cooking_table",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.FAST, ItemTag.BURGER),
  "hidden_effect": None,
  "food": {
    "nutrition": 14,
    "saturation": FoodSaturation.GOOD,
    "can_eat": True,
    "effect": (
      {
        "name": EffectType.STRENGTH,
        "chance": 1,
        "duration": 60,
        "amplifier": 0
      },
      {
        "name": EffectType.ABSORPTION,
        "chance": 1,
        "duration": 30,
        "amplifier": 0
      },
    )
  }
}