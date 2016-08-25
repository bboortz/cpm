import logging
import logging.config

logging.config.fileConfig('logging.conf')

def getLogger(logname):
    """create logger
    """
    logger = logging.getLogger(logname)
    return logger

