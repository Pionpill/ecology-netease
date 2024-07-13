from scripts.common.enum import BiomeTag
from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

PEPPER = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.CROP: ("ham:pepper",),
    ItemSource.WILD: (BiomeTag.FOREST,)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.VEGETABLE, ItemTag.CAPSICUM),
  "hidden_effect": [EffectType.SPEED],
  "food": {
    "nutrition": 0.5,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": True
  }
}
