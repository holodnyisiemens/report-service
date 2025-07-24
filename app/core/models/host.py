from beanie import Document
from core.config import settings


class Host(Document):
    responsible: str

    class Config:
        extra = "allow"

    class Settings:
        name = "hosts"


class HostEmailReport(Host):
    class Settings:
        projection = settings.email.report_mongo_projection
