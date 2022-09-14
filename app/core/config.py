from typing import List, Union

from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    PROJECT_NAME: str
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator('BACKEND_CORS_ORIGINS', pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith('['):
            return [i.strip() for i in v.split(',')]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # примеры строк подключений к базе данных:
    # - sqlite+aiosqlite:///./db.sqlite3
    # - postgresql+asyncpg://postgres:postgres@database:5432/app
    DATABASE_URL: str

    # база данных для тестов
    TEST_DATABASE_URL: str = 'sqlite+aiosqlite:///./test_db.sqlite3'

    class Config:
        case_sensitive = True
        env_file = '.env'


settings = Settings()
