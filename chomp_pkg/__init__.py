from utils import ChompSettings as C
import os
import logging.config

LOG_PATH = C.LOG_PATH
LOG_FILE_PATH = C.LOCAL_LOG_PATH
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)
if not os.path.exists(LOG_FILE_PATH):
    f = open(LOG_FILE_PATH, "w")
LOG_CONFIG_PATH = C.LOGGING_FILE_CONFIG
logging.disable(logging.DEBUG)
logging.config.fileConfig(LOG_CONFIG_PATH)
choco_chomp_logger = logging.getLogger("choco_chomp")
choco_chomp_logger.debug('configured choco_chomp logger')
