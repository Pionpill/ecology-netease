from scripts.common import logger

def GetSlotPath(path):
    # type: (str) -> str
    """获取 slot 的UI路径"""
    if not 'slot' in path:
        logger.error('{} 中不存在 slot 路径'.format(path))
    oriPathList = path.split("/")
    if "slot" in oriPathList[-1]:
        return path
    newPathList = []
    for subPath in oriPathList:
        newPathList.append(subPath)
        if "slot" in subPath:
            break
    return ("/").join(newPathList)

def IsResultSlot(slotName):
    # type: (str) -> bool
    return isinstance(slotName, str) and 'result_slot' in slotName