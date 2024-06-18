from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

BUNS = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:food_steamer",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.SIMPLE, ItemTag.MEAT),
  "hidden_effect": None,
  "food": {
    "nutrition": 6,
    "saturation": FoodSaturation.GOOD,
    "can_eat": True,
    "effect": ({
        "name": EffectType.STRENGTH,
        "chance": 1,
        "duration": 10,
        "amplifier": 0
    },)
  }
}

RAW_BUNS = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:cooking_table",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.SIMPLE, ItemTag.MEAT),
  "hidden_effect": None,
  "food": {
    "nutrition": 6,
    "saturation": FoodSaturation.POOR,
    "can_eat": False,
  }
}
