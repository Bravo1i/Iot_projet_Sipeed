from os.path import dirname, basename, isfile, join

import logging
import logging.config

from typing import Union
from app import app
from server import startHttpServer

dirpath=join(dirname(__file__))

logging.config.fileConfig(join(dirpath, 'logging.conf'))
logger = logging.getLogger('uwbloc')

logger.info('Start main...')

#   Starting http server
startHttpServer()

logger.info('End of main')
