from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

YAM_FISH_PORRIDGE = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:stew_pot",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.PORRIDGE,),
  "hidden_effect": None,
  "food": {
    "nutrition": 5,
    "saturation": FoodSaturation.GOOD,
    "can_eat": True,
    "effect": (
      {
        "name": EffectType.WATER_BREATHING,
        "chance": 1,
        "duration": 120,
        "amplifier": 0
      },
      {
        "name": EffectType.INSTANT_HEALTH,
        "chance": 1,
        "duration": 15,
        "amplifier": 0
      }
    )
  }
}
