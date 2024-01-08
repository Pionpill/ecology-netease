# -*- coding: utf-8 -*-

from mod.common.mod import Mod
import mod.server.extraServerApi as serverApi
from scripts.common import modConfig
from scripts.common import logger


@Mod.Binding(name=modConfig.ADDON_NAME, version="0.1.0")
class Ecology(object):

    def __init__(self):
        logger.info("Ecology Mod Scripts Init")

    @Mod.InitServer()
    def ServerInit(self):
        logger.info("Ecology Server Init")
        serverApi.RegisterSystem(modConfig.ADDON_NAME,
                                 modConfig.ECOLOGY_SERVER_NAME,
                                 modConfig.ECOLOGY_SERVER_PATH)
        serverApi.RegisterSystem(modConfig.ADDON_NAME,
                                 modConfig.CROP_SERVER_NAME,
                                 modConfig.CROP_SERVER_PATH)

    @Mod.DestroyServer()
    def ServerDestroy(self):
        logger.info("Ecology Server Destroy")

    @Mod.InitClient()
    def ClientInit(self):
        logger.info("Ecology Client Init")

    @Mod.DestroyClient()
    def ClientDestroy(self):
        logger.info("Ecology Client Destroy")
