from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

APPLE_PIE = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:baking_furnace",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.BAKE, ItemTag.PIE),
  "hidden_effect": None,
  "food": {
    "nutrition": 10,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": True,
    "effect": ({
        "name": EffectType.REGENERATION,
        "chance": 1,
        "duration": 60,
        "amplifier": 0
    },)
  }
}

RAW_APPLE_PIE = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:cooking_table"),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.BAKE, ItemTag.PIE),
  "hidden_effect": None,
  "food": {
    "nutrition": 10,
    "saturation": FoodSaturation.POOR,
    "can_eat": False
  }
}
