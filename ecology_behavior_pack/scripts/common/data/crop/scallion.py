SCALLION = {
    "beta": True,
    "seed": 'ham:scallion_seeds',
    "blockPrefix": 'ham:scallion',
    "grow": {
        "stage": (
            {
                "tick": 11,
                "height": (14, 32)
            },
            {
                "tick": 11,
                "height": (26, 32)
            },
            {
                "tick": 11,
                "height": (34, 32)
            },
            {
                "height": (50, 32)
            }
        ),
        "harvest": {
            "count": 1,
            "stage": (2,3)
        },
        "temperature": {
            "suit": (15, 25),
            "can": (0, 35)
        },
        "rainfall": {
            "suit": (40, 80),
            "can": (15, 100)
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
        2: {
            "name": "ham:scallion",
            "chance": 100,
            "count": 2
        },
        3: (
            {
                "name": "ham:scallion",
                "chance": 100,
                "count": 3
            },
            {
                "name": "ham:scallion_seeds",
                "chance": 100,
                "count": 1.5
            }
        )
    }
}