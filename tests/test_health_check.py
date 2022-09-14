import pytest
from fastapi import status
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.apps.health_check import models


@pytest.mark.anyio
async def test_read_item(async_client: AsyncClient, db_session: AsyncSession):
    result = await db_session.execute(select(models.HealthCheckResult))
    initial_health_check_count = len(result.fetchall())

    response = await async_client.get('/api/health_check/')

    result = await db_session.execute(select(models.HealthCheckResult))
    new_health_check_count = len(result.fetchall())

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'detail': '', 'status': 'ok'}
    assert new_health_check_count == initial_health_check_count + 1
