from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from .host import Host
from core.config import settings


async def init_db():
    client = AsyncIOMotorClient(str(settings.mongo.url))
    db = client[settings.mongo.db_name]
    await init_beanie(database=db, document_models=[Host])
