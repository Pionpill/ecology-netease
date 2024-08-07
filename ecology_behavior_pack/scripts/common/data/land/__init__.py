LAND_DATA = {
    "minecraft:farmland": {
        "fertility": 120,
        "tag": ("dirt"),
        "aux": {
            "fertility": 130
        }
    },
    "minecraft:podzol": {
        "fertility": 100,
        "tag": ("dirt", "fungi"),
    },
    "minecraft:grass": {
        "fertility": 90,
        "tag": ("dirt"),
    },
    "minecraft:grass_path": {
        "fertility": 70,
        "tag": ("dirt"),
    },
    "minecraft:dirt": {
        "fertility": 80,
        "tag": ("dirt"),
    },
    "minecraft:sand": {
        "fertility": 40,
        "tag": ("sand"),
    },
    "minecraft:red_sand": {
        "fertility": 30,
        "tag": ("sand"),
    },
    "minecraft:mycelium": {
        "fertility": 130,
        "tag": ("fungi"),
    },
    "minecraft:moss_block": {
        "fertility": 90,
        "tag": ("dirt")
    },
    # "minecraft:rooted_dirt": {
    #     "fertility": 60,
    #     "tag": ("dirt")
    # },
    "minecraft:clay": {
        "fertility": 50,
        "tag": ("clay")
    },
    # "minecraft:coarse_dirt": {
    #     "fertility": 70,
    #     "tag": ("dirt")
    # }
}

__all__ = ['LAND_DATA']