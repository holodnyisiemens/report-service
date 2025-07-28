from pathlib import Path

from pydantic import BaseModel, MongoDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

APP_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = APP_DIR / (".env.local" if (APP_DIR / ".env.local").exists() else ".env")


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    hosts: str = "/hosts"
    responsible: str = "/responsible"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class AuthConfig(BaseModel):
    user: str
    password: str


class MongoDatabaseConfig(BaseModel):
    url: MongoDsn
    db_name: str
    hosts_collection: str


class SMTPConfig(BaseModel):
    user: str
    password: str
    host: str
    port: int


class EmailConfig(BaseModel):
    receivers_domain: str
    hosts_report_subject: str = "[Report] Check your hosts"
    report_mongo_projection: dict = {
        "_id": 0,
        "server": 0,
        "updatable": 0,
        "restartable": 0,
        "zabbixId": 0,
        "launchDate": 0,
        "description": 0,
        "nightstop": 0,
        "kubernetes": 0,
        "emails": 0,
    }


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        case_sensitive=False,
        env_nested_delimiter="__",
    )

    debug: bool
    debug_email: str
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    auth: AuthConfig
    mongo: MongoDatabaseConfig
    smtp: SMTPConfig
    email: EmailConfig


settings = Settings()
