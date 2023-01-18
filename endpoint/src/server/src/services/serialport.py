import logging
import asyncio
import importlib 

import serial_asyncio
import serial.tools.list_ports
import json
wstagevent = importlib.import_module("routes.60-wstagevent")

logger = logging.getLogger('uwbloc')

deviceStreamReader = None
deviceStreamWriter = None
streamReaderTask = None

async def get_serial_infos():
    """
    Listing ports
    """
    logger.debug('get_serial_infos')
    listPort = serial.tools.list_ports.comports()
    result = [ { "name": obj.name, 'device': obj.device, "description": obj.description, "manufacturer": obj.manufacturer, "product": obj.product }
        for obj in listPort]
    logger.debug("List port: %s", result)
    return result



async def readserial(reader):
    while True:
        msg = await reader.readuntil(b'\n')
        logger.debug(f'received: {msg.rstrip().decode()}')
        await wstagevent.wsManager.broadcast(msg.rstrip().decode())
        data=msg.rstrip().decode()
        cnt_vehicule={ "nb_voitures" : str(data)}
        logger.debug(f'send: {json.dumps(cnt_vehicule)}')
        await wstagevent.wsManager.broadcast(json.dumps(cnt_vehicule))

async def connect_serial(port, baudrate):
    """
    Listing ports
    """
    global deviceStreamReader, deviceStreamWriter, streamReaderTask
    logger.debug('service connect_serial(%s, %d)', port, baudrate)
    try:
        if streamReaderTask:
            logger.debug('cancel streamReaderTask')
            streamReaderTask.cancel()
            streamReaderTask = None
        if deviceStreamReader:
            logger.debug('close serial reader')
            del deviceStreamReader
            deviceStreamReader = None
        if deviceStreamWriter:
            logger.debug('close serial writer')
            deviceStreamWriter.transport.close()
            del deviceStreamWriter
            deviceStreamWriter = None
        deviceStreamReader, deviceStreamWriter = await serial_asyncio.open_serial_connection(url=port, baudrate=baudrate)
        streamReaderTask = asyncio.create_task(readserial(deviceStreamReader))
    except Exception as e:
        logger.error('Exception: %s', e)
        raise e
    return {}

