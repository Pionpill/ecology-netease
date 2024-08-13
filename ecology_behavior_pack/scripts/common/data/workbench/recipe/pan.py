from scripts.common.enum.Item import ItemTag


PAN_FRY_DATA = {
    "ham:leek_egg": {
        "material": {
            0: "ham:leek", # 1
            1: "minecraft:egg",
        },
        "fixed_material": (1, 0, 1, 1), # 2
        "result": "ham:leek_egg", # 6
    },
    "ham:fry_bok_choy": {
        "material": {
            1: "ham:chili",
            3: "ham:lentinula", # 1
            4: ("ham:bok_choy", 3), # 3
            5: "ham:garlic",
        },
        "fixed_material": (1, 0, 1, 1), # 2
        "result": "ham:fry_bok_choy", # 8
    },
    "ham:fry_broccoli": {
        "material": {
            1: "ham:chili",
            3: "ham:scallion", # 1
            4: ("ham:broccoli", 3), # 3
            5: "ham:garlic",
        },
        "fixed_material": (1, 0, 1, 1), # 2
        "result": "ham:fry_broccoli", # 8
    },
    "ham:fry_cabbage": {
        "material": {
            1: "ham:chili",
            3: "ham:scallion", # 1
            4: ("ham:cabbage", 3), # 3
            5: "ham:garlic",
        },
        "fixed_material": (1, 0, 1, 1), # 2
        "result": "ham:fry_cabbage", # 8
    },
    "ham:garlic_lettuce": {
        "material": {
            1: "ham:scallion",
            3: ("ham:garlic", 2),
            4: ("ham:lettuce", 3), # 3
            5: ("ham:garlic", 2),
        },
        "fixed_material": (1, 0, 1, 1), # 2
        "result": "ham:garlic_lettuce", # 8
    },
    "ham:tomato_egg": {
        "material": {
            1: "ham:scallion",
            3: "minecraft:egg",
            4: ("ham:tomato", 3), # 3
            5: "minecraft:egg",
        },
        "fixed_material": (1, 1, 1, 1), # 2
        "result": "ham:tomato_egg", # 10
    },
    "ham:onion_potato": {
        "material": {
            1: "ham:scallion",
            3: "ham:onion", # 1
            4: "ham:potato", # 2
            5: "ham:onion", # 1
        },
        "fixed_material": (1, 0, 1, 1), # 2
        "result": "ham:onion_potato", # 8
    },
    "ham:peanut_spinach": {
        "material": {
            1: "ham:simple_pack",
            3: "ham:peanut", # 1
            4: ("ham:spinach", 2), # 2
            5: "ham:wood_ear", # 1
        },
        "fixed_material": (0, 1, 1, 0), # 3
        "result": "ham:peanut_spinach", # 9
    },
    "ham:fry_matsutake": {
        "material": {
            1: "ham:scallion",
            4: ("ham:matsutake", 3), # 3
        },
        "fixed_material": (1, 0, 1, 1), # 2
        "result": "ham:fry_matsutake", # 7
    },
    "ham:pork_eggplant": {
        "material": {
            1: "ham:meal_pack",
            3: "ham:eggplant", # 1
            4: "ham:ground_pork", # 3
            5: "ham:starch", # 1
        },
        "fixed_material": (0, 0, 1, 0), # 2
        "result": ("ham:pork_eggplant", 2), # 9
    },
    "ham:pepper_pork": {
        "material": {
            1: "ham:meal_pack",
            3: "ham:pepper", # 1
            4: "minecraft:porkchop", # 3
            5: "ham:chili", # 1
        },
        "fixed_material": (0, 0, 1, 0), # 2
        "result": "ham:pepper_pork", # 9
    },
    "ham:scallion_mutton": {
        "material": {
            1: "ham:meal_pack",
            3: "ham:scallion", # 1
            4: "minecraft:mutton", # 3
            5: "ham:scallion", # 1
        },
        "fixed_material": (0, 0, 1, 0), # 2
        "result": "ham:scallion_mutton", # 9
    },
    "ham:celery_beef": {
        "material": {
            1: "ham:chili_pack",
            3: "ham:celery", # 1
            4: "minecraft:beef", # 3
            5: "ham:celery", # 1
        },
        "fixed_material": (0, 0, 1, 0), # 2
        "result": "ham:celery_beef", # 9
    },
}

