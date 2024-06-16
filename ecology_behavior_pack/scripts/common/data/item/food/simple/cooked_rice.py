from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

COOKED_RICE = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.WORKBENCH: ("ham:food_steamer",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.SIMPLE, ItemTag.RICE),
  "hidden_effect": None,
  "food": {
    "nutrition": 4,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": True,
  }
}
