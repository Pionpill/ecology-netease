from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

EGG_FIRED_RICE = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.WORKBENCH: ("ham:pan",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.RICE,),
  "hidden_effect": None,
  "food": {
    "nutrition": 9,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": True
  }
}
