from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

CORN_PEA_PORRIDGE = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:stew_pot",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.PORRIDGE,),
  "hidden_effect": None,
  "food": {
    "nutrition": 4,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": True,
    "effect": ({
      "name": EffectType.HASTE,
      "chance": 1,
      "duration": 30,
      "amplifier": 0
    },)
  }
}
