from email.message import EmailMessage
import smtplib
import ssl
from typing import Any

from fastapi import HTTPException, status
import pandas as pd
from pydantic import BaseModel, EmailStr

from core.config import settings


class EmailAddress(BaseModel):
    email: EmailStr


def docs_to_html_table(docs: list[dict[str, Any]]) -> str:
    docs_df = pd.DataFrame(docs)
    docs_html_table = docs_df.to_html(index=False, border=1)
    return docs_html_table


def get_email_address(responsible: str) -> str:
    if settings.debug:
        if not settings.debug_email:
            raise ValueError(
                "DEBUG is True but DEBUG_EMAIL is not set in .env file. Set DEBUG_EMAIL or disable DEBUG mode."
            )
        return settings.debug_email
    
    email_suffix = f"@{settings.email.receivers_domain}"

    if responsible.endswith(email_suffix):
        return responsible
    else:
        return responsible + email_suffix


def send_email(receiver_email: EmailAddress, content: str, email_subject: str) -> None:
    msg = EmailMessage()
    msg["Subject"] = email_subject
    msg["From"] = settings.smtp.user
    msg["To"] = receiver_email
    msg.set_content("HTML content is not displayed", subtype="plain")
    msg.add_alternative(content, subtype="html")

    server = None

    try:
        context = ssl.create_default_context()
        server = smtplib.SMTP(settings.smtp.host, settings.smtp.port)
        server.starttls(context=context)
        server.login(settings.smtp.user, settings.smtp.password)
        server.send_message(msg)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error while sending email",
        ) from e

    finally:
        if server:
            server.quit()
