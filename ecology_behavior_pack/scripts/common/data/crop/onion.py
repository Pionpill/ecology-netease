ONION = {
    "beta": True,
    "seed": 'ham:onion',
    "blockPrefix": 'ham:onion',
    "grow": {
        "stage": (
            {
                "tick": 55,
                "height": (103, 32)
            },
            {
                "tick": 55,
                "height": (14, 32)
            },
            {
                "tick": 56,
                "height": (20, 32)
            },
            {
                "height": (22, 32)
            }
        ),
        "harvest": {
            "count": 1,
            "stage": (1, 2, 3),
        },
        "temperature": {
            "suit": (10, 25),
            "can": (-5, 35)
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
            "sensitivity": 40,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": {
        1: {
            "name": "ham:onion",
            "chance": 100,
            "count": 2
        },
        2: {
            "name": "ham:onion",
            "chance": 100,
            "count": 5
        },
        3: {
            "name": "ham:onion",
            "chance": 100,
            "count": 10
        },
    }
}