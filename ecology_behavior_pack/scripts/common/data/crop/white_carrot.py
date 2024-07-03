WHITE_CARROT = {
    "beta": True,
    "seed": 'ham:white_carrot',
    "blockPrefix": 'ham:white_carrot',
    "grow": {
        "stage": (
            {
                "tick": 12,
                "height": (5, 32)
            },
            {
                "tick": 12,
                "height": (11, 32)
            },
            {
                "tick": 12,
                "height": (24, 32)
            },
            {
                "height": (20, 32)
            }
        ),
        "harvest": {
            "count": 1,
            "stage": 3
        },
        "temperature": {
            "suit": (5, 20),
            "can": (0, 30)
        },
        "rainfall": {
            "suit": (50, 80),
            "can": (30, 100)
        },
        "brightness": {
            "suit": (9, 15),
            "can": (5, 15)
        },
        "fertility": {
            "min": 80,
            "sensitivity": 40,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:white_carrot",
            "chance": 100,
            "count": 3
        },
    )
}