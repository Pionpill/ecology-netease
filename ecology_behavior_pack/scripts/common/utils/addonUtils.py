from scripts.common.modConfig import ADDON_VERSION


def IsBeta():
    return 'alpha' in ADDON_VERSION or 'beta' in ADDON_VERSION