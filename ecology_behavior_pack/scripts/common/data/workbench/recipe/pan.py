PAN_DATA = {
    "minecraft:apple": "minecraft:apple",
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
    "ham:yangzhou_fried_rice": {
        "material": {
            0: {
                "newItemName": "ham:lentinula",
                "count": 1,
            },
            1: {
                "newItemName": "ham:corn",
                "count": 2,
            },
            2: {
                "newItemName": "ham:scallion",
                "count": 1,
            },
            3: {
                "newItemName": "ham:sausage",
                "count": 2,
            },
            4: {
                "newItemName": "ham:cooked_rice",
                "count": 2,
            },
            5: {
                "newItemName": "minecraft:egg",
                "count": 3,
            }
        },
        "fixed_material": (1, 0, 1, 1),
        "result": {
            "newItemName": "ham:yangzhou_fried_rice", 
            "count": 2,
        }
    },
    "ham:mapo_tofu": {
        "material": {
            0: "ham:starch",
            1: "ham:ground_pork",
            2: "ham:scallion",
            3: "ham:chili",
            4: {
                "newItemName": "ham:tofu",
                "count": 3,
            },
            5: "ham:chili",
        },
        "fixed_material": (1, 0, 1, 2),
        "result": {
            "newItemName": "ham:mapo_tofu", 
            "count": 2, # 6
        }
    }
}
