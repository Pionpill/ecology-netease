from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

POTATO_BEEF_PIE = {
  "quality": ItemQuality.EPIC,
  "source": {
    ItemSource.WORKBENCH: ("ham:baking_furnace",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.BAKE, ItemTag.PIE),
  "hidden_effect": None,
  "food": {
    "nutrition": 10,
    "saturation": FoodSaturation.MAX,
    "can_eat": True,
    "effect": ({
        "name": EffectType.STRENGTH,
        "chance": 1,
        "duration": 120,
        "amplifier": 1
    },)
  }
}

RAW_POTATO_BEEF_PIE = {
  "quality": ItemQuality.EPIC,
  "source": {
    ItemSource.WORKBENCH: ("ham:cooking_table"),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.RAW_PIE,),
  "hidden_effect": None
}
