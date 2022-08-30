from fastapi import APIRouter

from src.apps.health_check.endpoints import router as health_check_router

router = APIRouter()
router.include_router(health_check_router)
