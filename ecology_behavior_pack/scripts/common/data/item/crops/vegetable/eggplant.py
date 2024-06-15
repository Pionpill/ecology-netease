from scripts.common.enum import EffectType
from scripts.common.enum.Item import FoodSaturation, ItemCategory, ItemQuality, ItemSource, ItemTag

EGGPLANT = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.CROP: ("ham:eggplant",)
  },
  "category": ItemCategory.CROPS,
  "tag": (ItemTag.VEGETABLE, ItemTag.SOLANUM),
  "hidden_effect": [EffectType.POISON, EffectType.REGENERATION],
  "food": {
    "nutrition": 1.5,
    "saturation": FoodSaturation.POOR,
    "can_eat": True,
    "effect": (
      {
        "name": EffectType.POISON,
        "chance": 0.2,
        "duration": 5,
        "amplifier": 0
      },
    )
  }
}
