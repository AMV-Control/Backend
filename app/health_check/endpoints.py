from fastapi import APIRouter, Depends

from app.health_check.services import HealthChecker
from . import schemas

router = APIRouter(prefix='/health_check', tags=['health_check'])


@router.get('/', response_model=schemas.HealthCheck)
async def health_check(service: HealthChecker = Depends()):
    return service.health_check()
