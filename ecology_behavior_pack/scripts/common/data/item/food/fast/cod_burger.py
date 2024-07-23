from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

COD_BURGER = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:cooking_table",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.FAST, ItemTag.BURGER),
  "hidden_effect": None,
  "food": {
    "nutrition": 7,
    "saturation": FoodSaturation.GOOD,
    "can_eat": True,
    "effect": ({
        "name": EffectType.WATER_BREATHING,
        "chance": 1,
        "duration": 180,
        "amplifier": 0
    },)
  }
}