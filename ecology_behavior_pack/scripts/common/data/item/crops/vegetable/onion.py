from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

ONION = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.CROP: ("ham:onion",)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.VEGETABLE, ItemTag.ALLIUM),
  "hidden_effect": (EffectType.ABSORPTION,),
  "food": {
    "nutrition": 1,
    "saturation": FoodSaturation.LOW,
    "can_eat": True
  }
}
