RICE = {
    "beta": True,
    "seed": 'ham:rice_seeds',
    "blockPrefix": 'ham:rice',
    "grow": {
        "stage": (
            {
                "tick": 13,
                "height": (12, 32)
            },
            {
                "tick": 13,
                "height": (30, 32)
            },
            {
                "tick": 14,
                "height": (38, 32)
            },
            {
                "height": (42, 32)
            }
        ),
        "harvest": {
            "count": 1,
            "stage": 3
        },
        "temperature": {
            "suit": (20, 35),
            "can": (10, 40)
        },
        "rainfall": {
            "suit": (40, 100),
            "can": (20, 100)
        },
        "brightness": {
            "suit": (9, 15),
            "can": (5, 15)
        },
        "fertility": {
            "min": 120,
            "sensitivity": 130,
            "type": ["dirt"]
        },
        "rain_multiply": 2,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:rice_plant",
            "chance": 100,
            "count": 1
        },
        {
            "name": "ham:rice_seeds",
            "chance": 100,
            "count": 1.5
        },
    )
}