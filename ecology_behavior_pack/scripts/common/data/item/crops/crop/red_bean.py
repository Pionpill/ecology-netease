from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

RED_BEAN = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.CROP: ("ham:red_bean",)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.CROP, ItemTag.CEREAL, ItemTag.BEAN),
  "hidden_effect": None,
  "food": {
    "nutrition": 1,
    "saturation": FoodSaturation.NORMAL,
    "can_eat": False,
    "effect": None
  }
}
