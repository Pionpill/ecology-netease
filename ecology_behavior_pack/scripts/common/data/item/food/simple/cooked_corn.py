from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

COOKED_CORN = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.WORKBENCH: ("ham:baking_furnace", "ham:grill", "ham:food_steamer", "ham:stew_pot"),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.SIMPLE,),
  "hidden_effect": None,
  "food": {
    "nutrition": 3,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": True,
    "effect": None
  }
}
