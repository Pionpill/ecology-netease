from scripts.common.enum.Item import ItemTag

COOK_PIE_DATA = {
    "ham:raw_corn_pie": {
        "material": {
            4: ("ham:butter", 2),
            6: ("ham:corn", 3),
            7: ("ham:dough", 4),
            8: ("ham:corn", 3),
        },
        "fixed_material": (1, 1, 1, 1),
        "result": ("ham:raw_corn_pie", 6), # 5
    },
    "ham:raw_sweet_potato_pie": {
        "material": {
            4: ("ham:butter", 2),
            6: "ham:sweet_potato",
            7: ("ham:dough", 4),
            8: "ham:sweet_potato",
        },
        "fixed_material": (1, 1, 1, 1),
        "result": ("ham:raw_sweet_potato_pie", 6), # 5
    },
    "ham:raw_taro_pie": {
        "material": {
            4: ("ham:butter", 2),
            6: "ham:taro",
            7: ("ham:dough", 4), 
            8: "ham:taro",
        },
        "fixed_material": (1, 1, 1, 1),
        "result": ("ham:raw_taro_pie", 6), # 5
    },
    "ham:raw_cheese_pie": {
        "material": {
            4: ("ham:butter", 3),
            6: ("ham:cheese", 3),
            7: ("ham:dough", 4),
            8: ("minecraft:egg", 3),
        },
        "fixed_material": (1, 3, 2, 1),
        "result": ("ham:raw_cheese_pie", 6), # 7
    },
    "ham:raw_carrot_pie": {
        "material": {
            4: ("ham:butter", 3),
            6: ("ham:carrot", 6),
            7: ("ham:dough", 4),
            8: ("minecraft:egg", 3),
        },
        "fixed_material": (1, 3, 2, 1),
        "result": ("ham:raw_carrot_pie", 6), # 7
    },
    "ham:raw_strawberry_pie": {
        "material": {
            4: ("ham:butter", 3),
            6: ("ham:strawberry", 6),
            7: ("ham:dough", 4),
            8: ("minecraft:egg", 3),
        },
        "fixed_material": (1, 3, 2, 1),
        "result": ("ham:raw_strawberry_pie", 6), # 7
    },
    "ham:raw_apple_pie": {
        "material": {
            4: ("ham:butter", 3),
            6: ("minecraft:apple", 4),
            7: ("ham:dough", 4),
            8: ("minecraft:egg", 3),
        },
        "fixed_material": (1, 3, 2, 1),
        "result": ("ham:raw_apple_pie", 6), # 7
    },
    "ham:raw_potato_beef_pie": {
        "material": {
            1: ("ham:butter", 3),
            3: "ham:corn_thick_soup",
            4: "ham:onion",
            5: "ham:cheese",
            6: ("minecraft:beef", 2),
            7: ("ham:dough", 4),
            8: ("ham:potato", 3),
        },
        "fixed_material": (3, 1, 3, 3),
        "result": ("ham:raw_potato_beef_pie", 6) # 9
    },
    "ham:raw_mushroom_pork_pie": {
        "material": {
            1: ("ham:butter", 3),
            3: ("ham:salad", 2),
            4: "ham:onion",
            5: "ham:cheese",
            6: ("ham:ground_pork", 2),
            7: ("ham:dough", 4),
            8: "ham:mushroom_thick_soup",
        },
        "fixed_material": (3, 1, 3, 3),
        "result": ("ham:raw_mushroom_pork_pie", 6) # 9
    },
    "ham:raw_corn_chicken_pie": {
        "material": {
            1: ("ham:butter", 3),
            3: ("ham:pea", 3),
            4: ("ham:sweet_milk", 3),
            5: "ham:cheese",
            6: ("minecraft:chicken", 2),
            7: ("ham:dough", 4),
            8: "ham:corn_thick_soup",
        },
        "fixed_material": (3, 1, 3, 3),
        "result": ("ham:raw_corn_chicken_pie", 6) # 9
    },
}

