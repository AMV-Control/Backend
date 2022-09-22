import os
from typing import AsyncGenerator, Callable

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy_utils import database_exists, drop_database

from alembic import command
from alembic.config import Config
from app.core.config import settings

# устанавливаем `os.environ`, чтобы использовать тестовую БД
os.environ['TESTING'] = 'True'


@pytest.fixture(scope='session')
def anyio_backend():
    return 'asyncio'


@pytest.fixture(scope='module')
def db_engine():
    engine = create_async_engine(settings.TEST_DATABASE_URL,
                                 pool_pre_ping=True, echo=True)

    # удаляем старую тестовую базу данных
    if database_exists(engine.url):
        drop_database(engine.url)

    # загружаем конфигурацию alembic
    alembic_cfg = Config('alembic.ini')

    # выполняем миграции
    command.upgrade(alembic_cfg, 'head')

    yield engine

    # после выполнения тестов, удаляем тестовую базу данных
    drop_database(engine.url)


@pytest.fixture()
async def db_session(db_engine: AsyncEngine) -> AsyncGenerator:
    async with db_engine.begin() as connection:
        async with AsyncSession(bind=connection) as session:
            yield session
            await session.flush()
            await session.rollback()


@pytest.fixture()
def override_get_session(db_session: AsyncSession) -> Callable:
    async def _override_get_db():
        yield db_session

    return _override_get_db


@pytest.fixture()
def app(override_get_session) -> FastAPI:
    from app.core.database import get_session
    from app.main import app

    app.dependency_overrides[get_session] = override_get_session
    return app


@pytest.fixture()
async def async_client(app: FastAPI) -> AsyncGenerator:
    async with AsyncClient(app=app, base_url='http://test') as ac:
        yield ac
