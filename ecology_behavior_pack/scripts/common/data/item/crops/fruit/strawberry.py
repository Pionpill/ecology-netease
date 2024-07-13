from scripts.common.enum import BiomeTag
from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

STRAWBERRY = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.CROP: ("ham:strawberry",),
    ItemSource.WILD: (BiomeTag.FOREST,)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.FRUIT, ),
  "hidden_effect": [EffectType.REGENERATION],
  "food": {
    "nutrition": 0.5,
    "saturation": FoodSaturation.POOR,
    "can_eat": True
  }
}
