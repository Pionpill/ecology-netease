class PlantFailReason(object):
    LAND_UNABLE = 'landUnable' # 方块不可耕种 
    LAND_FERTILITY = 'fertility' # 土地肥力不够
    LAND_TYPE = 'landType' # 土地类型有误
    ECOLOGY_TEMPERATURE = 'ecologyTemperature' # 生态温度不适宜
    ECOLOGY_RAINFALL = 'ecology_rainfall' # 生态湿度不适宜