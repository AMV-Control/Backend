from datetime import datetime

from sqlmodel import SQLModel, Field, text


class HealthCheck(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    status: str = Field()
