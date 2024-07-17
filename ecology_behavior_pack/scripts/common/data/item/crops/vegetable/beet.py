from scripts.common.enum import BiomeTag
from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

BEET_ROOT = {
  "quality": ItemQuality.COMMON,
  "source": {
    ItemSource.CROP: ("ham:beet_root",),
    ItemSource.WILD: (BiomeTag.FOREST, BiomeTag.TAIGA)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.VEGETABLE,),
  "hidden_effect": None,
  "food": {
    "nutrition": 1,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": True
  }
}

BEET_LEAF = {
  "quality": ItemQuality.COMMON,
  "source": {
    ItemSource.CROP: ("ham:beet_root",),
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.VEGETABLE,),
  "hidden_effect": None,
  "food": {
    "nutrition": 1,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": True
  }
}