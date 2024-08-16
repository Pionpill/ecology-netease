ADDON_NAME = 'HammerEcology'
ADDON_NAME_CN = '锤子生态'

ADDON_VERSION = 'v1.0.5'
__DEV__ = True

# 生态系统
ECOLOGY_SERVER_NAME = "EcologyServerSystem{}".format(ADDON_VERSION)
ECOLOGY_SERVER_PATH = "scripts.ecology.server.system.EcologyServerSystem"

# 作物系统
CROP_SERVER_NAME = "CropServerSystem{}".format(ADDON_VERSION)
CROP_SERVER_PATH = "scripts.crop.server.system.CropServerSystem"

# 工作台系统
WORKBENCH_SERVER_NAME = "WorkbenchServerSystem{}".format(ADDON_VERSION)
WORKBENCH_SERVER_PATH = "scripts.workbench.server.system.WorkbenchServerSystem"
WORKBENCH_CLIENT_NAME = "WorkbenchClientSystem{}".format(ADDON_VERSION)
WORKBENCH_CLIENT_PATH = "scripts.workbench.client.system.WorkbenchClientSystem"

# 书籍系统
BOOK_SERVER_NAME = "BookServerSystem{}".format(ADDON_VERSION)
BOOK_SERVER_PATH = "scripts.book.server.system.BookServerSystem"
BOOK_CLIENT_NAME = "BookClientSystem{}".format(ADDON_VERSION)
BOOK_CLIENT_PATH = "scripts.book.client.system.BookClientSystem"