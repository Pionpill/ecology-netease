from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

ONION_BEEF_RICE = {
  "quality": ItemQuality.EPIC,
  "source": {
    ItemSource.WORKBENCH: ("ham:pan",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.RICE,),
  "hidden_effect": None,
  "food": {
    "nutrition": 15,
    "saturation": FoodSaturation.MAX,
    "can_eat": True,
    "effect": ({
        "name": EffectType.STRENGTH,
        "chance": 1,
        "duration": 180,
        "amplifier": 2
    },{
        "name": EffectType.ABSORPTION,
        "chance": 1,
        "duration": 180,
        "amplifier": 1
    },)
  }
}
