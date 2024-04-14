class AddonEntityDataError(SyntaxError):
    def __init__(self, message="获取实体数据异常"):
        realMessage = message + '，请报告给开发者群：712936357'
        SyntaxError.__init__(self, realMessage)
        self.message = realMessage

    def __str__(self):
        return self.message