YAM = {
    "beta": True,
    "seed": 'ham:yam',
    "blockPrefix": 'ham:yam',
    "grow": {
        "stage": (
            {
                "tick": 30,
                "height": (8, 32)
            },
            {
                "tick": 30,
                "height": (8, 32)
            },
            {
                "tick": 30,
                "height": (14, 32)
            },
            {
                "height": (20, 32)
            }
        ),
        "harvest": {
            "count": 1,
            "stage": 3
        },
        "temperature": {
            "suit": (20, 35),
            "can": (10, 40)
        },
        "rainfall": {
            "suit": (50, 70),
            "can": (30, 90)
        },
        "brightness": {
            "suit": (9, 15),
            "can": (5, 15)
        },
        "fertility": {
            "min": 80,
            "sensitivity": 60,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:yam",
            "chance": 100,
            "count": 6
        },
    )
}