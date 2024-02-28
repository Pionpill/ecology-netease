from scripts.common import modConfig, logger
from scripts.workbench.client.ui.base import BaseInventoryScreen

import mod.client.extraClientApi as clientApi

CLASSPATH = "scripts.workbench.client.ui."

UI_DEFS = {
    "ham:cooking_table": {
        "name": "cooking_table_screen",
        "clsPath": CLASSPATH + "CraftingScreen",
        "screenDef": "cooking_table_screen.main"
    },
    "ham:baking_furnace": {
        "name": "baking_furnace_screen",
        "clsPath": CLASSPATH + "FurnaceScreen",
        "screenDef": "baking_furnace_screen.main"
    },
    "ham:mill": {
        "name": "mill_screen",
        "clsPath": CLASSPATH + "FurnaceScreen",
        "screenDef": "mill_screen.main"
    },
    "ham:butcher_table": {
        "name": "butcher_table_screen",
        "clsPath": CLASSPATH + "CraftingScreen",
        "screenDef": "butcher_table_screen.main"
    },
    "ham:food_steamer": {
        "name": "food_steamer_screen",
        "clsPath": CLASSPATH + "FurnaceScreen",
        "screenDef": "food_steamer_screen.main"
    },
    "ham:fryer": {
        "name": "fryer_screen",
        "clsPath": CLASSPATH + "FurnaceScreen",
        "screenDef": "fryer_screen.main"
    },
    "ham:grill": {
        "name": "grill_screen",
        "clsPath": CLASSPATH + "FurnaceScreen",
        "screenDef": "grill_screen.main"
    },
    "ham:pan": {
        "name": "pan_screen",
        "clsPath": CLASSPATH + "FurnaceScreen",
        "screenDef": "pan_screen.main"
    },
    "ham:squeezer": {
        "name": "squeezer_screen",
        "clsPath": CLASSPATH + "FurnaceScreen",
        "screenDef": "squeezer_screen.main"
    },
    "ham:stew_pot": {
        "name": "stew_pot_screen",
        "clsPath": CLASSPATH + "FurnaceScreen",
        "screenDef": "stew_pot_screen.main"
    },
}

class UIManager(object):
    currentUsingBlock = None
    currentScreen = None

    @staticmethod
    def Init():
        for uiDict in UI_DEFS.values():
            clientApi.RegisterUI(modConfig.ADDON_NAME, uiDict['name'], uiDict['clsPath'], uiDict['screenDef'])

    @staticmethod
    def GetUINode(blockName):
        # type: (str) -> BaseInventoryScreen
        if UIManager.currentScreen is None:
            uiInfo = UI_DEFS.get(blockName)
            if uiInfo is None:
                logger.error('不存在 {} 对应的 UI 配置'.format(blockName))
                return
            UIManager.currentUsingBlock = blockName
            UIManager.currentScreen = clientApi.PushScreen(modConfig.ADDON_NAME, uiInfo['name'], {'isHub': 1})
        return UIManager.currentScreen
    
    @staticmethod
    def ResetUINode():
        UIManager.currentUsingBlock = None
        UIManager.currentScreen = None
        clientApi.PopScreen()

    @staticmethod
    def GetCurrentUsingBlock():
        # type: () -> str | None
        """获取玩家正在使用的方块"""
        return UIManager.currentUsingBlock