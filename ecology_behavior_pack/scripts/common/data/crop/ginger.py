GINGER = {
    "beta": True,
    "seed": 'ham:ginger',
    "blockPrefix": 'ham:ginger',
    "grow": {
        "stage": (
            {
                "tick": 40,
                "height": (8, 32)
            },
            {
                "tick": 40,
                "height": (15, 32)
            },
            {
                "tick": 40,
                "height": (23, 32)
            },
            {
                "height": (29, 32)
            }
        ),
        "harvest": {
            "count": 1,
            "stage": 3
        },
        "temperature": {
            "suit": (15, 30),
            "can": (5, 35)
        },
        "rainfall": {
            "suit": (50, 70),
            "can": (30, 100)
        },
        "brightness": {
            "suit": (9, 15),
            "can": (5, 15)
        },
        "fertility": {
            "min": 70,
            "sensitivity": 20,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:ginger",
            "chance": 100,
            "count": 6
        },
    )
}