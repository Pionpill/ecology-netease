from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

BROCCOLI_PORRIDGE = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:stew_pot",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.PORRIDGE,),
  "hidden_effect": None,
  "food": {
    "nutrition": 6,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": True,
    "effect": (
      {
        "name": EffectType.HEALTH_BOOST,
        "chance": 1,
        "duration": 120,
        "amplifier": 0
      },
      {
        "name": EffectType.RESISTANCE,
        "chance": 1,
        "duration": 120,
        "amplifier": 0
      }
    )
  }
}
