from sqlmodel import Session, SQLModel, create_engine

from app.core.config import settings


def _engine_kwargs(db_url: str) -> dict:
    if db_url.startswith("sqlite"):
        return {"echo": False, "connect_args": {"check_same_thread": False}}
    return {"echo": False, "pool_pre_ping": True}


engine = create_engine(settings.database_url, **_engine_kwargs(settings.database_url))
engine = create_engine(settings.database_url, echo=False)


def init_db() -> None:
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
