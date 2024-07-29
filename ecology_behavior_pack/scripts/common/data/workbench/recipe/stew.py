from scripts.common.enum.Item import ItemTag

STEW_PORRIDGE_DATA = {
    "ham:porridge": {
        "material": {
            4: ("ham:rice", 3)
        },
        "result": ("ham:porridge", 5) # 3
    },
    "ham:green_bean_porridge": {
        "material": {
            1: ("ham:sugar", 2),
            4: ("ham:green_bean", 7)
        },
        "result": ("ham:green_bean_porridge", 5) # 3
    },
    "ham:red_bean_porridge": {
        "material": {
            1: ("ham:sugar", 2),
            4: ("ham:red_bean", 7)
        },
        "result": ("ham:red_bean_porridge", 5) # 3
    },
    "ham:sweet_potato_porridge": {
        "material": {
            1: ("ham:sugar", 2),
            3: "ham:sweet_potato",
            4: ("ham:rice", 3),
            5: "ham:sweet_potato",
        },
        "result": ("ham:sweet_potato_porridge", 5) # 4
    },
    "ham:vegetable_porridge": {
        "material": {
            1: ("ham:salt", 2),
            3: "ham-tag:" + ItemTag.GREEN,
            4: ("ham:rice", 3),
            5: "ham-tag:" + ItemTag.GREEN,
        },
        "result": ("ham:vegetable_porridge", 5) # 3
    },
    "ham:sorghum_porridge": {
        "material": {
            1: "ham:peanut",
            3: "ham:red_bean",
            4: ("ham:sorghum", 3),
            5: "ham:green_bean",
        },
        "result": ("ham:sorghum_porridge", 5) # 4
    },
    "ham:sweet_potato_yam_porridge": {
        "material": {
            1: ("ham:sugar", 2),
            3: "ham:sweet_potato",
            4: ("ham:rice", 3),
            5: "ham:yam",
        },
        "result": ("ham:sweet_potato_yam_porridge", 5) # 4
    },
    "ham:vegetable_pork_porridge": {
        "material": {
            1: ("ham:salt", 2),
            3: "ham-tag:" + ItemTag.GREEN,
            4: ("ham:rice", 3),
            5: "ham:ground_pork",
        },
        "result": ("ham:vegetable_pork_porridge", 5) # 4
    },
    "ham:red_bean_taro_porridge": {
        "material": {
            0: "ham:sweet_milk",
            1: ("ham:sugar", 2),
            2: "ham:sweet_milk",
            3: "ham:red_bean",
            4: ("ham:rice", 3),
            5: "ham:taro",
        },
        "result": ("ham:red_bean_taro_porridge", 5) # 4
    },
    "ham:corn_pea_porridge": {
        "material": {
            0: "ham:sweet_milk",
            1: ("ham:sugar", 2),
            2: "ham:sweet_milk",
            3: "ham:pea",
            4: ("ham:rice", 3),
            5: "ham:corn",
        },
        "result": ("ham:corn_pea_porridge", 5) # 4
    },
    "ham:yam_fish_porridge": {
        "material": {
            0: "ham:carrot",
            1: ("ham:salt", 2),
            2: ("ham:scallion", 2),
            3: "ham:yam",
            4: ("ham:rice", 3),
            5: "ham-tag:" + ItemTag.FISH,
        },
        "result": ("ham:yam_fish_porridge", 5) # 5
    },
    "ham:lentinula_sausage_porridge": {
        "material": {
            0: "ham:ground_pork",
            1: ("ham:salt", 2),
            2: "ham:scallion",
            3: "ham:raw_sausage",
            4: ("ham:rice", 3),
            5: ("ham:lentinula", 2),
        },
        "result": ("ham:lentinula_sausage_porridge", 5) # 6
    },
    "ham:tomato_beef_porridge": {
        "material": {
            0: "ham:ginger",
            1: ("ham:salt", 2),
            2: "ham:scallion",
            3: "ham:tomato",
            4: ("ham:rice", 3),
            5: "ham:beef",
        },
        "result": ("ham:tomato_beef_porridge", 5) # 6
    },
    "ham:broccoli_porridge": {
        "material": {
            0: "ham:carrot",
            1: ("ham:salt", 2),
            2: "ham:scallion",
            3: ("ham:broccoli", 2),
            4: ("ham:rice", 3),
            5: ("ham:corn", 2),
        },
        "result": ("ham:broccoli_porridge", 5) # 5
    },
}

