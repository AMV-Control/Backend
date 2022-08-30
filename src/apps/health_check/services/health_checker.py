from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .. import schemas
from .. import models
from src.core.database import get_session


class HealthCheckService:

    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session

    async def _run_health_checks(self):
        """
        Функция запуска проверок работы приложения

        Если проверка не проходит, должно вызываться исключение
        """

        # TODO: добавить проверки работы приложения

        return True

    async def health_check(self) -> models.HealthCheckResult:
        """
        Проверка работы приложения
        """
        status = schemas.HealthCheckStatus.OK
        detail = ''
        try:
            await self._run_health_checks()
        except Exception as e:
            status = schemas.HealthCheckStatus.ERROR
            detail = str(e)

        health_check_result = models.HealthCheckResult(
            status=status,
            detail=detail
        )

        self.session.add(health_check_result)
        await self.session.commit()
        await self.session.refresh(health_check_result)

        return health_check_result
