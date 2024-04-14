from time import time

defaultCollDownDict = {}

def coolDown(playerId = None, coolTime=0.2, coolDict = defaultCollDownDict):
    # type: (int | tuple | None, float, dict) -> bool
    """交互冷却"""
    key = playerId or 'default'
    if not coolDict.get(key):
        coolDict[key] = time()
        return True
    elif time() - coolDict[key] < coolTime:
        return False
    else:
        coolDict[key] = time()
        return True
