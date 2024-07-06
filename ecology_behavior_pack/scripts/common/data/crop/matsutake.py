MATSUTAKE = {
    "beta": True,
    "seed": 'ham:matsutake',
    "blockPrefix": 'ham:matsutake',
    "grow": {
        "stage": (
            {
                "tick": 100,
                "height": (8, 32)
            },
            {
                "tick": 100,
                "height": (12, 32)
            },
            {
                "tick": 100,
                "height": (22, 32)
            },
            {
                "height": (22, 32)
            },
        ),
        "harvest": {
            "count": -1,
            "stage": 3,
            "return": 0,
        },
        "temperature": {
            "suit": (15, 25),
            "can": (10, 30)
        },
        "rainfall": {
            "suit": (60, 80),
            "can": (40, 100)
        },
        "brightness": {
            "suit": (4, 12),
            "can": (0, 12)
        },
        "fertility": {
            "min": 100,
            "sensitivity": 50,
            "type": ["fungi"]
        },
        "rain_multiply": 1,
        "period": "none",
    },
    "loot": (
        {
            "name": "ham:matsutake",
            "chance": 100,
            "count": 7
        },
    )
}