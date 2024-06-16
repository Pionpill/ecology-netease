from scripts.common.enum.Item import ItemCategory, ItemQuality, ItemSource, ItemTag

SALT = {
  "quality": ItemQuality.COMMON,
  "source": {
    ItemSource.BLOCK: ("ham:salt",)
  },
  "category": ItemCategory.MATERIAL,
  "tag": (ItemTag.SEASONING,),
  "hidden_effect": None
}
