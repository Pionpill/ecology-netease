from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

TOMATO_PORK_SAUCE_RICE = {
  "quality": ItemQuality.EPIC,
  "source": {
    ItemSource.WORKBENCH: ("ham:pan",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.RICE,),
  "hidden_effect": None,
  "food": {
    "nutrition": 16,
    "saturation": FoodSaturation.MAX,
    "can_eat": True,
    "effect": ({
        "name": EffectType.REGENERATION,
        "chance": 1,
        "duration": 60,
        "amplifier": 1
    },{
        "name": EffectType.STRENGTH,
        "chance": 1,
        "duration": 240,
        "amplifier": 1
    })
  }
}
