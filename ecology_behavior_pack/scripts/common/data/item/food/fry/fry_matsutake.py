from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

FRY_MATSUTAKE = {
  "quality": ItemQuality.EPIC,
  "source": {
    ItemSource.WORKBENCH: ("ham:pan",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.FRY,),
  "hidden_effect": None,
  "food": {
    "nutrition": 7,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": True,
    "effect": ({
      "name": EffectType.REGENERATION,
      "chance": 1,
      "duration": 60,
      "amplifier": 2
    },)
  }
}
