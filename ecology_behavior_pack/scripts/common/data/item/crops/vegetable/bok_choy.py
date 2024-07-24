from scripts.common.enum import BiomeTag
from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

BOK_CHOY = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.CROP: ("ham:bok_choy",),
    ItemSource.WILD: (BiomeTag.FOREST,)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.VEGETABLE, ItemTag.GREEN),
  "hidden_effect": [EffectType.ABSORPTION],
  "food": {
    "nutrition": 1,
    "saturation": FoodSaturation.POOR,
    "can_eat": True
  }
}
