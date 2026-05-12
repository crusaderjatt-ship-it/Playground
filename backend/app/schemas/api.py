from typing import List

from pydantic import BaseModel


class DiscoveryRequest(BaseModel):
    sources: List[str]


class ContentRequest(BaseModel):
    tool_id: int
    tones: List[str] = ["professional", "viral", "humorous", "serious", "inspirational", "minimal"]


class ToolFilter(BaseModel):
    audience: str | None = None
    industry: str | None = None
    category: str | None = None
    free_only: bool | None = None
    min_trending_score: float | None = None
    min_virality_score: float | None = None
