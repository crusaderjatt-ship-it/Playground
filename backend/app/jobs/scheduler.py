from apscheduler.schedulers.background import BackgroundScheduler

from app.services.discovery import trend_discovery_service


scheduler = BackgroundScheduler(timezone="UTC")


def start_scheduler():
    def daily_discovery_job():
        trend_discovery_service.discover(
            [
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
        )

    scheduler.add_job(daily_discovery_job, "cron", hour=7, minute=0, id="daily_discovery", replace_existing=True)
    scheduler.start()
