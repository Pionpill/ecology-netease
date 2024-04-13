import mod.server.extraServerApi as serverApi

levelId = serverApi.GetLevelId()
dimensionComp = serverApi.GetEngineCompFactory().CreateDimension(levelId)

class FrameService(object):
    FRAME_PER_MC_DAY = 24000
    BEGIN_HOUR = 6

    @staticmethod
    def GetDayFrame(dimensionId):
        # type: (int) -> int
        """获取MC当天的Frame"""
        return dimensionComp.GetLocalTime(dimensionId) % FrameService.FRAME_PER_MC_DAY

    @staticmethod
    def GetFormatDayTime(dimensionId):
        # type: (int) -> str
        """获取格式化的当前时间"""
        dayFrame = FrameService.GetDayFrame(dimensionId)
        deltaHour = dayFrame // 1000
        deltaMinute = dayFrame % 1000 // 60
        if deltaHour < 18:
            return "%s:%02d" % (str(6 + deltaHour).rjust(2), deltaMinute)
        return "%s:%02d" % (str(deltaHour - 18).rjust(2), deltaMinute)
    
    @staticmethod
    def HasSun(dimensionId):
        # type: (int) -> bool
        """判断是否存在太阳"""
        dayFrame = FrameService.GetDayFrame(dimensionId)
        return dayFrame <= 13000 or dayFrame >= 23000

    @staticmethod
    def HasMoon(dimensionId):
        # type: (int) -> bool
        """判断是否存在月亮"""
        dayFrame = FrameService.GetDayFrame(dimensionId)
        return dayFrame >= 11000