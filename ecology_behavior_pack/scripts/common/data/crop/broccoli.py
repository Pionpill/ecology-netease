BROCCOLI = {
    "beta": True,
    "seed": 'ham:white_broccoli',
    "blockPrefix": 'ham:broccoli',
    "grow": {
        "stage": (
            {
                "tick": 17,
                "height": (8, 32)
            },
            {
                "tick": 17,
                "height": (10, 32)
            },
            {
                "tick": 17,
                "height": (11, 32)
            },
            {
                "height": (14, 32)
            }
        ),
        "harvest": {
            "count": 1,
            "stage": 3,
        },
        "temperature": {
            "suit": (15, 25),
            "can": (5, 30)
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
            "min": 70,
            "sensitivity": 40,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:white_broccoli",
            "chance": 100,
            "count": 5
        },
        {
            "name": "ham:broccoli",
            "chance": 10,
            "count": 1
        }
    )
}