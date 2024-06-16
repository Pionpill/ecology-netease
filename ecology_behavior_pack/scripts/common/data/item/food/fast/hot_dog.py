from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

HOT_DOG = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:cooking_table",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.FAST,),
  "hidden_effect": None,
  "food": {
    "nutrition": 12,
    "saturation": FoodSaturation.GOOD,
    "can_eat": True,
    "effect": (
      {
        "name": EffectType.STRENGTH,
        "chance": 1,
        "duration": 30,
        "amplifier": 0
      },
    )
  }
}