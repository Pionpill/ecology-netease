from scripts.common.params import BiomeInfo
from scripts.ecology.server.facade import EcologyFacade

def SetBiomeInfoToBlockEntityData(blockEntityData, biomeInfo):
    # type: (dict, BiomeInfo) -> None
    blockEntityData['biome_name'] = biomeInfo.name
    blockEntityData['biome_name_cn'] = biomeInfo.name_cn
    blockEntityData['biome_rainfall'] = biomeInfo.rainfall
    blockEntityData['biome_temperature'] = biomeInfo.temperature
    blockEntityData['biome_tags'] = biomeInfo.tags

def GetBiomeInfoFromBlockEntityData(blockEntityData):
    # type: (dict) -> BiomeInfo
    biomeData = {
        "name": blockEntityData['biome_name'],
        "name_cn": blockEntityData['biome_name_cn'],
        "rainfall": blockEntityData['biome_rainfall'],
        "temperature": blockEntityData['biome_temperature'] / 20,
        "tags": blockEntityData['biome_tags']
    }
    return EcologyFacade.GetBiomeInfoFromData(biomeData)