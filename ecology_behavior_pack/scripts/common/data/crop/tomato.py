TOMATO = {
    "beta": True,
    "seed": 'ham:tomato',
    "blockPrefix": 'ham:tomato',
    "grow": {
        "stage": (
            {
                "tick": 13,
                "height": (14, 32)
            },
            {
                "tick": 13,
                "height": (20, 32)
            },
            {
                "tick": 14,
                "height": (24, 32)
            },
            {
                "height": (34, 32)
            }
        ),
        "harvest": {
            "count": 3,
            "stage": 3,
            "return": 2,
        },
        "temperature": {
            "suit": (20, 30),
            "can": (10, 35)
        },
        "rainfall": {
            "suit": (60, 80),
            "can": (30, 100)
        },
        "brightness": {
            "suit": (9, 15),
            "can": (5, 15)
        },
        "fertility": {
            "min": 100,
            "sensitivity": 80,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:tomato",
            "chance": 100,
            "count": 3
        },
    )
}