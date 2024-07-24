from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

FRY_BROCCOLI = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:pan",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.FRY,),
  "hidden_effect": None,
  "food": {
    "nutrition": 8,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": True,
    "effect": ({
      "name": EffectType.RESISTANCE,
      "chance": 1,
      "duration": 90,
      "amplifier": 0
    },)
  }
}
