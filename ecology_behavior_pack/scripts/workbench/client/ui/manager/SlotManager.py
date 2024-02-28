from scripts.common import logger

class SlotManager(object):
    def __init__(self):
        object.__init__(self)
        self.__slots = {}   # key: slotName (str|int)  value: { path, item }
        self.__paths = {}   # key: path (str) value: slotName

    def GetSlotPath(self, slotName):
        # type: (str|int) -> str
        """通过槽名获取 slot 的UI路径"""
        return self.__GetSlotInfo(slotName).get("path")
    
    def SetSlotPath(self, slotName, slotPath):
        # type: (str|int, str) -> None
        """设置 slot 的UI路径"""
        slotInfo = self.__slots.get(slotName)
        if slotInfo is None:
            self.__slots[slotName] = {}
        self.__slots[slotName]["path"] = slotPath
        self.__paths[slotPath] = slotName

    def GetSlotItem(self, slotName = None, slotPath = None):
        # type: (str|int, str) -> dict
        """通过槽名或槽路径获取 slot 对应的物品信息，，如果不存在会抛错"""
        if slotName is not None:
            return self.__GetSlotInfo(slotName).get("item")
        if slotPath is not None:
            slotName = self.GetSlotName(slotPath)
            return self.__GetSlotInfo(slotName).get("item")
        logger.error('请传入槽名或槽路径')
        return

    def SetSlotItem(self, slotName, slotItem):
        # type: (str|int, str) -> None
        """设置 slot 对应的物品信息"""
        slotInfo = self.__slots.get(slotName)
        if slotInfo is None:
            self.__slots[slotName] = {}
        self.__slots[slotName]["item"] = slotItem

    def GetSlotName(self, slotPath):
        # type: (str) -> str|int
        """根据 UI 路径获取 slotName，如果不存在会抛错"""
        slotName = self.__paths.get(slotPath)
        if slotName is None:
            logger.error(slotPath + "不存在对应的槽名或未初始化")
            return
        return slotName

    def __GetSlotInfo(self, slotName):
        # type: (str|int) -> dict
        """获取 slot 的信息，包括 slotPath, item 两个键，如果不存在会抛错"""
        slotInfo = self.__slots.get(slotName)
        if slotInfo is None:
            logger.error(str(slotName) + "不存在对应的物品信息或未初始化")
            return
        return slotInfo

    def SetSlotInfo(self, slotName, slotPath = None, itemDict = None):
        # type: (str|int, str, dict) -> None
        """设置 slot 的信息"""
        if slotPath is not None:
            self.SetSlotPath(slotName, slotPath)
        self.SetSlotItem(slotName, itemDict)

    def GetAllSlotPath(self):
        """获取所有的槽UI路径"""
        # type: () -> list[int|str]
        return self.__paths.keys()
