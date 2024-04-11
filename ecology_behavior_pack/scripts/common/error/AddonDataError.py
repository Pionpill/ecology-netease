class AddonDataError(KeyError):
    def __init__(self, message="模组数据异常"):
        KeyError.__init__(self, message)
        self.message = message

    def __str__(self):
        return self.message