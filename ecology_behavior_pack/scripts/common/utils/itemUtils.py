from scripts.common.error import AddonDataError
from scripts.common import logger

def IsSameItem(item1, item2):
    # type: (dict | None, dict | None) -> bool
    """判断是否为同一item，只有itemName和auxValue均相同才返回True"""
    if item1 is None or item2 is None:
        return item1 is None and item2 is None
    if item1.get("newItemName") != item2.get("newItemName"):
        return False
    if item1.get("newAuxValue") != item2.get("newAuxValue"):
        return False
    # if item1.get("userData") != item2.get("userData"):
    #     return False
    # if item1.get("durability") != item2.get("durability"):
    #     return False
    return True

def GetItemDict(itemName=None, auxValue=0, count=1, itemDict=None):
    # type: (str | None, int, int, dict | None) -> dict
    if itemName is not None:
        return {
            'newItemName': itemName,
            'newAuxValue': auxValue,
            'count': count,
        }
    if itemDict is not None:
        # 如果第二个值也拿不到直接报错
        newItemName = itemDict.get('newItemName') or itemDict['itemName']
        newAuxValue = itemDict.get('newAuxValue') or itemDict.get('auxValue') or 0
        count = itemDict.get('count') or 1
        return {
            'newItemName': newItemName,
            'newAuxValue': newAuxValue,
            'count': count,
        }
    raise AddonDataError('获取物品字典时为传入有效信息')

def FilterDict(dict, filterTuple = ( None, )):
    # type: (dict, tuple) -> dict
    """过滤字典，将特定值删除"""
    return { k:v for k,v in dict.items() if v not in filterTuple}