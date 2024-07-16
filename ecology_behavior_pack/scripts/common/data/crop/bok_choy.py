BOK_CHOY = {
    "beta": False,
    "seed": 'ham:bok_choy_seeds',
    "blockPrefix": 'ham:bok_choy',
    "grow": {
        "stage": (
            {
                "tick": 10,
                "height": (14, 32)
            },
            {
                "tick": 10,
                "height": (20, 32)
            },
            {
                "height": (24, 32)
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
            "can": (40, 100)
        },
        "brightness": {
            "suit": (9, 15),
            "can": (5, 15)
        },
        "fertility": {
            "min": 60,
            "sensitivity": 60,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": {
        1: {
            "name": "ham:bok_choy",
            "chance": 100,
            "count": 2
        },
        2: (
            {
            "name": "ham:bok_choy",
            "chance": 100,
            "count": 3
            },
            {
            "name": "ham:bok_choy_seeds",
            "chance": 100,
            "count": 1.5
            },
        ),
    }
}