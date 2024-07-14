from scripts.common.enum import BiomeTag, EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

ONION = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.CROP: ("ham:onion",),
    ItemSource.WILD: (BiomeTag.TAIGA)
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
