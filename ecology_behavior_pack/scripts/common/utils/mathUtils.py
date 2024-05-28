import math
import random
from scripts.common import logger

def hasCommonElements(list1, list2):
    # type: (tuple | list, tuple | list) -> bool
    """判断两个列表是否有相同的元素"""
    set1 = set(list1)
    set2 = set(list2)
    return bool(set1 & set2)

def between(value, range):
    # type: (float, tuple[float, float]) -> bool
    """判断某个值是否在某个范围内"""
    return range[0] <= value <= range[1]

def calculateAbleTickRatio(value, suitRange, canRange):
    # type: (int | float, tuple[float, float], tuple[float, float]) -> float
    """获取温度，降水，光照的适宜度"""
    if between(value, suitRange):
        return 1.0
    if value <= canRange[0] or value >= canRange[1]:
        return 0
    elif value < suitRange[0]:
        return (float(value) - canRange[0]) / (suitRange[0] - canRange[0])
    else:
        return (canRange[1] - float(value)) / (canRange[1] - suitRange[1])
    
def GetRandomInteger(value):
    # type: (float) -> int
    """将一个浮点数按概率转换为邻近的整数"""
    floor = math.floor(value)
    ceil = math.ceil(value)
    return ceil if random.random() < (value - floor) else floor

def addTuple(tuple1, tuple2, addExcess = True):
    # type: (tuple[int, ...], tuple[int, ...], bool) -> tuple[int, ]
    """将两个元组元素相加"""
    longTuple = tuple1 if len(tuple1) >= len(tuple2) else tuple2
    shortTuple = tuple1 if len(tuple1) < len(tuple2) else tuple2
    resultList = []
    for x in range(len(shortTuple)):
        resultList.append(shortTuple[x] + longTuple[x])
    if addExcess:
        for x in range(len(shortTuple), len(longTuple)):
            resultList.append(longTuple[x])
    return tuple(resultList)