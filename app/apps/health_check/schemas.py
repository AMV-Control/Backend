from enum import Enum

from pydantic import BaseModel


class HealthCheckStatus(str, Enum):
    OK = 'ok'
    ERROR = 'error'


class HealthCheckResult(BaseModel):
    status: HealthCheckStatus
    detail: str

    class Config:
        orm_mode = True
