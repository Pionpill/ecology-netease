from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemTag

COOKED_TROPICAL = {
  "quality": ItemQuality.UNCOMMON,
  "source": {},
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.COOKED_FISH,),
  "hidden_effect": [EffectType.WATER_BREATHING, EffectType.INSTANT_HEALTH],
  "food": {
    "nutrition": 5,
    "saturation": FoodSaturation.GOOD,
    "can_eat": True,
    "effect": None
  }
}
