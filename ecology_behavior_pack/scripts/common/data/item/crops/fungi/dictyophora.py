from scripts.common.enum import BiomeTag
from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

DICTYOPHORA = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.CROP: ("ham:dictyophora",),
    ItemSource.WILD: (BiomeTag.FOREST,),
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.FUNGI,),
  "effect": [EffectType.POISON],
  "hidden_effect": [EffectType.HEALTH_BOOST],
  "food": {
    "nutrition": 1,
    "saturation": FoodSaturation.POOR,
    "can_eat": False
  }
}
