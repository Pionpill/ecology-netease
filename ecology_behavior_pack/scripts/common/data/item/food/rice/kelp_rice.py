from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

KELP_RICE = {
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
        "name": EffectType.WATER_BREATHING,
        "chance": 1,
        "duration": 360,
        "amplifier": 0
    },)
  }
}
