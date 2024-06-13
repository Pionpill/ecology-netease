from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

LETTUCE = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.BLOCK: ("ham:lettuce")
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.VEGETABLE, ItemTag.GREEN),
  "hidden_effect": [EffectType.RESISTANCE],
  "food": {
    "nutrition": 0.5,
    "saturation_modifier": FoodSaturation.POOR,
    "can_eat": True
  }
}
