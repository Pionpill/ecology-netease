def GetBelowPosition(position, offset = 1):
    # type: (tuple[int, int, int], int) -> tuple[int, int, int]
    """获取某个位置下方的位置"""
    return (position[0], position[1] - offset, position[2])

def GetAbovePosition(position, offset = 1):
    # type: (tuple[int, int, int], int) -> tuple[int, int, int]
    """获取某个位置上方的位置"""
    return (position[0], position[1] + offset, position[2])

def IsOnSamePlain(position1, position2):
    # type: (tuple[int, int, int], tuple[int, int, int]) -> bool
    """两个坐标是否在同一平面（仅y轴不同）"""
    return position1[0] == position2[0] and position1[2] == position2[2]

def GetNearbyPosition(position, distance, mode = 'cube', type = "point"):
    # type: (tuple[int, int, int], int, str, str) -> tuple[tuple[int, int, int], ...]
    """获取一定距离的位置，返回一个包含所有满足距离条件的元素 TODO 需要补全功能

    Args:
        position (tuple[int, int, int]): 当前位置
        distance (int): 距离
        mode (str, optional): 测距模式，目前仅支持 cube 模式.
        type (str, optional): 获取的距离模式，目前支持 point(点), vertex(顶点) 两种模式.
    """
    x = position[0]
    y = position[1]
    z = position[2]
    if type == 'point':
        return (
            (x - distance, y, z),
            (x + distance, y, z),
            (x, y - distance, z),
            (x, y + distance, z),
            (x, y, z - distance),
            (x, y, z + distance),
        )
    if mode == 'cube':
        if type == 'vertex':
            return (
                (x - distance, y - distance, z - distance),
                (x - distance, y - distance, z + distance),
                (x - distance, y + distance, z - distance),
                (x - distance, y + distance, z + distance),
                (x + distance, y - distance, z - distance),
                (x + distance, y - distance, z + distance),
                (x + distance, y + distance, z - distance),
                (x + distance, y + distance, z + distance),
            )