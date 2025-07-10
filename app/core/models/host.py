from beanie import Document


class Host(Document):
    responsible: str

    class Config:
        extra = "allow"

    class Settings:
        name = "hosts"


class HostEmailReport(Host):
    class Settings:
        projection = {
            "_id": 0,
            "updatable": 0,
            "restartable": 0,
            "zabbixId": 0,
            "emails": 0,
        }
