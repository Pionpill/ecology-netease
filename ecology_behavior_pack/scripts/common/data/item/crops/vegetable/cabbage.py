from scripts.common.enum import BiomeTag
from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

CABBAGE = {
  "quality": ItemQuality.COMMON,
  "source": {
    ItemSource.CROP: ("ham:cabbage",),
    ItemSource.WILD: (BiomeTag.PLAINS,),
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.VEGETABLE,),
  "hidden_effect": [EffectType.RESISTANCE],
  "food": {
    "nutrition": 1,
    "saturation": FoodSaturation.POOR,
    "can_eat": False
  }
}
