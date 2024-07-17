LEEK = {
    "beta": False,
    "seed": 'ham:leek_seeds',
    "blockPrefix": 'ham:leek',
    "grow": {
        "stage": (
            {
                "tick": 17,
                "height": (7, 32)
            },
            {
                "tick": 17,
                "height": (14, 32)
            },
            {
                "height": (24, 32)
            }
        ),
        "harvest": {
            "count": 10,
            "stage": 2,
            "return": 0,
        },
        "temperature": {
            "suit": (15, 25),
            "can": (5, 30)
        },
        "rainfall": {
            "suit": (40, 80),
            "can": (20, 100)
        },
        "brightness": {
            "suit": (9, 15),
            "can": (5, 15)
        },
        "fertility": {
            "min": 60,
            "sensitivity": 40,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "none"
    },
    "loot": {
        1: {
            "name": "ham:leek",
            "chance": 100,
            "count": 2
        },
        2: (
            {
                "name": "ham:leek",
                "chance": 100,
                "count": 4
            },
            {
                "name": "ham:leek_seeds",
                "chance": 100,
                "count": 1.5
            }
        ),
    }
}