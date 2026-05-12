from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Trend Radar"
    database_url: str = "sqlite:///./ai_trend_radar.db"
    openai_model: str = "gpt-4.1-mini"
    scheduler_cron: str = "0 7 * * *"
    x_bearer_token: str = ""
    reddit_client_id: str = ""
    reddit_client_secret: str = ""
    youtube_api_key: str = ""
    news_api_key: str = ""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
