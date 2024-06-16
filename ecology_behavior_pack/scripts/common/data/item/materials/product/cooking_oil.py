from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

COOKING_OIL = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.WORKBENCH: ("ham:squeezer",),
  },
  "category": ItemCategory.MATERIAL,
  "tag": (ItemTag.PRODUCT, ItemTag.OIL),
  "hidden_effect": None,
  "food": {
    "nutrition": 2,
    "saturation": FoodSaturation.GOOD,
    "can_eat": False,
    "effect": None
  }
}
