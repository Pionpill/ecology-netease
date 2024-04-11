class Biome(object):
    def __init__(self, name, name_cn, temperature, rainfall, tags):
        # type: (str, str, float, float, list) -> None
        self.name = name
        self.name_cn = name_cn
        self.temperature = temperature * 20
        self.rainfall = rainfall
        self.tags = tags

    @staticmethod
    def FromData(biomeData, biomeName = None):
        # type: (dict, str) -> Biome
        """
        从数据对象，实例数据中初始化 Biome 对象，
        TODO 生态数据是固定的，可以存储在容器中
        如果 biomeData 中没有 name 属性，则必须指派 biomeName
        """
        name = biomeData.get("name") if biomeName is None else biomeName
        return Biome(name, biomeData.get("name_cn"), biomeData.get("temperature"), biomeData.get("rainfall"), biomeData.get("tags"))
    
    def toJson(self):
        return {
            "name": self.name,
            "name_cn": self.name_cn,
            "temperature": self.temperature,
            "rainfall": self.rainfall,
            "tags": self.tags,
        }