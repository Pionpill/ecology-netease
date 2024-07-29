from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

HEN_CHICKEN_NOODLES = {
  "quality": ItemQuality.EPIC,
  "source": {
    ItemSource.WORKBENCH: ("ham:stew_pot",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.NOODLE,),
  "hidden_effect": None,
  "food": {
    "nutrition": 10,
    "saturation": FoodSaturation.MAX,
    "can_eat": True,
    "effect": ({
      "name": EffectType.STRENGTH,
      "chance": 1,
      "duration": 180,
      "amplifier": 2
    },{
      "name": EffectType.REGENERATION,
      "chance": 1,
      "duration": 30,
      "amplifier": 0
    },{
      "name": EffectType.HEALTH_BOOST,
      "chance": 1,
      "duration": 1,
      "amplifier": 1
    })
  }
}
