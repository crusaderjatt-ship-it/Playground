# AI Trend Radar

AI-powered web app that discovers trending AI tools and auto-generates viral X content.

[![Deploy to Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/YOUR_GITHUB_USERNAME/ai-trend-radar&env=DATABASE_URL,OPENAI_MODEL,SCHEDULER_CRON,X_BEARER_TOKEN,REDDIT_CLIENT_ID,REDDIT_CLIENT_SECRET,YOUTUBE_API_KEY,NEWS_API_KEY&envDescription=Set%20Postgres%20and%20optional%20source%20API%20credentials&project-name=ai-trend-radar&repository-name=ai-trend-radar)

## Stack
- Frontend: React + Vite + TypeScript
- API: FastAPI (Vercel Python Functions)
- Storage: SQLite locally, Supabase Postgres in production
- Automation: Vercel Cron job (`/api/cron` at 07:00 UTC)

## Environment variables
1. Copy `.env.example` to `.env`.
2. Fill values (at minimum `DATABASE_URL` in production).

```bash
cp .env.example .env
```

## Local development
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

## Supabase Postgres migration (production persistence)
1. Create a Supabase project and copy the connection string.
2. Set `DATABASE_URL` as:
   - `postgresql+psycopg://postgres:<PASSWORD>@<PROJECT-REF>.supabase.co:5432/postgres?sslmode=require`
3. Run the SQL migration in Supabase SQL editor:
   - `supabase/migrations/20260512070000_init_ai_trend_radar.sql`
4. (Optional) backfill existing local SQLite data with a one-time script.

## Deploy to Vercel
1. Push this repo to GitHub.
2. Click the **Deploy to Vercel** button above (or import manually in Vercel).
3. Confirm root path is `/`.
4. Set environment variables from `.env.example` in Vercel Project Settings.
5. Deploy — Vercel uses `vercel.json` to:
   - build frontend from `frontend/`
   - serve static files from `frontend/dist`
   - route `/api/*` to FastAPI (`api/index.py`)
   - run daily cron at `/api/cron`

## Core capabilities
- Daily multi-source trend discovery pipeline
- Scoring by virality, growth velocity, usefulness, search demand
- Deduplication of previously covered tools
- AI content generation for posts, hooks, threads, CTAs, hashtags
- Infographic concept generation for 1:1 and 16:9
- Virality optimization predictions and scheduling suggestions
- Dashboard analytics APIs + filter endpoints
