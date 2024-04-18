EGGPLANT = {
    "beta": True,
    "seed": 'ham:eggplant',
    "blockPrefix": 'ham:eggplant',
    "grow": {
        "stage": (
            {
                "tick": 3,
                "height": (13, 32)
            },
            {
                "tick": 3,
                "height": (24, 32)
            },
            {
                "tick": 3,
                "height": (37, 32)
            },
            {
                "height": (44, 32)
            }
        ),
        "harvest": {
            "count": 3,
            "stage": 3,
            "return": 2,
        },
        "temperature": {
            "suit": (15, 30),
            "can": (5, 40)
        },
        "rainfall": {
            "suit": (50, 80),
            "can": (15, 100)
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
            "name": "ham:eggplant",
            "chance": 100,
            "count": 2
        },
    )
}