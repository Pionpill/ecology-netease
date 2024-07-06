RED_BEAN = {
    "beta": True,
    "seed": 'ham:red_bean',
    "blockPrefix": 'ham:red_bean',
    "grow": {
        "stage": (
            {
                "tick": 17,
                "height": (8, 32)
            },
            {
                "tick": 17,
                "height": (18, 32)
            },
            {
                "tick": 17,
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
            "suit": (20, 30),
            "can": (10, 40)
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
            "sensitivity": 40,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:red_bean",
            "chance": 100,
            "count": 6
        },
    )
}