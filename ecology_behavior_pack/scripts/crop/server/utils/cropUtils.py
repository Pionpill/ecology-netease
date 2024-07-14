from scripts.common.utils.collection import BiList
from scripts.common.error import AddonDataFieldError
from scripts.common.utils import dataUtils
from scripts.common import logger
from scripts.common.data.crop import CROP_DATA

seedList = [] # type: list[str]
seedPrefixList = [] # type: list[str]
seedPlaceBlockDict = BiList(True)

def __InitSeedList():
    def GetDefaultPrefix(seedName):
        # type: (str) -> str
        defaultValue = seedName
        for suffix in ['_seeds', '_seed']:
            defaultValue = defaultValue.replace(suffix, '')
        return defaultValue
    for cropInfo in CROP_DATA.values():
        seedName = cropInfo.get('seed')
        if seedName is None:
            # seedName 是主键，不可能不存在
            continue
        seedList.append(seedName)
        seedPrefixList.append(cropInfo.get('blockPrefix', GetDefaultPrefix(seedName)))
        try:
            placeBlock = dataUtils.GetField(('grow', 'replace_block'), cropInfo)
        except AddonDataFieldError:
            continue
        seedPlaceBlockDict.Set(seedName, placeBlock)

def IsSeed(itemName):
    # type: (str) -> bool
    if len(seedList) == 0:
        __InitSeedList()
    return itemName in seedList

def GetReplaceBlock(seedName):
    # type: (str) -> str | None
    if len(seedPlaceBlockDict) == 0:
        __InitSeedList()
    return seedPlaceBlockDict.Get(seedName)

def GetSeedByReplaceBlock(blockName):
    # type: (str) -> str | None
    if len(seedPlaceBlockDict) == 0:
        __InitSeedList()
    return seedPlaceBlockDict.GetByValue(blockName)

def IsCropBlock(blockName):
    # type: (str) -> bool
    if len(seedPrefixList) == 0:
        __InitSeedList()
    blockPrefix = __GetBlockPrefix(blockName)
    return blockPrefix in seedPrefixList

def GetSeedKey(blockOrItemName):
    # type: (str) -> str
    """获取作物块/种子对应的seed键名"""
    if 'seed' in blockOrItemName:
        for suffix in ['_seeds', '_seed']:
            blockOrItemName = blockOrItemName.replace(suffix, '')
        return blockOrItemName
    elif 'stage' in blockOrItemName:
        return __GetBlockPrefix(blockOrItemName)
    else:
        return blockOrItemName

def GetBlockStageDict(blockPrefix, stageId = 0):
    # type: (str, int) -> dict
    """获取种植后作物方块字典"""
    return {"name": blockPrefix + '_stage_' + str(stageId), "aux": 0}

def __GetBlockPrefix(blockName):
    # type: (str) -> str
    return '_'.join(blockName.split('_')[:-2]) if 'stage' in blockName else blockName