from os.path import dirname, join

import logging

from app import app

logger = logging.getLogger('http')

logger.debug('tag route')

@app.get("/tags",
    response_description="system status",
    tags=["tags"],)
async def get_tagslist():
    """
    Get tag lists:

    - **var1**
    - **var2**
    """
    logger.debug('get_tagslist')
    return [{"item_id": 'ff'}]


@app.get("/tags/{item_id}",
    response_description="system status",
    tags=["tags"],)
async def get_tags(item_id: int):
    """
    Get tag lists:

    - **var1**
    - **var2**
    """
    logger.debug('get_tags')
    return {"item_id": item_id}