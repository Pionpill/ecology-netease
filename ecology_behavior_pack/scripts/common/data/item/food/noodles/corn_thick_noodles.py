from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

CORN_THICK_NOODLES = {
  "quality": ItemQuality.EPIC,
  "source": {
    ItemSource.WORKBENCH: ("ham:stew_pot",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.NOODLE,),
  "hidden_effect": None,
  "food": {
    "nutrition": 10,
    "saturation": FoodSaturation.GOOD,
    "can_eat": True,
    "effect": ({
      "name": EffectType.STRENGTH,
      "chance": 1,
      "duration": 120,
      "amplifier": 1
    },{
      "name": EffectType.REGENERATION,
      "chance": 1,
      "duration": 120,
      "amplifier": 1
    })
  }
}
