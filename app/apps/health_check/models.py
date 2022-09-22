from sqlmodel import Field

from app.core.database import BaseSQLModel


class HealthCheckResult(BaseSQLModel, table=True):
    status: str = Field()
    detail: str = Field()
