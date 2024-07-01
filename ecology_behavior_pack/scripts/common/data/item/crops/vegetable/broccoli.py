from scripts.common.enum import BiomeTag
from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

BROCCOLI = {
  "quality": ItemQuality.RARE,
  "source": {
    ItemSource.CROP: ("ham:broccoli",),
    ItemSource.WILD: (BiomeTag.PLAINS,),
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.VEGETABLE,),
  "hidden_effect": [EffectType.RESISTANCE, EffectType.HEALTH_BOOST],
  "food": {
    "nutrition": 0.5,
    "saturation": FoodSaturation.POOR,
    "can_eat": True
  }
}

WHITE_BROCCOLI = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.CROP: ("ham:broccoli",),
    ItemSource.WILD: (BiomeTag.PLAINS,)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.VEGETABLE,),
  "hidden_effect": [EffectType.RESISTANCE],
  "food": {
    "nutrition": 0.5,
    "saturation": FoodSaturation.POOR,
    "can_eat": True
  }
}
