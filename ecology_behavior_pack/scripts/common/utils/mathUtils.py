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