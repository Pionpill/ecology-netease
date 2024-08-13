BAKE_PIE_DATA = {
    "ham:corn_pie": {
        "material": ("ham:raw_corn_pie", 6),
        "result": ("ham:corn_pie", 6)
    },
    "ham:sweet_potato_pie": {
        "material": ("ham:raw_sweet_potato_pie", 6),
        "result": ("ham:sweet_potato_pie", 6)
    },
    "ham:taro_pie": {
        "material": ("ham:raw_taro_pie", 6),
        "result": ("ham:taro_pie", 6)
    },
    "ham:apple_pie": {
        "material": ("ham:raw_apple_pie", 6),
        "result": ("ham:apple_pie", 6)
    },
    "ham:carrot_pie": {
        "material": ("ham:raw_carrot_pie", 6),
        "result": ("ham:carrot_pie", 6)
    },
    "ham:strawberry_pie": {
        "material": ("ham:raw_strawberry_pie", 6),
        "result": ("ham:strawberry_pie", 6)
    },
    "ham:cheese_pie": {
        "material": ("ham:raw_cheese_pie", 6),
        "result": ("ham:cheese_pie", 6),
    },
    "ham:potato_beef_pie": {
        "material": ("ham:raw_potato_beef_pie", 6),
        "result": ("ham:potato_beef_pie", 6),
    },
    "ham:mushroom_pork_pie": {
        "material": ("ham:raw_mushroom_pork_pie", 6),
        "result": ("ham:mushroom_pork_pie", 6),
    },
    "ham:corn_chicken_pie": {
        "material": ("ham:raw_corn_chicken_pie", 6),
        "result": ("ham:corn_chicken_pie", 6),
    },
}

BAKE_COMMON_DATA = {
    "ham:bread": {
        "material": "ham:dough",
        "result": {
            "newItemName": "ham:bread", 
            "count": 2,
        }
    },
    "ham:cooked_corn": {
        "material": ("ham:corn", 2),
        "result": ("ham:cooked_corn", 2),
    },
}

BAKE_DATA = dict(BAKE_COMMON_DATA, **BAKE_PIE_DATA)