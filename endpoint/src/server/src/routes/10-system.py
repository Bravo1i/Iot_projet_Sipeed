from os.path import dirname, join

import logging

from app import app

logger = logging.getLogger('http')

logger.debug('System route')

@app.get("/system",
    response_description="system status",
    tags=["system"],
)
async def get_system_info():
    """
    Get system details:

    - **software version...**
    """
    logger.debug('get_system_info')
    return {"Hello": "World"}

