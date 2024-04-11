class AddonDevelopError(SyntaxError):
    def __init__(self, message="模组逻辑异常"):
        realMessage = message + '，请报告给开发者群：712936357'
        SyntaxError.__init__(self, realMessage)
        self.message = realMessage

    def __str__(self):
        return self.message