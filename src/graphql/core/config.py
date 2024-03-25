import os
from pathlib import Path

from dotenv import load_dotenv

from pydantic.v1 import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
ENV_FILE = os.path.join(BASE_DIR, 'envs', '.env')
load_dotenv(ENV_FILE)


class Settings(BaseSettings):
    PROJECT_TITLE: str = "Fast Api GraphQL Strawberry"
    PROJECT_VERSION: str = "0.0.1"
    HOST_HTTP: str = os.getenv("HOST_HTTP", "http://")
    HOST_URL: str = os.getenv("HOST_URL")
    HOST_PORT: int = int(os.getenv("HOST_PORT"))
    BASE_URL: str = HOST_HTTP + HOST_URL + ":" + str(HOST_PORT)
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", 5432))
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()