PAN_RICE_DATA = {
    "ham:egg_fired_rice": {
        "material": {
            1: {
                "newItemName": "ham:scallion",
                "count": 1,
            },
            3: {
                "newItemName": "minecraft:egg",
                "count": 1,
            },
            4: {
                "newItemName": "ham:cooked_rice",
                "count": 1,
            },
            5: {
                "newItemName": "minecraft:egg",
                "count": 1,
            }
        },
        "fixed_material": (1, 0, 1, 1),
        "result": {
            "newItemName": "ham:egg_fired_rice", 
            "count": 1,
        }
    },
    "ham:pork_sauce_rice": {
        "material": {
            1: {
                "newItemName": "ham:ground_pork",
                "count": 1,
            },
            3: {
                "newItemName": "ham:scallion",
                "count": 1,
            },
            4: {
                "newItemName": "ham:cooked_rice",
                "count": 1,
            },
            5: {
                "newItemName": "ham:lentinula",
                "count": 1,
            }
        },
        "fixed_material": (1, 0, 1, 1),
        "result": {
            "newItemName": "ham:pork_sauce_rice", 
            "count": 1,
        }
    },
    "ham:curry_pork_rice": {
        "material": {
            0: "ham-tag:" + ItemTag.GREEN, # 1
            1: "minecraft:egg", # 1
            2: "ham:carrot", # 1
            3: "ham:potato", # 2
            4: "ham:cooked_rice", # 4
            5: "minecraft:porkchop" # 3
        },
        "fixed_material": (1, 0, 1, 1),
        "result": "ham:curry_pork_rice" # 16
    },
    "ham:kelp_rice": {
        "material": {
            1: "ham:corn", # 1
            3: "ham:pea", # 1
            4: "ham:cooked_rice", # 4
            5: "minecraft:dried_kelp" # 1
        },
        "fixed_material": (1, 0, 1, 1),
        "result": "ham:kelp_rice" # 11
    },
    "ham:onion_beef_rice": {
        "material": {
            0: "ham:eggplant", # 1
            1: "minecraft:egg", # 1
            2: "ham:broccoli", # 1
            3: "ham:onion", # 1
            4: "ham:cooked_rice", # 4
            5: "minecraft:beef" # 3
        },
        "fixed_material": (1, 0, 1, 1),
        "result": "ham:onion_beef_rice" # 15
    },
    "ham:tomato_egg_rice": {
        "material": {
            3: "ham:tomato", # 1
            4: "ham:cooked_rice", # 4
            5: ("minecraft:egg", 2) # 1
        },
        "fixed_material": (1, 0, 1, 1),
        "result": "ham:tomato_egg_rice" # 11
    },
    "ham:tomato_pork_sauce_rice": {
        "material": {
            0: "ham:pea", # 1
            1: "ham:ground_pork", # 3
            2: "ham:corn", # 1
            3: "ham:tomato", # 1
            4: "ham:cooked_rice", # 4
            5: ("minecraft:egg", 2) # 1
        },
        "fixed_material": (1, 0, 1, 1),
        "result": "ham:tomato_pork_sauce_rice" # 16
    },
}

PAN_COMMON_DATA = {
    "ham:beef_patties": {
        "material": {
            "newItemName": "ham:raw_beef_patties",
            "count": 1,
        },
        "fixed_material": (1, 0, 0, 1),
        "result": {
            "newItemName": "ham:beef_patties", 
            "count": 1,
        }
    },
    "ham:sausage": {
        "material": {
            "newItemName": "ham:raw_sausage",
            "count": 1,
        },
        "fixed_material": (0, 0, 0, 0),
        "result": {
            "newItemName": "ham:sausage", 
            "count": 1,
        }
    },
}

PAN_DATA = {k: v for d in (PAN_COMMON_DATA, PAN_FRY_DATA, PAN_RICE_DATA) for k, v in d.items()}