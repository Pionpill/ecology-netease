class EcologyInfo(object):
    """生态信息，受当前状态影响"""
    def __init__(self, name, name_cn, temperature_basic, temperature, rainfall, tags):
        object.__init__(self)
        self.name = name
        self.name_cn = name_cn
        self.temperature_basic = temperature_basic
        self.temperature = temperature
        self.rainfall = rainfall
        self.tags = tags

    def __str__(self):
        return "=================\n生态信息: {0} ({1})\n温度: {2}\n湿度: {3}\n=================".format(self.name, self.name_cn, self.temperature, self.rainfall)
        