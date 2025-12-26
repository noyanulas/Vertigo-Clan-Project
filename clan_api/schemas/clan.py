from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

class ClanCreate(BaseModel):
    name: str
    region: str

class ClanOut(BaseModel):
    id: UUID
    name: str
    region: str
    created_at: datetime

    class Config:
        from_attributes = True  # SQLAlchemy → Pydantic
