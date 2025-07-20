# agents/nutrition_expert_agent.py
from typing import Any
import asyncio

class NutritionExpertAgent:
    async def handle_message(self, context: Any) -> str:
        """Provide nutrition advice (async implementation)"""
        await asyncio.sleep(0)
        return "Nutrition advice: Focus on whole foods and balanced meals."