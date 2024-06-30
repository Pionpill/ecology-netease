POTATO = {
    "beta": True,
    "seed": 'ham:potato',
    "blockPrefix": 'ham:potato',
    "grow": {
        "stage": (
            {
                "tick": 17,
                "height": (8, 32)
            },
            {
                "tick": 17,
                "height": (21, 32)
            },
            {
                "tick": 17,
                "height": (26, 32)
            },
            {
                "height": (30, 32)
            }
        ),
        "harvest": {
            "count": 1,
            "stage": 3
        },
        "temperature": {
            "suit": (5, 25),
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
            "sensitivity": 100,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:potato",
            "chance": 100,
            "count": 4
        },
    )
}