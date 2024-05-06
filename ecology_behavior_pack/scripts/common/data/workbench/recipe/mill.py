MILL_DATA = {
    "minecraft:apple": "minecraft:apple",
    "ham:seasoning": {
        "material": {
            "newItemName": "ham:herb",
            "count": 3,
        },
        "result": {
            0: {
                "newItemName": "ham:seasoning",
                "count": 3,
            },
            1: "ham:straw"
        }
    },
    "ham:chili_powder": {
        "material": {
            0: "ham:chili"
        },
        "result": {
            0: "ham:chili_powder"
        }
    },
    "ham:rice": {
        "material": "ham:rice_plant",
        "result": {
            0: {
                "newItemName": "ham:rice",
                "count": 2,
            },
            1: "ham:straw",
        }
    },
    "ham:starch": {
        "material": "ham:rice",
        "result": {
            "newItemName": "ham:starch",
            "count": 2,
        }
    },
    "ham:flour": {
        "material": "minecraft:wheat",
        "result": {
            "newItemName": "ham:flour",
            "count": 1,
        }
    }
}
