BUTTON_MUSHROOM = {
    "beta": False,
    "seed": 'ham:button_mushroom',
    "blockPrefix": 'ham:button_mushroom',
    "grow": {
        "stage": (
            {
                "tick": 10,
                "height": (2, 32)
            },
            {
                "tick": 10,
                "height": (4, 32)
            },
            {
                "tick": 10,
                "height": (5, 32)
            },
            {
                "height": (7, 32)
            }
        ),
        "harvest": {
            "count": -1,
            "stage": 3,
            "return": 0,
        },
        "temperature": {
            "suit": (15, 25),
            "can": (5, 30)
        },
        "rainfall": {
            "suit": (60, 100),
            "can": (40, 100)
        },
        "brightness": {
            "suit": (8, 12),
            "can": (4, 15)
        },
        "fertility": {
            "min": 80,
            "sensitivity": 60,
            "type": ["fungi"]
        },
        "rain_multiply": 2,
        "period": "none",
    },
    "loot": (
        {
            "name": "ham:button_mushroom",
            "chance": 100,
            "count": 4
        },
    )
}