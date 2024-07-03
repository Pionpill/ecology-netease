COOK_DATA = {
    "minecraft:apple": {
        "material": {
            4: "minecraft:apple"
        },
        "fixed_material": (1, 0, 0, 0),
        "result": "minecraft:apple",
    },
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
    "ham:raw_cheese_pie": {
        "material": {
            1: "ham:butter",
            3: "ham:cheese",
            4: "minecraft:egg",
            5: "ham:cheese",
            6: "ham:dough",
            7: "ham:dough",
            8: "ham:dough",
        },
        "fixed_material": (1, 3, 1, 1),
        "result": {
            "newItemName": "ham:raw_cheese_pie", 
            "count": 4,
        },
    },
    "ham:raw_corn_pie": {
        "material": {
            1: "ham:cheese",
            3: {
                "newItemName": "ham:corn",
                "count": 2
            },
            4: "ham:butter",
            5: {
                "newItemName": "ham:corn",
                "count": 2
            },
            6: "ham:dough",
            7: "ham:dough",
            8: "ham:dough",
        },
        "fixed_material": (1, 3, 1, 1),
        "result": {
            "newItemName": "ham:raw_corn_pie", 
            "count": 4,
        },
    },
    "ham:raw_apple_pie": {
        "material": {
            0: "minecraft:egg",
            1: "ham:butter",
            2: "minecraft:egg",
            3: "ham:cheese",
            4: {
                "newItemName": "minecraft:apple",
                "count": 4
            },
            5: "ham:cheese",
            6: "ham:dough",
            7: "ham:dough",
            8: "ham:dough",
        },
        "fixed_material": (1, 3, 1, 1),
        "result": {
            "newItemName": "ham:raw_apple_pie", 
            "count": 4,
        },
    },
    "ham:burger_simple": {
        "material": {
            1: "ham:bread",
            3: {
                "newItemName": "ham:cheese",
                "count": 2
            },
            4: {
                "newItemName": "ham:beef_patties",
                "count": 2
            },
            5: "ham:tomato",
            7: "ham:bread",
        },
        "fixed_material": (1, 0, 0, 2),
        "result": {
            "newItemName": "ham:burger_simple", 
            "count": 2, # 饥饿 10
        },
    },
    "ham:burger": {
        "material": {
            0: "ham:lettuce",
            1: "ham:bread",
            2: "ham:onion",
            3: {
                "newItemName": "ham:cheese",
                "count": 2
            },
            4: {
                "newItemName": "ham:beef_patties",
                "count": 2
            },
            5: "ham:tomato",
            6: "ham:salad",
            7: "ham:bread",
            8: "ham:salad",
        },
        "fixed_material": (1, 0, 0, 2),
        "result": {
            "newItemName": "ham:burger", 
            "count": 2, # 饥饿 14
        },
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
}