STEW_NOODLE_DATA = {
    "ham:plain_noodles": {
        "material": {
            0: "ham:salt",
            1: "ham:scallion",
            2: "ham:seasoning",
            4: "ham:noodle"
        },
        "result": "ham:plain_noodles"
    },
    "ham:pork_sauce_noodles": {
        "material": {
            0: "ham:salt",
            1: "ham:scallion",
            2: "ham:seasoning",
            3: "ham:ground_pork",
            4: "ham:noodle",
            5: "ham:lentinula",
        },
        "result": "ham:pork_sauce_noodles"
    },
    "ham:tomato_egg_noodles": {
        "material": {
            0: "ham:salt",
            1: "ham:scallion",
            2: "ham:seasoning",
            3: "ham:tomato",
            4: "ham:noodle",
            5: "minecraft:egg",
        },
        "result": "ham:tomato_egg_noodles"
    },
    "ham:beef_noodles": {
        "material": {
            0: "ham:scallion",
            1: "ham:meal_pack",
            3: "ham:carrot", # 1
            4: "ham:noodle", # 3
            5: "minecraft:beef", # 3
        },
        "result": "ham:beef_noodles" # 9
    },
    "ham:borsch_noodles": {
        "material": {
            0: "ham:carrot", # 1
            1: "ham:tomato_pack",
            2: "ham:celery",
            3: "ham:potato", # 2
            4: "ham:noodle", # 3
            5: "minecraft:beef", # 3
        },
        "result": "ham:borsch_noodles" # 11
    },
    "ham:chili_beef_noodles": {
        "material": {
            0: "ham-tag:" + ItemTag.GREEN, # 1
            1: "ham:chili_pack",
            2: "minecraft:egg", # 1
            3: "ham:carrot", # 1
            4: "ham:noodle", # 3
            5: "minecraft:beef", # 3
        },
        "result": "ham:chili_beef_noodles" # 11
    },
    "ham:corn_thick_noodles": {
        "material": {
            1: "ham:pea", # 1
            3: "ham:corn", # 1
            4: "ham:noodle", # 3
            5: "ham:corn_thick_soup", # 3
        },
        "result": "ham:corn_thick_noodles" # 10
    },
    "ham:mushroom_thick_noodles": {
        "material": {
            1: "ham-tag:" + ItemTag.GREEN, # 1
            3: "ham:ground_pork", # 3
            4: "ham:noodle", # 3
            5: "ham:mushroom_thick_soup", # 3
        },
        "result": "ham:mushroom_thick_noodles" # 12
    },
    "ham:hen_chicken_noodles": {
        "material": {
            1: "ham:mushroom_pack",
            2: "ham:dictyophora", # 1
            3: "minecraft:egg", # 1
            4: "ham:noodle", # 3
            5: "minecraft:chicken", # 3
        },
        "result": "ham:hen_chicken_noodles" # 10
    },
    "ham:lentinula_chicken_noodles": {
        "material": {
            1: "ham:mushroom_pack",
            3: "ham:lentinula", # 1
            4: "ham:noodle", # 3
            5: "minecraft:chicken", # 3
        },
        "result": "ham:lentinula_chicken_noodles" # 9
    },
    "ham:seafood_noodles": {
        "material": {
            0: "ham:wood_ear", # 1
            1: "ham:meal_pack",
            2: "ham:tofu", # 1
            3: "minecraft:egg", # 1
            4: "ham:noodle", # 3
            5: "ham-tag:" + ItemTag.FISH, # 3
        },
        "result": "ham:seafood_noodles" # 11
    },
    "ham:tonkotsu_noodles": {
        "material": {
            0: "ham:wood_ear", # 1
            1: "ham:meal_pack",
            2: "ham:corn", # 1
            3: "minecraft:egg", # 1
            4: "ham:noodle", # 3
            5: "minecraft:porkchop", # 3
        },
        "result": "ham:tonkotsu_noodles" # 11
    },
}

STEW_SOUP_DATA = {
    "ham:corn_thick_soup": {
        "material": {
            0: "ham:sausage", # 3
            1: "ham:butter", # 1
            2: "ham:sweet_milk", # 1
            3: "ham:onion", # 1
            4: "ham:corn", # 1
            5: "ham:potato", # 1
        },
        "result": ("ham:corn_thick_soup", 3) # 3
    },
    "ham:mushroom_thick_soup": {
        "material": {
            0: "ham:sausage", # 3
            1: "ham:butter", # 1
            2: ("ham:sweet_milk", 2), # 1
            3: "ham:button_mushroom", # 1
            4: "ham:flour", # 3
            5: "ham:button_mushroom", # 1
        },
        "result": ("ham:mushroom_thick_soup", 4) # 3
    },
}

STEW_COMMON_DATA = {
    "minecraft:apple": "minecraft:apple",
    "ham:cooked_corn": {
        "material": {
            0: "ham:corn",
            1: "ham:corn",
            2: "ham:corn",
            3: "ham:corn",
            4: "ham:corn",
            5: "ham:corn",
        },
        "result": {
            "newItemName": "ham:cooked_corn", 
            "count": 3,
        }
    },
}

STEW_DATA = {k: v for d in (STEW_PORRIDGE_DATA, STEW_NOODLE_DATA, STEW_SOUP_DATA, STEW_COMMON_DATA) for k, v in d.items()}