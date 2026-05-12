from __future__ import annotations

import hashlib
import random
from dataclasses import dataclass
from typing import Iterable, List

from app.models.tool import Tool


@dataclass
class DiscoveryItem:
    name: str
    category: str
    audience: str
    description: str
    source: str
    url: str


class TrendDiscoveryService:
    """Pluggable discovery engine for Product Hunt, Reddit, HN, GitHub, etc."""

    def discover(self, sources: Iterable[str]) -> List[DiscoveryItem]:
        # Placeholder adapters. Replace with real API clients and scrapers.
        sample = [
            DiscoveryItem(
                name="PromptPilot",
                category="Productivity",
                audience="Working professionals",
                description="Automates repetitive writing workflows.",
                source=src,
                url=f"https://example.com/{src}/promptpilot",
            )
            for src in sources
        ]
        return self._dedupe(sample)

    def score(self, item: DiscoveryItem) -> dict[str, float]:
        seed = int(hashlib.md5(item.name.encode()).hexdigest(), 16)
        random.seed(seed)
        growth = random.uniform(60, 95)
        engagement = random.uniform(55, 98)
        search = random.uniform(50, 96)
        usefulness = random.uniform(65, 99)
        trending = 0.35 * growth + 0.30 * engagement + 0.20 * search + 0.15 * usefulness
        return {
            "growth_velocity": round(growth, 2),
            "virality_score": round(engagement, 2),
            "usefulness_score": round(usefulness, 2),
            "trending_score": round(trending, 2),
        }

    def _dedupe(self, items: List[DiscoveryItem]) -> List[DiscoveryItem]:
        seen = set()
        out: List[DiscoveryItem] = []
        for item in items:
            key = item.name.lower().strip()
            if key in seen:
                continue
            seen.add(key)
            out.append(item)
        return out


trend_discovery_service = TrendDiscoveryService()
