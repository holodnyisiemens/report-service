from fastapi import APIRouter

from api.v1.hosts import router as hosts_router
from api.v1.responsible import router as responsible_router
from core.config import settings

router = APIRouter()

router.include_router(
    hosts_router,
    prefix=settings.api.v1.hosts,
)

router.include_router(
    responsible_router,
    prefix=settings.api.v1.responsible,
)
