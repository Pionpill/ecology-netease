from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

CORN_THICK_SOUP = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:stew_pot",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.SOUP,),
  "hidden_effect": None,
  "food": {
    "nutrition": 3,
    "saturation": FoodSaturation.GOOD,
    "can_eat": True,
    "effect": ({
        "name": EffectType.SPEED,
        "chance": 1,
        "duration": 120,
        "amplifier": 0
    },)
  }
}