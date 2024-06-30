from scripts.common.data.crop.chili import CHILI
from scripts.common.data.crop.corn import CORN
from scripts.common.data.crop.eggplant import EGGPLANT
from scripts.common.data.crop.herb import HERB
from scripts.common.data.crop.lentinula import LENTINULA
from scripts.common.data.crop.lettuce import LETTUCE
from scripts.common.data.crop.onion import ONION
from scripts.common.data.crop.wheat import WHEAT
from scripts.common.data.crop.rice import RICE
from scripts.common.data.crop.scallion import SCALLION
from scripts.common.data.crop.soy_bean import SOYBEAN
from scripts.common.data.crop.tomato import TOMATO
from scripts.common.data.crop.potato import POTATO
from scripts.common.data.crop.bok_choy import BOK_CHOY
from scripts.common.data.crop.broccoli import BROCCOLI
from scripts.common.data.crop.weed import WEED
from scripts.common.data.crop.weed_tall import WEED_TALL

CROP_DATA = {
    "ham:herb": HERB,
    "ham:chili": CHILI,
    "ham:corn": CORN,
    "ham:eggplant": EGGPLANT,
    "ham:lentinula": LENTINULA,
    "ham:lettuce": LETTUCE,
    "ham:onion": ONION,
    "ham:rice": RICE,
    "ham:wheat": WHEAT,
    "ham:scallion": SCALLION,
    "ham:soy_bean": SOYBEAN,
    "ham:tomato": TOMATO,
    "ham:weed": WEED,
    "ham:weed_tall": WEED_TALL,
    "ham:potato": POTATO,
    "ham:bok_choy": BOK_CHOY,
    "ham:white_broccoli": BROCCOLI,
}

__all__ = ['CROP_DATA']