from scripts.common.enum import BiomeTag, EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

SCALLION = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.CROP: ("ham:scallion",),
    ItemSource.WILD: (BiomeTag.FOREST,),
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.SEASONING, ItemTag.ALLIUM),
  "effect": (EffectType.NAUSEA,),
  "hidden_effect": (EffectType.ABSORPTION,),
  "food": {
    "nutrition": 1,
    "saturation": FoodSaturation.LOW,
    "can_eat": True
  }
}
