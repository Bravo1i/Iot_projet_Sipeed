from os.path import dirname, join

import logging
from typing import List

from app import app

from fastapi import WebSocket, WebSocketDisconnect

logger = logging.getLogger('http')

logger.debug('ws tag event route')
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


wsManager = ConnectionManager()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await wsManager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await wsManager.send_personal_message(f"You wrote: {data}", websocket)
            await wsManager.broadcast(f"Client # says: {data}")
            logger.debug('msg recu %s', data)
    except WebSocketDisconnect:
        wsManager.disconnect(websocket)
        logger.debug('disconnect from %s', websocket)
        await wsManager.broadcast(f"Client # left the chat")
