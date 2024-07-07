from scripts.common.enum import BiomeTag
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

YAM = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.CROP: ("ham:yam",),
    ItemSource.WILD: (BiomeTag.FOREST,)
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
