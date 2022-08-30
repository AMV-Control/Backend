from sqlmodel import SQLModel, Field


class HealthCheckResult(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    status: str = Field()
    detail: str = Field()
