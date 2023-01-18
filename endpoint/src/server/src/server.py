from os.path import dirname, basename, isfile, join
import glob
import importlib
import sys

import logging
from app import app

dirpath=join(dirname(__file__))

logger = logging.getLogger('http')

def startHttpServer():
    #   load all routes
    logger.debug('starting http server')
    routespath = join(dirpath, 'routes')
    routesfiles = glob.glob(join(dirpath, 'routes', "*.py"))
    routes = [ basename(f)[:-3] for f in routesfiles if isfile(f) and not f.endswith('__init__.py')]

    logger.debug("loading routes : %s", routes)
    for route in routes:
        logger.debug('\tloading %s from %s', route, routespath)
        spec = importlib.util.spec_from_file_location(route, join(routespath, route+'.py'))
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
    logger.debug('http server started')
