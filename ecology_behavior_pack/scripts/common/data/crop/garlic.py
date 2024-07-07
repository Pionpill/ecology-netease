GARLIC = {
    "beta": True,
    "seed": 'ham:garlic',
    "blockPrefix": 'ham:garlic',
    "grow": {
        "stage": (
            {
                "tick": 25,
                "height": (11, 32)
            },
            {
                "tick": 25,
                "height": (27, 32)
            },
            {
                "height": (28, 32)
            }
        ),
        "harvest": {
            "count": 1,
            "stage": 2
        },
        "temperature": {
            "suit": (10, 25),
            "can": (0, 30)
        },
        "rainfall": {
            "suit": (50, 70),
            "can": (20, 80)
        },
        "brightness": {
            "suit": (9, 15),
            "can": (5, 15)
        },
        "fertility": {
            "min": 60,
            "sensitivity": 20,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:garlic",
            "chance": 100,
            "count": 9
        },
    )
}