COOK_FAST_DATA = {
    "ham:cod_burger": {
        "material": {
            1: "ham:bread", # 3
            3: "ham:cheese", # 2
            4: ("minecraft:cooked_cod", 2), # 6
            5: "ham:tomato", # 1
            7: "ham:bread", # 3
        },
        "fixed_material": (1, 0, 0, 2),
        "result": ("ham:cod_burger", 2), # 7
    },
    "ham:chicken_burger": {
        "material": {
            1: "ham:bread", # 3
            3: ("ham:lettuce", 2), # 1
            4: ("minecraft:cooked_chicken", 2), # 6
            5: "ham:tomato", # 1
            7: "ham:bread", # 3
        },
        "fixed_material": (1, 0, 0, 2),
        "result": ("ham:chicken_burger", 2), # 7
    },
    "ham:beef_burger": {
        "material": {
            1: "ham:bread", # 3
            3: ("ham:salad", 2), # 1
            4: ("ham:beef_patties", 2), # 5
            5: "ham:tomato", # 1
            7: "ham:bread", # 3
        },
        "fixed_material": (1, 0, 0, 2),
        "result": ("ham:beef_burger", 2), # 7
    },
    "ham:double_beef_burger": {
        "material": {
            0: "ham:lettuce", # 1
            1: "ham:bread", # 3
            2: "ham:onion", # 1
            3: ("ham:cheese", 2), # 2
            4: ("ham:beef_patties", 5), # 5
            5: "ham:tomato", # 1
            6: "ham:salad", # 1
            7: "ham:bread", # 3
            8: "ham:salad", # 1
        },
        "fixed_material": (1, 0, 0, 2),
        "result": ("ham:double_beef_burger", 2), # 12
    },
    "ham:hot_dog": {
        "material": {
            1: "ham:lettuce",
            3: "ham:bread",
            4: "ham:sausage",
            5: "ham:bread",
            7: "ham:salad",
        },
        "fixed_material": (1, 1, 0, 2),
        "result": "ham:hot_dog", # 12
    },
}

