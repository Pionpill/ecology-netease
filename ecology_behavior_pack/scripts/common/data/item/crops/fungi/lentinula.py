from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

LENTINULA = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.CROP: ("ham:lentinula",)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.FUNGI,),
  "hidden_effect": [EffectType.NAUSEA, EffectType.LEVITATION],
  "food": {
    "nutrition": 0.5,
    "saturation": FoodSaturation.POOR,
    "can_eat": False
  }
}
