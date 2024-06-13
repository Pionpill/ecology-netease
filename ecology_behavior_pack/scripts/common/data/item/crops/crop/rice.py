from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

RICE = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.BLOCK: ("ham:rice")
  },
  "category": (ItemCategory.CROPS),
  "tag": (ItemTag.CROP, ItemTag.CEREAL, ItemTag.WATER),
  "hidden_effect": None,
  "food": {
    "nutrition": 5,
    "saturation_modifier": FoodSaturation.NORMAL,
    "can_eat": False,
    "effect": None
  }
}
