-- AI Trend Radar initial schema for Supabase Postgres

create table if not exists public.tool (
  id serial primary key,
  name varchar(255) not null,
  category varchar(100) not null,
  source varchar(100) not null,
  url varchar(1024) not null,
  trending_score float not null,
  virality_score float not null,
  growth_velocity float not null,
  usefulness_score float not null,
  search_popularity float not null,
  audience_type varchar(100) not null,
  pricing_type varchar(50) not null,
  is_covered boolean not null default false,
  discovered_at timestamp not null default now()
);

create unique index if not exists uq_tool_name_source on public.tool (name, source);
create index if not exists idx_tool_trending_score on public.tool (trending_score desc);
create index if not exists idx_tool_audience_type on public.tool (audience_type);
create index if not exists idx_tool_category on public.tool (category);

create table if not exists public.generatedcontent (
  id serial primary key,
  tool_id int not null references public.tool(id) on delete cascade,
  tone varchar(50) not null,
  tweet_variations jsonb not null,
  hook_variations jsonb not null,
  thread_idea text not null,
  infographic jsonb not null,
  cta text not null,
  caution text not null,
  hashtags jsonb not null,
  emotional_angles jsonb not null,
  predicted_engagement float not null,
  predicted_virality float not null,
  suggested_times jsonb not null,
  created_at timestamp not null default now()
);

create index if not exists idx_generatedcontent_tool_id on public.generatedcontent (tool_id);
create index if not exists idx_generatedcontent_created_at on public.generatedcontent (created_at desc);
