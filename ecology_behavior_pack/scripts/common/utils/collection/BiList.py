from scripts.common import logger

class BiList(object):
    """双向映射，列表实现，适用于少量数据"""
    def __init__(self, allowDuplicateValues = False):
        object.__init__(self)
        self.__allowDuplicateValues = allowDuplicateValues
        self.__keyList = []
        self.__valueList = []

    def __len__(self):
        return len(self.__keyList)

    def Set(self, key, value):
        if key in self.__keyList:
            logger.error('双向映射键不能重复 {}'.format(key))
            return False
        if value in self.__valueList and not self.__allowDuplicateValues:
            logger.error('双向映射值不能重复 {}'.format(value))
            return False
        self.__keyList.append(key)
        self.__valueList.append(value)

    def Get(self, key):
        """通过键获取"""
        return self.GetByKey(key)

    def GetByKey(self, key):
        """通过键获取"""
        if not key in self.__keyList:
            return None
        else:
            index = self.__keyList.index(key)
            return self.__valueList[index]
        
    def GetByValue(self, value):
        """通过键获取"""
        if not value in self.__valueList:
            return None
        else:
            index = self.__valueList.index(value)
            return self.__keyList[index]
    
    def Delete(self, key):
        """通过键删除，返回布尔值表示是否成功删除"""
        return self.DeleteByKey(key)

    def DeleteByKey(self, key):
        """通过键删除，返回布尔值表示是否成功删除"""
        if not key in self.__keyList:
            return False
        index = self.__keyList.index(key)
        self.__keyList.pop(index)
        self.__valueList.pop(index)
        return True
    
    def DeleteByValue(self, value):
        """通过键删除，返回布尔值表示是否成功删除"""
        if not value in self.__valueList:
            return False
        index = self.__valueList.index(value)
        self.__valueList.pop(index)
        self.__keyList.pop(index)
        return True