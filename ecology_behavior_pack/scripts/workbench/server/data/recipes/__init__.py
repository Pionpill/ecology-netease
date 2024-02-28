from scripts.workbench.common.enum import WorkbenchType
from scripts.workbench.server.data.recipes.bake import BAKE_DATA
from scripts.workbench.server.data.recipes.cook import COOK_DATA
from scripts.workbench.server.data.recipes.fryer import FRYER_DATA
from scripts.workbench.server.data.recipes.grill import GRILL_DATA
from scripts.workbench.server.data.recipes.mill import MILL_DATA
from scripts.workbench.server.data.recipes.pan import PAN_DATA
from scripts.workbench.server.data.recipes.squeezer import SQUEEZER_DATA
from scripts.workbench.server.data.recipes.steamer import STEAMER_DATA
from scripts.workbench.server.data.recipes.stew import STEW_DATA

WORKBENCH_MAP = {
    "ham:cooking_table": {
        "recipe": COOK_DATA,
        "material": 13,
        "fixed_material": 4,
        "fuel": 0,
        "result": 1,
        "type": WorkbenchType.Crafting,
    },
    "ham:baking_furnace": {
        "recipe": BAKE_DATA,
        "material": 1,
        "fuel": 1,
        "result": 1,
        "type": WorkbenchType.Furnace,
    },
    "ham:mill": {
        "recipe": MILL_DATA,
        "material": 1,
        "fuel": 1,
        "result": 2,
        "type": WorkbenchType.Furnace,
    },
    "ham:food_steamer": {
        "recipe": STEAMER_DATA,
        "material": 1,
        "fuel": 1,
        "result": 1,
        "type": WorkbenchType.Furnace,
    },
    "ham:fryer": {
        "recipe": FRYER_DATA,
        "material": 1,
        "fuel": 1,
        "result": 1,
        "type": WorkbenchType.Furnace,
    },
    "ham:grill": {
        "recipe": GRILL_DATA,
        "material": 1,
        "fuel": 1,
        "result": 1,
        "type": WorkbenchType.Furnace,
    },
    "ham:pan": {
        "recipe": PAN_DATA,
        "material": 11,
        "fixed_material": 5,
        "fuel": 1,
        "result": 1,
        "type": WorkbenchType.Furnace,
    },
    "ham:squeezer": {
        "recipe": SQUEEZER_DATA,
        "material": 3,
        "fuel": 1,
        "result": 1,
        "type": WorkbenchType.Furnace,
    },
    "ham:stew_pot": {
        "recipe": STEW_DATA,
        "material": 7,
        "fixed_material": 1,
        "fuel": 1,
        "result": 1,
        "type": WorkbenchType.Furnace,
    },
}

__all__ = [BAKE_DATA, COOK_DATA, FRYER_DATA, GRILL_DATA, MILL_DATA, PAN_DATA, SQUEEZER_DATA, STEAMER_DATA, STEW_DATA]
