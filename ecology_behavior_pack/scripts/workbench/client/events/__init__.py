from scripts.common import modConfig

"""
玩家关闭自定义方块 UI 事件
通信方向:
    客户端 -> 客户端
参数:
    blockName: 方块名
"""
WorkbenchBlockUICloseClientEvent = modConfig.ADDON_NAME + 'WorkbenchBlockUICloseClientEvent'