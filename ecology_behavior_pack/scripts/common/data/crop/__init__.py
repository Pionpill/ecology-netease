from scripts.common.data.crop.corn import CORN
from scripts.common.data.crop.eggplant import EGGPLANT
from scripts.common.data.crop.herb import HERB
from scripts.common.data.crop.lettuce import LETTUCE

CROP_DATA = {
    "ham:herb": HERB,
    "ham:corn": CORN,
    "ham:eggplant": EGGPLANT,
    "ham:lettuce": LETTUCE,
}

__all__ = [CROP_DATA]