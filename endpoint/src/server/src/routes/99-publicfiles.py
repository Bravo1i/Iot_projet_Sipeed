import logging

from app import app

logger = logging.getLogger('http')

from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="src/public", html=True), name="public")