from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

TONKOTSU_NOODLES = {
  "quality": ItemQuality.EPIC,
  "source": {
    ItemSource.WORKBENCH: ("ham:stew_pot",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.NOODLE,),
  "hidden_effect": None,
  "food": {
    "nutrition": 11,
    "saturation": FoodSaturation.MAX,
    "can_eat": True,
    "effect": ({
      "name": EffectType.HASTE,
      "chance": 1,
      "duration": 300,
      "amplifier": 1
    },{
      "name": EffectType.REGENERATION,
      "chance": 1,
      "duration": 90,
      "amplifier": 1
    },{
      "name": EffectType.SPEED,
      "chance": 1,
      "duration": 300,
      "amplifier": 1
    })
  }
}
