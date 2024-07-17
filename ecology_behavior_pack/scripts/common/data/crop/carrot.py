CARROT = {
    "beta": True,
    "seed": 'ham:carrot',
    "blockPrefix": 'ham:carrot',
    "grow": {
        "stage": (
            {
                "tick": 17,
                "height": (9, 32)
            },
            {
                "tick": 17,
                "height": (12, 32)
            },
            {
                "tick": 17,
                "height": (23, 32)
            },
            {
                "height": (23, 32)
            }
        ),
        "harvest": {
            "count": 1,
            "stage": 3
        },
        "temperature": {
            "suit": (10, 25),
            "can": (5, 35)
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
            "min": 90,
            "sensitivity": 50,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:carrot",
            "chance": 100,
            "count": 3
        },
    )
}