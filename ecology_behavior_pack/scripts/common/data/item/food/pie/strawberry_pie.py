from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

STRAWBERRY_PIE = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:baking_furnace",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.BAKE, ItemTag.PIE),
  "hidden_effect": None,
  "food": {
    "nutrition": 7,
    "saturation": FoodSaturation.GOOD,
    "can_eat": True,
    "effect": ({
        "name": EffectType.REGENERATION,
        "chance": 1,
        "duration": 45,
        "amplifier": 0
    },)
  }
}

RAW_STRAWBERRY_PIE = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:cooking_table"),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.RAW_PIE,),
  "hidden_effect": None
}
