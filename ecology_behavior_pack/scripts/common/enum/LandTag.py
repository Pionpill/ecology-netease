class LandTag(object):
    DIRT = 'dirt'
    FUNGI = 'fungi'
    STONE = 'stone'
    CLAY = 'clay'
    SAND = 'sand'

    cnNameDict = {
        DIRT: '泥土',
        FUNGI: '菌类',
        STONE: '石头',
        CLAY: '粘土',
        SAND: '沙子',
    }

    @staticmethod
    def GetChinese(name):
        # str | list[str] -> str
        if isinstance(name, str):
            return LandTag.cnNameDict.get(name, LandTag.DIRT)
        else:
            nameList = [LandTag.cnNameDict.get(x) for x in name]
            nameStr = ''
            for name in nameList:
                nameStr += str(name) + ' '
            return nameStr