from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

CORN_PIE = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.WORKBENCH: ("ham:baking_furnace",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.BAKE, ItemTag.PIE),
  "hidden_effect": None,
  "food": {
    "nutrition": 5,
    "saturation": FoodSaturation.GOOD,
    "can_eat": True,
  }
}

RAW_CORN_PIE = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.WORKBENCH: ("ham:cooking_table"),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.RAW_PIE,),
  "hidden_effect": None,
}
