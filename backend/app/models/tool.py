from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Tool(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    category: str = Field(index=True)
    audience: str = Field(index=True)
    description: str
    source: str
    url: str
    trending_score: float = 0
    virality_score: float = 0
    growth_velocity: float = 0
    usefulness_score: float = 0
    is_free: bool = True
    pricing_summary: str = "Unknown"
    created_at: datetime = Field(default_factory=datetime.utcnow)
