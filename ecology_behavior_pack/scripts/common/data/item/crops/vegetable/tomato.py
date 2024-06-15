from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

TOMATO = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.CROP: ("ham:tomato",)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.VEGETABLE, ItemTag.SOLANUM),
  "hidden_effect": (EffectType.REGENERATION,),
  "food": {
    "nutrition": 1.5,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": True
  }
}
