STRAWBERRY = {
    "beta": True,
    "seed": 'ham:strawberry',
    "blockPrefix": 'ham:strawberry',
    "grow": {
        "stage": (
            {
                "tick": 23,
                "height": (2, 32)
            },
            {
                "tick": 23,
                "height": (6, 32)
            },
            {
                "tick": 23,
                "height": (7, 32)
            },
            {
                "height": (7, 32)
            }
        ),
        "harvest": {
            "count": 3,
            "stage": 3,
            "return": 2,
        },
        "temperature": {
            "suit": (10, 25),
            "can": (0, 30)
        },
        "rainfall": {
            "suit": (60, 70),
            "can": (30, 90)
        },
        "brightness": {
            "suit": (9, 15),
            "can": (5, 15)
        },
        "fertility": {
            "min": 100,
            "sensitivity": 60,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:strawberry",
            "chance": 100,
            "count": 5
        },
    )
}