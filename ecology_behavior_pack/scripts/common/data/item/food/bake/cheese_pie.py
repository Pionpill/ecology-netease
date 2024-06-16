from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

CHEESE_PIE = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:baking_furnace",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.BAKE, ItemTag.PIE),
  "hidden_effect": None,
  "food": {
    "nutrition": 8,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": True,
    "effect": ({
        "name": EffectType.HASTE,
        "chance": 1,
        "duration": 90,
        "amplifier": 0
    },)
  }
}

RAW_CHEESE_PIE = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:cooking_table"),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.BAKE, ItemTag.PIE),
  "hidden_effect": None,
  "food": {
    "nutrition": 8,
    "saturation": FoodSaturation.POOR,
    "can_eat": False
  }
}
