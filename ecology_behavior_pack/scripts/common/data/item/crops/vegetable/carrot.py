from scripts.common.enum import BiomeTag
from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

CARROT = {
  "quality": ItemQuality.COMMON,
  "source": {
    ItemSource.CROP: ("ham:carrot",),
    ItemSource.WILD: (BiomeTag.PLAINS,),
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.VEGETABLE, ItemTag.CARROT),
  "hidden_effect": [EffectType.NIGHT_VISION],
  "food": {
    "nutrition": 2,
    "saturation": FoodSaturation.LOW,
    "can_eat": True
  }
}
