from fastapi import APIRouter, Depends, Response, status

from app.apps.health_check.services.health_checker import HealthCheckService
from . import schemas

router = APIRouter(prefix='/health_check', tags=['health_check'])


@router.get('/', response_model=schemas.HealthCheckResult)
async def health_check(response: Response, service: HealthCheckService = Depends()):
    health_check_result = await service.health_check()

    if health_check_result.status != schemas.HealthCheckStatus.OK:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    return health_check_result
