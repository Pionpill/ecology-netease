from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

RICE_PLANT = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.CROP: ("ham:rice",)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.CROP, ItemTag.CEREAL, ItemTag.WATER),
  "hidden_effect": None,
  "food": {
    "nutrition": 5,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": False,
    "effect": None
  }
}
