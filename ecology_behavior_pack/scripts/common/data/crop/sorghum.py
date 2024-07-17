SORGHUM = {
    "beta": True,
    "seed": 'ham:sorghum',
    "blockPrefix": 'ham:sorghum',
    "grow": {
        "stage": (
            {
                "tick": 23,
                "height": (24, 32)
            },
            {
                "tick": 23,
                "height": (32, 32)
            },
            {
                "tick": 23,
                "height": (64, 32)
            },
            {
                "height": (80, 32)
            }
        ),
        "harvest": {
            "count": 1,
            "stage": 3
        },
        "temperature": {
            "suit": (20, 30),
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
            "min": 100,
            "sensitivity": 90,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:sorghum",
            "chance": 100,
            "count": 5
        },
    )
}