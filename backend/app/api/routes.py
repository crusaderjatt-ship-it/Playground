from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select

from app.core.db import get_session
from app.models.content import GeneratedContent
from app.models.tool import Tool
from app.schemas.api import ContentRequest, DiscoveryRequest
from app.services.content_gen import content_generation_service
from app.services.discovery import trend_discovery_service

router = APIRouter(prefix="/api", tags=["AI Trend Radar"])


@router.post("/discover")
def discover_tools(payload: DiscoveryRequest, session: Session = Depends(get_session)):
    discovered = trend_discovery_service.discover(payload.sources)
    created = []
    for item in discovered:
        scores = trend_discovery_service.score(item)
        tool = Tool(**item.__dict__, **scores)
        session.add(tool)
        created.append(tool)
    session.commit()
    return {"count": len(created), "tools": created}


@router.get("/tools")
def list_tools(
    audience: str | None = None,
    category: str | None = None,
    free_only: bool | None = Query(default=None),
    min_trending: float | None = None,
    min_virality: float | None = None,
    session: Session = Depends(get_session),
):
    stmt = select(Tool)
    if audience:
        stmt = stmt.where(Tool.audience == audience)
    if category:
        stmt = stmt.where(Tool.category == category)
    if free_only is not None:
        stmt = stmt.where(Tool.is_free == free_only)
    if min_trending is not None:
        stmt = stmt.where(Tool.trending_score >= min_trending)
    if min_virality is not None:
        stmt = stmt.where(Tool.virality_score >= min_virality)
    return session.exec(stmt.order_by(Tool.trending_score.desc())).all()


@router.post("/generate-content")
def generate_content(payload: ContentRequest, session: Session = Depends(get_session)):
    tool = session.get(Tool, payload.tool_id)
    if not tool:
        return {"error": "Tool not found"}

    outputs = []
    for tone in payload.tones:
        result = content_generation_service.generate(tool, tone)
        row = GeneratedContent(
            tool_id=tool.id,
            tone=tone,
            tweets_json=str(result["tweets"]),
            hooks_json=str(result["hooks"]),
            thread_idea=result["thread_idea"],
            cta=result["cta"],
            hashtags_json=str(result["hashtags"]),
            infographic_json=str(result["infographic"]),
            caution=result["caution"],
            emotional_angles_json=str(result["emotional_angles"]),
            predicted_engagement=result["predicted_engagement"],
            predicted_virality=result["predicted_virality"],
        )
        session.add(row)
        outputs.append(result)
    session.commit()
    return {"tool": tool.name, "variants": outputs}


@router.get("/dashboard")
def dashboard(session: Session = Depends(get_session)):
    tools = session.exec(select(Tool).order_by(Tool.trending_score.desc()).limit(10)).all()
    posts = session.exec(select(GeneratedContent).order_by(GeneratedContent.predicted_virality.desc()).limit(10)).all()
    return {
        "trending_tools_today": tools,
        "most_viral_generated_posts": posts,
        "best_hooks": ["Problem-solution", "FOMO", "Before/after"],
        "recommended_posting_windows_et": ["08:30", "12:15", "18:45"],
    }
