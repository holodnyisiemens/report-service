from fastapi import APIRouter, Depends

from .crud import get_all_responsible_query
from utils import get_auth_user

router = APIRouter()


@router.get("/")
async def read_all_responsible(auth_username: str = Depends(get_auth_user)) -> list:
    return await get_all_responsible_query()
