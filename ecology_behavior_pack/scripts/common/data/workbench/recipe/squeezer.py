SQUEEZER_DATA = {
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
                "count": 3,
            },
            1: {
                "newItemName": "ham:soy_bean", 
                "count": 3,
            },
            2: {
                "newItemName": "ham:soy_bean", 
                "count": 3,
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
                "count": 3,
            },
            1: {
                "newItemName": "ham:corn", 
                "count": 3,
            },
            2: {
                "newItemName": "ham:corn", 
                "count": 3,
            },
        },
        "result": {
            "newItemName": "ham:cooking_oil", 
            "count": 2,
        }
    },
    "ham:cooking_oil-peanut": {
        "material": {
            0: "ham:peanut",
            1: "ham:peanut",
            2: "ham:peanut",
        },
        "result": "ham:cooking_oil"
    },
    "ham:cooking_oil-rape_seeds": {
        "material": {
            0: "ham:rape_seeds",
            1: "ham:rape_seeds",
            2: "ham:rape_seeds",
        },
        "result": {
            "newItemName": "ham:cooking_oil", 
            "count": 3,
        }
    },
}