from scripts.crop.server.data import CROP_DATA

def IsCrop(blockOrItemName):
    # type: (str) -> bool
    seedKey = GetSeedKey(blockOrItemName)
    return CROP_DATA.get(seedKey) is not None

def GetSeedKey(blockOrItemName):
    # type: (str) -> str
    """获取作物块/种子对应的seed键名"""
    key = blockOrItemName.split('_')[0]
    return key if 'ham:' in key else 'ham:' + key

def GetBlockStageName(blockOrItemName, stageId):
    # type: (str, int) -> str
    """获取种植后作物方块名"""
    return blockOrItemName.split('_')[0] + '_stage_' + str(stageId)

def GetBlockStageDict(blockOrItemName, stageId):
    # type: (str, int) -> str
    """获取种植后作物方块字典"""
    return {"name": blockOrItemName.split('_')[0] + '_stage_' + str(stageId), "aux": 0}
