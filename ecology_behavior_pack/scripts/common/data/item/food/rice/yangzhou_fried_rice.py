from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

YANGZHOU_FRIED_RICE = {
  "quality": ItemQuality.EPIC,
  "source": {
    ItemSource.WORKBENCH: ("ham:pan",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.RICE,),
  "hidden_effect": None,
  "food": {
    "nutrition": 14,
    "saturation": FoodSaturation.GOOD,
    "can_eat": True,
    "effect": ({
      "name": EffectType.STRENGTH,
      "chance": 1,
      "duration": 120,
      "amplifier": 0
    },)
  }
}
