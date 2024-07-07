from scripts.common.enum import BiomeTag
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

TARO = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.CROP: ("ham:taro",),
    ItemSource.WILD: (BiomeTag.SWAMP,)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.CROP,),
  "hidden_effect": None,
  "food": {
    "nutrition": 2,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": False,
    "effect": None
  }
}
