CORN = {
    "beta": True,
    "seed": 'ham:corn',
    "blockPrefix": 'ham:corn',
    "grow": {
        "stage": (
            {
                "tick": 20,
                "height": (26, 32)
            },
            {
                "tick": 20,
                "height": (42, 32)
            },
            {
                "tick": 20,
                "height": (64, 32)
            },
            {
                "height": (70, 32)
            }
        ),
        "harvest": {
            "count": 1,
            "stage": 3
        },
        "temperature": {
            "suit": (15, 30),
            "can": (5, 40)
        },
        "rainfall": {
            "suit": (40, 100),
            "can": (15, 100)
        },
        "brightness": {
            "suit": (9, 15),
            "can": (5, 15)
        },
        "fertility": {
            "min": 100,
            "sensitivity": 110,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:corn",
            "chance": 100,
            "count": 6
        },
    )
}