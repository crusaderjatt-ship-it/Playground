# AI Trend Radar

AI-powered web app that discovers trending AI tools and auto-generates viral X content.

## Stack
- Backend: FastAPI
- Frontend: React + Vite + TypeScript
- Storage: SQLite (SQLModel)
- Jobs: APScheduler

## Quick start
### Backend
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Core capabilities
- Daily multi-source trend discovery pipeline
- Scoring by virality, growth velocity, usefulness, search demand
- Deduplication of previously covered tools
- AI content generation for posts, hooks, threads, CTAs, hashtags
- Infographic concept generation for 1:1 and 16:9
- Virality optimization predictions and scheduling suggestions
- Dashboard analytics APIs + filter endpoints
