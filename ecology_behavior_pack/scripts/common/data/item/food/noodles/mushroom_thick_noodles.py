from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

MUSHROOM_THICK_NOODLES = {
  "quality": ItemQuality.EPIC,
  "source": {
    ItemSource.WORKBENCH: ("ham:stew_pot",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.NOODLE,),
  "hidden_effect": None,
  "food": {
    "nutrition": 12,
    "saturation": FoodSaturation.MAX,
    "can_eat": True,
    "effect": ({
      "name": EffectType.STRENGTH,
      "chance": 1,
      "duration": 120,
      "amplifier": 1
    },{
      "name": EffectType.JUMP_BOOST,
      "chance": 1,
      "duration": 180,
      "amplifier": 1
    })
  }
}
