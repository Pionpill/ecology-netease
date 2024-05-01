from time import time
from scripts.common import logger

# 键：playerId / entityId 值：时间
defaultCollDownDict = {}    # type: dict[str, float]

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
