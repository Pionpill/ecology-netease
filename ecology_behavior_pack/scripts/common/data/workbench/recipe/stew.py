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

STEW_COMMON_DATA = {
    "minecraft:apple": "minecraft:apple",
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

STEW_DATA = dict(STEW_PORRIDGE_DATA, **STEW_COMMON_DATA)