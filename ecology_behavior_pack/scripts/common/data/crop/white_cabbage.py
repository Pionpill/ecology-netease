WHITE_CABBAGE = {
    "beta": False,
    "seed": 'ham:white_cabbage',
    "blockPrefix": 'ham:white_cabbage',
    "grow": {
        "stage": (
            {
                "tick": 12,
                "height": (6, 32)
            },
            {
                "tick": 12,
                "height": (8, 32)
            },
            {
                "tick": 13,
                "height": (19, 32)
            },
            {
                "height": (26, 32)
            }
        ),
        "harvest": {
            "count": 1,
            "stage": 3,
        },
        "temperature": {
            "suit": (5, 20),
            "can": (-5, 30)
        },
        "rainfall": {
            "suit": (40, 70),
            "can": (20, 100)
        },
        "brightness": {
            "suit": (9, 15),
            "can": (5, 15)
        },
        "fertility": {
            "min": 80,
            "sensitivity": 50,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:white_cabbage",
            "chance": 100,
            "count": 2
        },
    )
}