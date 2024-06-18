from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

PORK_SAUCE_RICE = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:pan",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.RICE,),
  "hidden_effect": None,
  "food": {
    "nutrition": 11,
    "saturation": FoodSaturation.GOOD,
    "can_eat": True,
    "effect": ({
      "name": EffectType.STRENGTH,
      "chance": 1,
      "duration": 60,
      "amplifier": 0
    },)
  }
}
