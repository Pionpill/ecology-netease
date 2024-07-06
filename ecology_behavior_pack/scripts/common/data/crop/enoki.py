ENOKI = {
    "beta": True,
    "seed": 'ham:enoki',
    "blockPrefix": 'ham:enoki',
    "grow": {
        "stage": (
            {
                "tick": 20,
                "height": (9, 32)
            },
            {
                "tick": 20,
                "height": (17, 32)
            },
            {
                "height": (23, 32)
            },
        ),
        "harvest": {
            "count": -1,
            "stage": 2,
            "return": 0,
        },
        "temperature": {
            "suit": (10, 25),
            "can": (0, 30)
        },
        "rainfall": {
            "suit": (60, 100),
            "can": (40, 100)
        },
        "brightness": {
            "suit": (4, 12),
            "can": (0, 12)
        },
        "fertility": {
            "min": 100,
            "sensitivity": 40,
            "type": ["fungi"]
        },
        "rain_multiply": 1,
        "period": "none",
    },
    "loot": {
        1: {
            "name": "ham:enoki",
            "chance": 100,
            "count": 2
        },
        2: {
            "name": "ham:enoki",
            "chance": 100,
            "count": 5
        },
    }
}