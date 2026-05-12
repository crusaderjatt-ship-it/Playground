from fastapi import FastAPI

from backend.app.services.discovery import trend_discovery_service

app = FastAPI(title="AI Trend Radar Cron")


@app.get("/api/cron")
def run_daily_discovery():
    sources = [
        "producthunt",
        "reddit",
        "hackernews",
        "x_trends",
        "github_trending",
        "youtube",
        "newsletters",
        "google_trends",
        "directories",
        "linkedin",
        "news_api",
        "rss",
    ]
    items = trend_discovery_service.discover(sources)
    return {"discovered": len(items), "sources": len(sources)}
