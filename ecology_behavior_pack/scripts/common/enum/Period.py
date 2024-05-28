class Period(object):
    DAY = 'day'
    NIGHT = 'night'
    SUN = 'sun'
    MOON = 'moon'
    NONE = 'none'

    CNNameDict = {
        DAY: '白天',
        NIGHT: '晚上',
        SUN: '太阳',
        MOON: '月亮',
        NONE: '全天',
    }

    @staticmethod
    def GetChinese(name):
        return Period.CNNameDict.get(name, Period.SUN)