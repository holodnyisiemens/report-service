import secrets
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from core.config import settings

security = HTTPBasic()


def get_auth_user(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
) -> str:
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect user or password"
    )

    if not secrets.compare_digest(
        credentials.username.encode("utf-8"),
        settings.auth.user.encode("utf-8"),
    ):
        raise unauthed_exc

    if not secrets.compare_digest(
        credentials.password.encode("utf-8"),
        settings.auth.password.encode("utf-8"),
    ):
        raise unauthed_exc

    return credentials.username
