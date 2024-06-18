from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

MAPO_TOFU = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:pan",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.FRY,),
  "hidden_effect": None,
  "food": {
    "nutrition": 6,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": True,
    "effect": ({
      "name": EffectType.SPEED,
      "chance": 1,
      "duration": 120,
      "amplifier": 0
    },)
  }
}
