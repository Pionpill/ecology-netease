from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

LENTINULA_CHICKEN_NOODLES = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.WORKBENCH: ("ham:stew_pot",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.NOODLE,),
  "hidden_effect": None,
  "food": {
    "nutrition": 9,
    "saturation": FoodSaturation.MAX,
    "can_eat": True,
    "effect": ({
      "name": EffectType.STRENGTH,
      "chance": 1,
      "duration": 90,
      "amplifier": 1
    },{
      "name": EffectType.REGENERATION,
      "chance": 1,
      "duration": 15,
      "amplifier": 0
    },{
      "name": EffectType.LEVITATION,
      "chance": 1,
      "duration": 90,
      "amplifier": 0
    })
  }
}
