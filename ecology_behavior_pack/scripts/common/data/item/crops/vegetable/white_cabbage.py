from scripts.common.enum import BiomeTag
from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

WHITE_CABBAGE = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.CROP: ("ham:white_cabbage",),
    ItemSource.WILD: (BiomeTag.PLAINS,),
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.VEGETABLE,),
  "hidden_effect": [EffectType.RESISTANCE],
  "food": {
    "nutrition": 2,
    "saturation": FoodSaturation.POOR,
    "can_eat": True
  }
}
