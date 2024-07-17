BEET = {
    "beta": False,
    "seed": 'ham:beet_root',
    "blockPrefix": 'ham:beet',
    "grow": {
        "stage": (
            {
                "tick": 14,
                "height": (12, 32)
            },
            {
                "tick": 14,
                "height": (14, 32)
            },
            {
                "height": (21, 32)
            }
        ),
        "harvest": {
            "count": 1,
            "stage": 2,
        },
        "temperature": {
            "suit": (15, 25),
            "can": (0, 30)
        },
        "rainfall": {
            "suit": (60, 80),
            "can": (40, 100)
        },
        "brightness": {
            "suit": (9, 15),
            "can": (5, 15)
        },
        "fertility": {
            "min": 80,
            "sensitivity": 60,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:beet_root",
            "chance": 100,
            "count": 4
        },
        {
            "name": "ham:beet_leaf",
            "chance": 100,
            "count": 1
        },
    )
}