import json
from os.path import dirname, join

import logging
from services import serialport as serialservice

from app import app

logger = logging.getLogger('http')

logger.debug('serial route')


@app.get("/serial",
    response_description="serial status",
    tags=["serial"],
)
async def get_serial_infos():
    """
    List all serial port
    """
    return await serialservice.get_serial_infos()


@app.get("/serial/connect",
    tags=["serial"],
)
async def connect_serial(port: str, baudrate: int = 115200):
    """
    Connected to port parameter
    """
    return await serialservice.connect_serial(port, baudrate)