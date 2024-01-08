import logging

def makeLogger():
    """日志生成器，格式:|ecology| [等级-时间]: 消息"""
    logging.basicConfig(
        level=0,
        format='|ecology| [%(levelname)s-%(asctime)s]: %(message)s')
    return logging.getLogger(__name__)

logger = makeLogger()