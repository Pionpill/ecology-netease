from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

SOY_BEAN = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.BLOCK: ("ham:soy_bean")
  },
  "category": (ItemCategory.CROPS),
  "tag": (ItemTag.CROP, ItemTag.CEREAL),
  "hidden_effect": None,
  "food": {
    "nutrition": 1.5,
    "saturation_modifier": FoodSaturation.NORMAL,
    "can_eat": False,
    "effect": None
  }
}
