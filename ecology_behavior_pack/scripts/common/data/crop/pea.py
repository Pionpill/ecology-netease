PEA = {
    "beta": True,
    "seed": 'ham:pea',
    "blockPrefix": 'ham:pea',
    "grow": {
        "stage": (
            {
                "tick": 12,
                "height": (11, 32)
            },
            {
                "tick": 12,
                "height": (16, 32)
            },
            {
                "tick": 12,
                "height": (21, 32)
            },
            {
                "height": (24, 32)
            }
        ),
        "harvest": {
            "count": 1,
            "stage": 3
        },
        "temperature": {
            "suit": (10, 20),
            "can": (5, 30)
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
            "min": 80,
            "sensitivity": 80,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:pea",
            "chance": 100,
            "count": 4
        },
    )
}