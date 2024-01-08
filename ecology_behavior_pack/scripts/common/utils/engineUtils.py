from time import time

defaultCollDownDict = {}

def coolDown(playerId, coolTime=0.2, coolDict = defaultCollDownDict):
    # type: (int, float, dict) -> bool
    """交互冷却"""
    if not coolDict.get(playerId):
        coolDict[playerId] = time()
        return True
    elif time() - coolDict[playerId] < coolTime:
        return False
    else:
        coolDict[playerId] = time()
        return True
