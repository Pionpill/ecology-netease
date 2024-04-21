SOYBEAN = {
    "beta": True,
    "seed": 'ham:soy_bean',
    "blockPrefix": 'ham:soy_bean',
    "grow": {
        "stage": (
            {
                "tick": 23,
                "height": (8, 32)
            },
            {
                "tick": 23,
                "height": (18, 32)
            },
            {
                "tick": 24,
                "height": (24, 32)
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
            "suit": (15, 25),
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
            "sensitivity": 70,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:soy_bean",
            "chance": 100,
            "count": 6
        },
    )
}