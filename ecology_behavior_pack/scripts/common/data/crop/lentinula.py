LENTINULA = {
    "beta": True,
    "seed": 'ham:lentinula',
    "blockPrefix": 'ham:lentinula',
    "grow": {
        "stage": (
            {
                "tick": 11,
                "height": (8, 32)
            },
            {
                "tick": 11,
                "height": (12, 32)
            },
            {
                "tick": 11,
                "height": (14, 32)
            },
            {
                "height": (14, 32)
            }
        ),
        "harvest": {
            "count": -1,
            "stage": 3,
            "return": 0,
        },
        "temperature": {
            "suit": (20, 25),
            "can": (10, 30)
        },
        "rainfall": {
            "suit": (80, 100),
            "can": (40, 100)
        },
        "brightness": {
            "suit": (4, 12),
            "can": (0, 12)
        },
        "fertility": {
            "min": 100,
            "sensitivity": 60,
            "type": ["fungi"]
        },
        "rain_multiply": 1,
        "period": "none",
        "replace_block": "ham:rotten_wood"
    },
    "loot": (
        {
            "name": "ham:lentinula",
            "chance": 100,
            "count": 3
        },
        # { FIXME 禁止右键使用时掉落
        #     "name": "ham:rotten_wood",
        #     "chance": 75,
        #     "count": 1
        # },
    )
}