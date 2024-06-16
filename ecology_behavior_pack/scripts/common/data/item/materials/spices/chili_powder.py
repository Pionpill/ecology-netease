from scripts.common.enum import EffectType
from scripts.common.enum.Item import ItemCategory, ItemQuality, ItemSource, ItemTag

CHILI_POWDER = {
  "quality": ItemQuality.UNCOMMON,
  "source": {
    ItemSource.WORKBENCH: ("ham:mill",)
  },
  "category": ItemCategory.MATERIAL,
  "tag": (ItemTag.SEASONING, ItemTag.SPICES),
  "hidden_effect": (EffectType.SPEED,),
}
