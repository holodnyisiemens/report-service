from fastapi import APIRouter

from api.v1 import router as v1_router
from core.config import settings

router = APIRouter()

router.include_router(
    v1_router,
    prefix=settings.api.v1.prefix,
)
