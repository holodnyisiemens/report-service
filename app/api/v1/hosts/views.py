from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from .crud import get_all_hosts_query, get_hosts_query
from ..responsible.crud import get_all_responsible_query
from core.config import settings
from core.models import HostEmailReport
from utils import (
    get_auth_user,
    query_to_docs,
    docs_to_html_table,
    get_email_address,
    send_email,
)

router = APIRouter()


@router.get("/")
async def read_all_hosts(auth_username: str = Depends(get_auth_user)):
    all_hosts_query = get_all_hosts_query()
    all_hosts = await query_to_docs(all_hosts_query)
    return all_hosts


@router.get("/{responsible}")
async def read_hosts_by_responsible(
    responsible: str,
    auth_username: str = Depends(get_auth_user),
    email_notify: bool = False,
):

    hosts_query = get_hosts_query(responsible)

    if not email_notify:
        hosts = await query_to_docs(hosts_query)
        return hosts

    elif responsible not in await get_all_responsible_query():
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{responsible} not in responsible list",
        )

    else:
        report_hosts_query = hosts_query.project(HostEmailReport)
        report_hosts = await query_to_docs(report_hosts_query)
        report_hosts_html_table = docs_to_html_table(report_hosts)

        reciever_email_address = get_email_address(responsible)

        send_email(
            reciever_email_address,
            report_hosts_html_table,
            email_subject=settings.email.hosts_report_subject,
        )

        return JSONResponse(
            content={"status": "ok"},
            status_code=status.HTTP_200_OK,
        )