COOK_COMMON_DATA = {
    "ham:ground_pork": {
        "material": {
            3: "minecraft:porkchop",
            4: "minecraft:porkchop",
            5: "minecraft:porkchop"
        },
        "fixed_material": (1, 0, 0, 1),
        "result": {
            "newItemName": "ham:ground_pork", 
            "count": 6,
        },
    },
    "ham:raw_beef_patties": {
        "material": {
            3: "minecraft:beef",
            4: "minecraft:beef",
            5: "minecraft:beef"
        },
        "fixed_material": (1, 0, 0, 1),
        "result": {
            "newItemName": "ham:raw_beef_patties", 
            "count": 6,
        },
    },
    "ham:sweet_milk": {
        "material": {
            4: "minecraft:milk_bucket",
        },
        "fixed_material": (0, 2, 0, 0),
        "result": {
            "newItemName": "ham:sweet_milk", 
            "count": 3,
        },
    },
    "ham:raw_sausage": {
        "material": {
            3: "ham:ground_pork",
            4: "ham:starch",
            5: "ham:ground_pork",
        },
        "fixed_material": (2, 0, 0, 3),
        "result": {
            "newItemName": "ham:raw_sausage", 
            "count": 3,
        },
    },
    "ham:dough": {
        "material": {
            0: "ham:flour",
            1: "ham:flour",
            2: "ham:flour",
            3: "ham:flour",
            4: "minecraft:water_bucket",
            5: "ham:flour",
            6: "ham:flour",
            7: "ham:flour",
            8: "ham:flour",
        },
        "fixed_material": (0, 0, 0, 0),
        "result": {
            "newItemName": "ham:dough", 
            "count": 6,
        },
    },
    "ham:noodle": {
        "material": {
            0: "ham:dough",
            2: "ham:dough",
            3: "ham:dough",
            5: "ham:dough",
            6: "ham:dough",
            8: "ham:dough",
        },
        "fixed_material": (2, 0, 0, 0),
        "result": {
            "newItemName": "ham:noodle", 
            "count": 8,
        },
    },
    "ham:salad": {
        "material": {
            4: "minecraft:egg",
        },
        "fixed_material": (0, 1, 3, 0),
        "result": {
            "newItemName": "ham:salad", 
            "count": 6,
        },
    },
    "ham:raw_buns": {
        "material": {
            0: "ham:dough",
            1: "ham:dough",
            2: "ham:dough",
            3: "ham:scallion",
            4: "ham:ground_pork",
            5: "ham:scallion",
            6: "ham:dough",
            7: "ham:dough",
            8: "ham:dough",
        },
        "fixed_material": (3, 2, 3, 3),
        "result": {
            "newItemName": "ham:raw_buns", 
            "count": 9,
        },
    },
    "ham:sugar-sorghum": {
        "material": {
            3: "ham:sorghum",
            4: "ham:sorghum",
            5: "ham:sorghum",
        },
        "fixed_material": (0, 0, 0, 0),
        "result": {
            "newItemName": "ham:sugar", 
            "count": 3, # 饥饿 1
        }
    },
    "ham:sugar-beet_root": {
        "material": {
            3: "ham:beet_root",
            4: "ham:beet_root",
            5: "ham:beet_root",
        },
        "fixed_material": (0, 0, 0, 0),
        "result": {
            "newItemName": "ham:sugar", 
            "count": 3, # 饥饿 1
        }
    },
    "ham:sugar-sugarcane": {
        "material": {
            3: "ham:sugarcane",
            4: "ham:sugarcane",
            5: "ham:sugarcane",
        },
        "fixed_material": (0, 0, 0, 0),
        "result": {
            "newItemName": "ham:sugar", 
            "count": 3, # 饥饿 1
        }
    },
    "minecraft:wheat": {
        "material": {
            4: "ham:wheat_plant",
        },
        "fixed_material": (0, 0, 0, 0),
        "result": "minecraft:wheat", # 2
    },
    "minecraft:potato": {
        "material": {
            4: "ham:potato",
        },
        "fixed_material": (0, 0, 0, 0),
        "result": "minecraft:potato", # 2
    },
    "minecraft:carrot": {
        "material": {
            4: "ham:carrot",
        },
        "fixed_material": (0, 0, 0, 0),
        "result": "minecraft:carrot", # 1.5
    },
    "minecraft:beetroot": {
        "material": {
            4: "ham:beet_root",
        },
        "fixed_material": (0, 0, 0, 0),
        "result": "minecraft:beetroot", # 1.5
    },
    "minecraft:sugar_cane": {
        "material": {
            4: "ham:sugarcane",
        },
        "fixed_material": (0, 0, 0, 0),
        "result": "minecraft:sugar_cane", # 1.5
    },
    "minecraft:sugar": {
        "material": {
            4: "ham:sugar",
        },
        "fixed_material": (0, 0, 0, 0),
        "result": "minecraft:sugar", # 1.5
    },
    "minecraft:paper": {
        "material": {
            0: "ham:straw",
            1: "ham:straw",
            2: "ham:straw",
            3: "ham:straw",
            4: "minecraft:water_bucket",
            5: "ham:straw",
            6: "ham:straw",
            7: "ham:straw",
            8: "ham:straw",
        },
        "fixed_material": (0, 0, 0, 0),
        "result": "minecraft:paper", # 1.5
    },
    "ham:simple_pack": {
        "material": {
            4: "ham:scallion"
        },
        "fixed_material": (1, 0, 0, 1),
        "result": "ham:simple_pack"
    },
    "ham:meal_pack": {
        "material": {
            3: "ham:ginger",
            4: "ham:scallion",
            5: "ham:garlic",
        },
        "fixed_material": (1, 0, 0, 1),
        "result": "ham:meal_pack"
    },
    "ham:tomato_pack": {
        "material": {
            3: "ham:tomato",
            4: "ham:scallion",
            5: "ham:garlic",
        },
        "fixed_material": (1, 1, 0, 1),
        "result": "ham:tomato_pack"
    },
    "ham:mushroom_pack": {
        "material": {
            3: "ham:lentinula",
            4: "ham:scallion",
            5: "ham:garlic",
        },
        "fixed_material": (1, 0, 0, 1),
        "result": "ham:mushroom_pack"
    },
    "ham:chili_pack": {
        "material": {
            3: "ham:chili_powder",
            4: "ham:scallion",
            5: "ham:garlic",
        },
        "fixed_material": (1, 0, 0, 1),
        "result": "ham:chili_pack"
    },
}

COOK_DATA = {k: v for d in (COOK_COMMON_DATA, COOK_PIE_DATA, COOK_FAST_DATA) for k, v in d.items()}