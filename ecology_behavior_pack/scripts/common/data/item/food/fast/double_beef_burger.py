from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

DOUBLE_BEEF_BURGER = {
  "quality": ItemQuality.EPIC,
  "source": {
    ItemSource.WORKBENCH: ("ham:cooking_table",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.FAST, ItemTag.BURGER),
  "hidden_effect": None,
  "food": {
    "nutrition": 12,
    "saturation": FoodSaturation.MAX,
    "can_eat": True,
    "effect": (
      {
        "name": EffectType.STRENGTH,
        "chance": 1,
        "duration": 180,
        "amplifier": 0
      },
      {
        "name": EffectType.ABSORPTION,
        "chance": 1,
        "duration": 180,
        "amplifier": 0
      },
    )
  }
}