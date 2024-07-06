GREEN_BEAN = {
    "beta": True,
    "seed": 'ham:green_bean',
    "blockPrefix": 'ham:green_bean',
    "grow": {
        "stage": (
            {
                "tick": 10,
                "height": (8, 32)
            },
            {
                "tick": 10,
                "height": (18, 32)
            },
            {
                "tick": 10,
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
            "name": "ham:green_bean",
            "chance": 100,
            "count": 4
        },
    )
}