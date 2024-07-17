from scripts.common.enum import BiomeTag
from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

ENOKI = {
  "quality": ItemQuality.COMMON,
  "source": {
    ItemSource.CROP: ("ham:enoki",),
    ItemSource.WILD: (BiomeTag.TAIGA,),
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.FUNGI,),
  "effect": [EffectType.POISON],
  "hidden_effect": [EffectType.JUMP_BOOST],
  "food": {
    "nutrition": 1,
    "saturation": FoodSaturation.POOR,
    "can_eat": False
  }
}
