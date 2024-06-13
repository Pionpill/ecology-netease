from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

CORN = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.BLOCK: ("ham:corn")
  },
  "category": (ItemCategory.CROPS),
  "tag": (ItemTag.CROP, ItemTag.CEREAL),
  "hidden_effect": None,
  "food": {
    "nutrition": 1.5,
    "saturation_modifier": FoodSaturation.NORMAL,
    "can_eat": True,
    "effect": None
  }
}
