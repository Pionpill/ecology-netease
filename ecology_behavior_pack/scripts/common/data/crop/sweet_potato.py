SWEET_POTATO = {
    "beta": True,
    "seed": 'ham:sweet_potato',
    "blockPrefix": 'ham:sweet_potato',
    "grow": {
        "stage": (
            {
                "tick": 20,
                "height": (9, 32)
            },
            {
                "tick": 20,
                "height": (19, 32)
            },
            {
                "tick": 20,
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
            "suit": (15, 35),
            "can": (10, 40)
        },
        "rainfall": {
            "suit": (30, 60),
            "can": (10, 80)
        },
        "brightness": {
            "suit": (9, 15),
            "can": (5, 15)
        },
        "fertility": {
            "min": 90,
            "sensitivity": 80,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:sweet_potato",
            "chance": 100,
            "count": 4
        },
    )
}