from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

SCALLION = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.BLOCK: ("ham:scallion")
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.VEGETABLE, ItemTag.ALLIUM),
  "hidden_effect": [EffectType.ABSORPTION],
  "food": {
    "nutrition": 0.5,
    "saturation_modifier": FoodSaturation.LOW,
    "can_eat": True
  }
}
