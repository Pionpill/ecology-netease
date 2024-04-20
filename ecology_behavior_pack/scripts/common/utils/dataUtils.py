from scripts.common.error import AddonDataFieldError
from scripts.common import logger

def GetField(key, data, dataKey = None, defaultValue = None):
    """
    获取字段值，支持递归获取
    
    :param key: 递归获取的数据键
    :param data: 数据
    :param dataKey: 数据名称（谁的数据）
    :param defaultValue: 默认值，如果传函数懒执行
    :raises AddonDataFieldError: 获取数据字段错误
    """
    keyTuple = (key, ) if isinstance(key, str) else key
    field = data.get(keyTuple[0])
    if field is None:
        if defaultValue is not None:
            return defaultValue() if callable(defaultValue) else defaultValue
        raise AddonDataFieldError('{} 没有对应字段 {}'.format(dataKey, keyTuple[0]))
    return field if len(keyTuple) == 1 else GetField(keyTuple[1:], field, dataKey, defaultValue)