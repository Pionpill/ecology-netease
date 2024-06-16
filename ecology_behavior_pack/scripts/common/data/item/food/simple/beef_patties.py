from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

BEEF_PATTIES = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:pan", "ham:food_steamer", "ham:grill"),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.SIMPLE, ItemTag.MEAT),
  "hidden_effect": (EffectType.STRENGTH,),
  "food": {
    "nutrition": 5,
    "saturation": FoodSaturation.GOOD,
    "can_eat": True,
    "effect": ({
        "name": EffectType.STRENGTH,
        "chance": 1,
        "duration": 30,
        "amplifier": 0
    },)
  }
}

RAW_BEEF_PATTIES = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:cooking_table",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.SIMPLE, ItemTag.MEAT, ItemTag.RAW),
  "hidden_effect": None,
  "food": {
    "nutrition": 5,
    "saturation": FoodSaturation.POOR,
    "can_eat": False,
  }
}
