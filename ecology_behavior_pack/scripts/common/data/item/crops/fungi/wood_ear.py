from scripts.common.enum import BiomeTag
from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

WOOD_EAR = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.CROP: ("ham:wood_ear",),
    ItemSource.WILD: (BiomeTag.FOREST,),
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.FUNGI,),
  "hidden_effect": [EffectType.SPEED],
  "food": {
    "nutrition": 0.5,
    "saturation": FoodSaturation.POOR,
    "can_eat": False
  }
}
