from scripts.common.enum import BiomeTag
from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

LETTUCE = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.CROP: ("ham:lettuce",),
    ItemSource.WILD: (BiomeTag.FOREST,)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.VEGETABLE, ItemTag.GREEN),
  "hidden_effect": (EffectType.RESISTANCE,),
  "food": {
    "nutrition": 1,
    "saturation": FoodSaturation.POOR,
    "can_eat": True
  }
}
