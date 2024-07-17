RAPE_FLOWER = {
    "beta": True,
    "seed": 'ham:rape_seeds',
    "blockPrefix": 'ham:rape_flower',
    "grow": {
        "stage": (
            {
                "tick": 15,
                "height": (6, 32)
            },
            {
                "tick": 15,
                "height": (10, 32)
            },
            {
                "tick": 15,
                "height": (32, 32)
            },
            {
                "height": (41, 32)
            }
        ),
        "harvest": {
            "count": 1,
            "stage": 3,
        },
        "temperature": {
            "suit": (10, 25),
            "can": (5, 30)
        },
        "rainfall": {
            "suit": (50, 80),
            "can": (20, 90)
        },
        "brightness": {
            "suit": (9, 15),
            "can": (5, 15)
        },
        "fertility": {
            "min": 80,
            "sensitivity": 60,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:rape_seeds",
            "chance": 100,
            "count": 4
        },
        {
            "name": "ham:straw",
            "chance": 100,
            "count": 1
        },
    )
}