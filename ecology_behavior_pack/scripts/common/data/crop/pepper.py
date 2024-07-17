PEPPER = {
    "beta": True,
    "seed": 'ham:pepper',
    "blockPrefix": 'ham:pepper',
    "grow": {
        "stage": (
            {
                "tick": 13,
                "height": (6, 32)
            },
            {
                "tick": 13,
                "height": (14, 32)
            },
            {
                "tick": 14,
                "height": (24, 32)
            },
            {
                "height": (30, 32)
            }
        ),
        "harvest": {
            "count": 3,
            "stage": 3,
            "return": 2,
        },
        "temperature": {
            "suit": (20, 30),
            "can": (10, 40)
        },
        "rainfall": {
            "suit": (50, 80),
            "can": (15, 90)
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
            "name": "ham:pepper",
            "chance": 100,
            "count": 3
        },
    )
}