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
  "hidden_effect": [EffectType.HEALTH_BOOST],
  "food": {
    "nutrition": 0.5,
    "saturation": FoodSaturation.POOR,
    "can_eat": False
  }
}
