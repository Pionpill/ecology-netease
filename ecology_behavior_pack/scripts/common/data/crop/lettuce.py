LETTUCE = {
    "beta": True,
    "seed": 'ham:lettuce_seeds',
    "blockPrefix": 'ham:lettuce',
    "grow": {
        "stage": (
            {
                "tick": 11,
                "height": (12, 32)
            },
            {
                "tick": 11,
                "height": (13, 32)
            },
            {
                "height": (14, 32)
            }
        ),
        "harvest": {
            "count": 1,
            "stage": (1, 2),
        },
        "temperature": {
            "suit": (10, 25),
            "can": (0, 30)
        },
        "rainfall": {
            "suit": (60, 100),
            "can": (30, 100)
        },
        "brightness": {
            "suit": (6, 12),
            "can": (4, 20)
        },
        "fertility": {
            "min": 80,
            "sensitivity": 50,
            "type": ["dirt"]
        },
        "rain_multiply": 1.5,
        "period": "none"
    },
    "loot": {
        1: {
            "name": "ham:lettuce",
            "chance": 100,
            "count": 2
        },
        2: (
            {
                "name": "ham:lettuce",
                "chance": 100,
                "count": 4
            }, 
            {
                "name": "ham:lettuce_seeds",
                "chance": 100,
                "count": 1.5
            }
        ),
    }
}