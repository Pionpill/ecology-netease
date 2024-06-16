from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

BUTTER = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.WORKBENCH: ("ham:squeezer",),
  },
  "category": ItemCategory.MATERIAL,
  "tag": (ItemTag.PRODUCT, ItemTag.DAIRY),
  "hidden_effect": None,
  "food": {
    "nutrition": 0.5,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": False,
    "effect": None
  }
}
