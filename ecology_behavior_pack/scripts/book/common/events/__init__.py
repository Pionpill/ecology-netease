from scripts.common import modConfig
"""
系统首次加载时间，依赖于客户端本地存储
通信方向：
    客户端 -> 服务端
参数:
    playerId: 玩家id
"""
BookFirstInitEvent = modConfig.ADDON_NAME + 'BookFirstInitEvent'