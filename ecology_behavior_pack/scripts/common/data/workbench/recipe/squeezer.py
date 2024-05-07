SQUEEZER_DATA = {
    "minecraft:apple": "minecraft:apple",
    "ham:butter": {
        "material": {
            1: "ham:sweet_milk",
        },
        "result": "ham:butter"
    },
    "ham:cheese": {
        "material": {
            0: "ham:sweet_milk",
            1: "ham:sweet_milk",
            2: "ham:sweet_milk",
        },
        "result": "ham:cheese"
    },
    "ham:tofu": {
        "material": {
            0: "ham:soy_bean",
            1: "ham:soy_bean",
        },
        "result": {
            "newItemName": "ham:tofu", 
            "count": 3,
        }
    },
    "ham:cooking_oil-soy_bean": {
        "material": {
            0: {
                "newItemName": "ham:soy_bean", 
                "count": 2,
            },
            1: {
                "newItemName": "ham:soy_bean", 
                "count": 2,
            },
            2: {
                "newItemName": "ham:soy_bean", 
                "count": 2,
            },
        },
        "result": {
            "newItemName": "ham:cooking_oil", 
            "count": 3,
        }
    },
    "ham:cooking_oil-corn": {
        "material": {
            0: {
                "newItemName": "ham:corn", 
                "count": 2,
            },
            1: {
                "newItemName": "ham:corn", 
                "count": 2,
            },
            2: {
                "newItemName": "ham:corn", 
                "count": 2,
            },
        },
        "result": {
            "newItemName": "ham:cooking_oil", 
            "count": 2,
        }
    },
}