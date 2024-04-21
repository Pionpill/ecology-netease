CHILI = {
    "beta": True,
    "seed": 'ham:chili',
    "blockPrefix": 'ham:chili',
    "grow": {
        "stage": (
            {
                "tick": 10,
                "height": (12, 32)
            },
            {
                "tick": 10,
                "height": (20, 32)
            },
            {
                "tick": 13,
                "height": (20, 32)
            },
            {
                "height": (24, 32)
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
            "suit": (40, 80),
            "can": (15, 100)
        },
        "brightness": {
            "suit": (9, 15),
            "can": (5, 15)
        },
        "fertility": {
            "min": 60,
            "sensitivity": 40,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:chili",
            "chance": 100,
            "count": 4
        },
    )
}