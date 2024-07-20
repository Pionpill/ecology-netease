from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

SWEET_POTATO_YAM_PORRIDGE = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.WORKBENCH: ("ham:stew_pot",),
  },
  "category": ItemCategory.FOOD,
  "tag": (ItemTag.PORRIDGE,),
  "hidden_effect": None,
  "food": {
    "nutrition": 4,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": True,
  }
}
