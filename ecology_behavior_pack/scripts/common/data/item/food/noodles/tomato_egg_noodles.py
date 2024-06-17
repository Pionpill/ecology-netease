from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

TOMATO_EGG_NOODLES = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:stew_pot",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.NOODLE,),
  "hidden_effect": None,
  "food": {
    "nutrition": 7,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": True,
    "effect": ({
      "name": EffectType.REGENERATION,
      "chance": 1,
      "duration": 20,
      "amplifier": 0
    },)
  }
}
