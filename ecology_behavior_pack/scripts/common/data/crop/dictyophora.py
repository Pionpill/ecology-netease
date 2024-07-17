DICTYOPHORA = {
    "beta": True,
    "seed": 'ham:dictyophora',
    "blockPrefix": 'ham:dictyophora',
    "grow": {
        "stage": (
            {
                "tick": 30,
                "height": (6, 32)
            },
            {
                "tick": 30,
                "height": (6, 32)
            },
            {
                "height": (8, 32)
            },
        ),
        "harvest": {
            "count": -1,
            "stage": 2,
            "return": 0,
        },
        "temperature": {
            "suit": (20, 30),
            "can": (15, 35)
        },
        "rainfall": {
            "suit": (60, 90),
            "can": (40, 100)
        },
        "brightness": {
            "suit": (4, 12),
            "can": (0, 12)
        },
        "fertility": {
            "min": 120,
            "sensitivity": 50,
            "type": ["fungi"]
        },
        "rain_multiply": 1,
        "period": "none",
    },
    "loot": {
        1: {
            "name": "ham:dictyophora",
            "chance": 100,
            "count": 2
        },
        2: {
            "name": "ham:dictyophora",
            "chance": 100,
            "count": 3
        },
    }
}