class BiomeInfo(object):
    """生物群系信息，只与当前位置相关"""
    def __init__(self, name, name_cn, temperature, rainfall, tags):
        # type: (str, str, float, float, list) -> None
        self.name = name
        self.name_cn = name_cn
        self.temperature = temperature * 20
        self.rainfall = rainfall
        self.tags = tags

    def __str__(self):
        return "=================\n群戏信息: {0} ({1})\n温度: {2}\n湿度: {3}\n=================".format(self.name, self.name_cn, self.temperature, self.rainfall)