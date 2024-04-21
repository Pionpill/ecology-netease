from scripts.common.data.crop.corn import CORN
from scripts.common.data.crop.eggplant import EGGPLANT
from scripts.common.data.crop.herb import HERB
from scripts.common.data.crop.lettuce import LETTUCE
from scripts.common.data.crop.onion import ONION
from scripts.common.data.crop.rice import RICE
from scripts.common.data.crop.scallion import SCALLION

CROP_DATA = {
    "ham:herb": HERB,
    "ham:corn": CORN,
    "ham:eggplant": EGGPLANT,
    "ham:lettuce": LETTUCE,
    "ham:onion": ONION,
    "ham:rice": RICE,
    "ham:scallion": SCALLION,
}

__all__ = [CROP_DATA]