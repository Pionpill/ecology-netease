from scripts.common.enum import EffectType
from scripts.common.enum.Item import ItemCategory, ItemQuality, ItemSource, ItemTag

TOMATO_PACK = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.WORKBENCH: ("ham:cooking_table",)
  },
  "category": ItemCategory.MATERIAL,
  "tag": (ItemTag.SEASONING, ItemTag.SPICES),
  "hidden_effect": None,
}
