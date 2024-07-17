CELERY = {
    "beta": False,
    "seed": 'ham:celery_seeds',
    "blockPrefix": 'ham:celery',
    "grow": {
        "stage": (
            {
                "tick": 35,
                "height": (6, 32)
            },
            {
                "tick": 35,
                "height": (10, 32)
            },
            {
                "height": (17, 32)
            }
        ),
        "harvest": {
            "count": 1,
            "stage": 2,
        },
        "temperature": {
            "suit": (15, 20),
            "can": (5, 25)
        },
        "rainfall": {
            "suit": (50, 80),
            "can": (30, 100)
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
    "loot": {
        1: {
            "name": "ham:celery",
            "chance": 100,
            "count": 3
        },
        2: (
            {
                "name": "ham:celery",
                "chance": 100,
                "count": 6
            },
            {
                "name": "ham:celery_seeds",
                "chance": 100,
                "count": 1.5
            },
        ),
    }
}