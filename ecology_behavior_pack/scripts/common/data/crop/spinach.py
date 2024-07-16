SPINACH = {
    "beta": False,
    "seed": 'ham:spinach_seeds',
    "blockPrefix": 'ham:spinach',
    "grow": {
        "stage": (
            {
                "tick": 12,
                "height": (6, 32)
            },
            {
                "tick": 12,
                "height": (9, 32)
            },
            {
                "height": (13, 32)
            }
        ),
        "harvest": {
            "count": 1,
            "stage": 2,
        },
        "temperature": {
            "suit": (10, 25),
            "can": (0, 30)
        },
        "rainfall": {
            "suit": (60, 80),
            "can": (30, 100)
        },
        "brightness": {
            "suit": (9, 15),
            "can": (5, 15)
        },
        "fertility": {
            "min": 70,
            "sensitivity": 60,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "none"
    },
    "loot": {
        1: {
            "name": "ham:spinach",
            "chance": 100,
            "count": 2
        },
        2: (
            {
                "name": "ham:spinach",
                "chance": 100,
                "count": 3.5
            },
            {
                "name": "ham:spinach_seeds",
                "chance": 100,
                "count": 1.5
            }
        )
    }
}