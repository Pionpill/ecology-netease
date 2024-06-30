WHEAT = {
    "beta": True,
    "seed": 'ham:wheat_seeds',
    "blockPrefix": 'ham:wheat',
    "grow": {
        "stage": (
            {
                "tick": 17,
                "height": (8, 32)
            },
            {
                "tick": 17,
                "height": (21, 32)
            },
            {
                "tick": 17,
                "height": (26, 32)
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
            "suit": (10, 25),
            "can": (0, 30)
        },
        "rainfall": {
            "suit": (40, 80),
            "can": (20, 100)
        },
        "brightness": {
            "suit": (9, 15),
            "can": (5, 15)
        },
        "fertility": {
            "min": 90,
            "sensitivity": 100,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:wheat_plant",
            "chance": 100,
            "count": 2
        },
        {
            "name": "ham:wheat_seeds",
            "chance": 100,
            "count": 1.5
        },
    )
}