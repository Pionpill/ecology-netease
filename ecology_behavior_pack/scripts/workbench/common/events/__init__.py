from scripts.common import modConfig
"""
玩家使用工作台事件
通信方向:
    服务端 -> 客户端
参数:
    position: 操作方块的位置
    dimensionId: 操作方块的维度
    playerId: 玩家id
    blockName: 方块名
    slotData: 方块实体存储的数据
    burnData: 熔炉燃烧数据，仅在 blockType 为 WorkbenchType.furnace 时存在
    blockType: 方块类型 WorkbenchType
"""
WorkbenchBlockUseEvent = modConfig.ADDON_NAME + 'WorkbenchBlockUseEvent'

"""
玩家关闭自定义方块 UI 事件
通信方向:
    客户端 -> 服务端 | 服务端 -> 客户端
参数:
    position: 操作方块的位置
    dimensionId: 操作方块的维度
    playerId: 玩家id
    blockType: 方块类型 WorkbenchType
    blockName: 方块名
"""
WorkbenchBlockUICloseEvent = modConfig.ADDON_NAME + 'WorkbenchBlockUICloseEvent'

"""
玩家工作台UI需要更新事件
通信方向:
    服务端 -> 客户端
参数:
    position: 操作方块的位置
    dimensionId: 操作方块的维度
    blockName: 方块名
    slotData: 方块实体存储的数据
    burnData: 熔炉燃烧数据，仅在 blockType 为 WorkbenchType.furnace 时存在
    blockType: 方块类型 WorkbenchType
"""
WorkbenchUIRefreshEvent = modConfig.ADDON_NAME + 'WorkbenchUIRefreshEvent'

"""
玩家在自定义UI界面中切换背包物品事件
通信方向:
    客户端 -> 服务端
参数:
    fromSlotName: 第一个交换物品的槽名
    toSlotName: 第二个交换物品的槽名
    fromItemDict: 第一个交互的物品 
    toItemDict: 第二个交互的物品 
    takePercent: 交换比例
    position: 操作方块的位置
    dimensionId: 操作方块的维度
    playerId: 玩家id
"""
WorkbenchSlotItemSwapEvent = modConfig.ADDON_NAME + 'WorkbenchSlotItemSwapEvent'

"""
玩家在自定义UI界面中点击结果槽取物品事件
通信方向:
    客户端 -> 服务端
参数:
    itemDict: 结果槽物品
    slotName: 槽名
    position: 操作方块的位置
    dimensionId: 操作方块的维度
    playerId: 玩家id
    blockName: 方块名
"""
WorkbenchOutSlotClickEvent = modConfig.ADDON_NAME + 'WorkbenchOutSlotClickEvent'