SUGARCANE = {
    "beta": True,
    "seed": 'ham:sugarcane',
    "blockPrefix": 'ham:sugarcane',
    "grow": {
        "stage": (
            {
                "tick": 50,
                "height": (18, 32)
            },
            {
                "tick": 50,
                "height": (32, 32)
            },
            {
                "tick": 50,
                "height": (54, 32)
            },
            {
                "height": (108, 32)
            }
        ),
        "harvest": {
            "count": 1,
            "stage": 3
        },
        "temperature": {
            "suit": (25, 35),
            "can": (15, 45)
        },
        "rainfall": {
            "suit": (50, 80),
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
            "name": "ham:sugarcane",
            "chance": 100,
            "count": 6
        },
    )
}