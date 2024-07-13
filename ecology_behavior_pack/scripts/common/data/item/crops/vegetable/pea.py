from scripts.common.enum import BiomeTag
from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

PEA = {
  "quality": ItemQuality.COMMON,
  "source": {
    ItemSource.CROP: ("ham:pea",),
    ItemSource.WILD: (BiomeTag.PLAINS, BiomeTag.MOUNTAIN, BiomeTag.MOUNTAINS, BiomeTag.HILLS)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.VEGETABLE,),
  "hidden_effect": [EffectType.HASTE],
  "food": {
    "nutrition": 0.5,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": True
  }
}
