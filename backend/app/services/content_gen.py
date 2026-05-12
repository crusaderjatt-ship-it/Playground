from __future__ import annotations

from app.models.tool import Tool


class ContentGenerationService:
    def generate(self, tool: Tool, tone: str) -> dict:
        base = f"{tool.name} helps {tool.audience.lower()} save time and move faster."
        tweets = [
            f"Just found {tool.name} and it is wild. {base} #AI #Productivity",
            f"If you're still doing this manually, you're wasting hours. {tool.name} fixes it.",
            f"{tool.name}: less busywork, more output. This one is going to trend.",
            f"I tested {tool.name} so you don't have to: faster workflows, cleaner results.",
            f"Hidden AI gem: {tool.name}. Early adopters will win big.",
        ]
        hooks = [
            f"This AI tool can save you 10+ hours/week.",
            f"Most people haven't discovered {tool.name} yet.",
            f"Before {tool.name}: chaos. After: streamlined execution.",
        ]
        return {
            "tone": tone,
            "tweets": tweets,
            "hooks": hooks,
            "thread_idea": f"Break down 5 ways {tool.name} improves ROI for {tool.audience.lower()}.",
            "cta": "Reply 'TOOL' and I’ll send a starter workflow.",
            "hashtags": ["#AI", "#AITools", "#Productivity", "#Startups", "#Automation"],
            "infographic": {
                "formats": ["1:1", "16:9"],
                "sections": [
                    "Problem",
                    "How it works",
                    "Time saved",
                    "ROI estimate",
                    "Risks/Cautions",
                    "Alternatives",
                    "Pricing",
                    "Best users",
                ],
            },
            "caution": "Always verify outputs for factual accuracy and data privacy compliance.",
            "emotional_angles": ["FOMO", "Curiosity", "Empowerment"],
            "predicted_engagement": 82.0,
            "predicted_virality": 79.0,
            "suggested_posting_times_et": ["08:30", "12:15", "18:45"],
            "target_audience": tool.audience,
        }


content_generation_service = ContentGenerationService()
