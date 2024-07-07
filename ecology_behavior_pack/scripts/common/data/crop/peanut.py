PEANUT = {
    "beta": True,
    "seed": 'ham:peanut',
    "blockPrefix": 'ham:peanut',
    "grow": {
        "stage": (
            {
                "tick": 22,
                "height": (9, 32)
            },
            {
                "tick": 22,
                "height": (22, 32)
            },
            {
                "tick": 22,
                "height": (27, 32)
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
            "suit": (15, 35),
            "can": (10, 40)
        },
        "rainfall": {
            "suit": (40, 60),
            "can": (20, 80)
        },
        "brightness": {
            "suit": (9, 15),
            "can": (5, 15)
        },
        "fertility": {
            "min": 90,
            "sensitivity": 70,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:peanut",
            "chance": 100,
            "count": 6
        },
    )
}