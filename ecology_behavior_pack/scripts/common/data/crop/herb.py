HERB = {
    "beta": True,
    "seed": 'ham:herb_seeds',
    "blockPrefix": 'ham:herb',
    "grow": {
        "stage": (
            {
                "tick": 6,
                "height": (5, 32)
            },
            {
                "tick": 6,
                "height": (14, 32)
            },
            {
                "tick": 6,
                "height": (26, 32)
            },
            {
                "height": (30, 32)
            }
        ),
        "harvest": {
            "count": 1,
            "stage": 3
        },
        "temperature": {
            "suit": (-5, 30),
            "can": (-15, 50)
        },
        "rainfall": {
            "suit": (30, 100),
            "can": (10, 100)
        },
        "brightness": {
            "suit": (9, 15),
            "can": (5, 15)
        },
        "fertility": {
            "min": 50,
            "sensitivity": 10,
            "type": ["dirt", "stone"]
        },
        "rain_multiply": 1.5,
        "period": "sun"
    },
    "loot": (
        {
            "name": "ham:herb",
            "chance": 100,
            "count": 4
        },
        {
            "name": "ham:herb_seeds",
            "chance": 100,
            "count": 1.5
        }
    )
}