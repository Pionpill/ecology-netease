from scripts.common.enum import BiomeTag
from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

RAPE_SEEDS = {
  "quality": ItemQuality.COMMON,
  "source": {
    ItemSource.CROP: ("ham:rape_seeds",),
    ItemSource.WILD: (BiomeTag.PLAINS,)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.VEGETABLE, ),
  "hidden_effect":None,
  "food": {
    "nutrition": 2,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": True
  }
}
