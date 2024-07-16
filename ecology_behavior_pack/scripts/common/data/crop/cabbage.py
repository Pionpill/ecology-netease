CABBAGE = {
    "beta": False,
    "seed": 'ham:cabbage_seeds',
    "blockPrefix": 'ham:cabbage',
    "grow": {
        "stage": (
            {
                "tick": 17,
                "height": (5, 32)
            },
            {
                "tick": 17,
                "height": (9, 32)
            },
            {
                "tick": 17,
                "height": (7, 32)
            },
            {
                "height": (10, 32)
            }
        ),
        "harvest": {
            "count": 1,
            "stage": 3,
        },
        "temperature": {
            "suit": (15, 25),
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
            "min": 70,
            "sensitivity": 40,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:cabbage",
            "chance": 100,
            "count": 3
        },
        {
            "name": "ham:cabbage_seeds",
            "chance": 100,
            "count": 1.5
        },
    )
}