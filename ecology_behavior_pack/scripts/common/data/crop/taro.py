TARO = {
    "beta": True,
    "seed": 'ham:taro',
    "blockPrefix": 'ham:taro',
    "grow": {
        "stage": (
            {
                "tick": 37,
                "height": (10, 32)
            },
            {
                "tick": 37,
                "height": (20, 32)
            },
            {
                "tick": 37,
                "height": (27, 32)
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
            "suit": (15, 30),
            "can": (10, 40)
        },
        "rainfall": {
            "suit": (60, 80),
            "can": (40, 100)
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
            "name": "ham:taro",
            "chance": 100,
            "count": 7
        },
    )
}