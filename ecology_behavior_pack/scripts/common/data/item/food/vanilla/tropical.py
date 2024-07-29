from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemTag

TROPICAL_FISH = {
  "quality": ItemQuality.UNCOMMON,
  "source": {},
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.FISH,),
  "hidden_effect": [EffectType.WATER_BREATHING, EffectType.INSTANT_HEALTH],
  "food": {
    "nutrition": 2,
    "saturation": FoodSaturation.GOOD,
    "can_eat": True,
    "effect": None
  }
}
