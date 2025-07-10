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


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class AuthConfig(BaseModel):
    user: str
    password: str


class MongoDatabaseConfig(BaseModel):
    url: MongoDsn
    db_name: str


class SMTPConfig(BaseModel):
    user: str
    password: str
    host: str
    port: int


class EmailConfig(BaseModel):
    recievers_domain: str
    hosts_report_subject: str = "[Report] Check your hosts"


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
