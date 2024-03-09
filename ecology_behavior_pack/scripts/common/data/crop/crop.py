# 作物种植与生长表，键名不可以有下划线_
CROP_DATA = {
    "ham:herb": {
        "plant": {
            "land": ["minecraft:farmland"],
            "tags": ["plain"],
            "special_plant": None,
        },
        "grow": {
            "ticks": [8,9,9],
            "harvest_count": 1,
            "temperature_suit": (-5,30),
            "temperature_can": (-15,40),
            "rainfall_suit": (0.3,1),
            "rainfall_can": (0.15,1),
            "brightness_suit": (9, 15),
            "brightness_can": (5,15),
            "rain_multiply": 1.5,
            "multi_grow_count": 1,
            "multi_grow_stage": 0,
            "middle_harvest_stages": [],
        }
    }
}