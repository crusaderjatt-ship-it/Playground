from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class GeneratedContent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tool_id: int = Field(index=True)
    tone: str = Field(index=True)
    tweets_json: str
    hooks_json: str
    thread_idea: str
    cta: str
    hashtags_json: str
    infographic_json: str
    caution: str
    emotional_angles_json: str
    predicted_engagement: float = 0
    predicted_virality: float = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
