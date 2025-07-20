# agents/injury_support_agent.py
from typing import Any
import asyncio

class InjurySupportAgent:
    async def handle_message(self, context: Any) -> str:
        """Provide injury support advice (async implementation)"""
        await asyncio.sleep(0)  # Makes this truly async
        return "Please consult with a physical therapist for personalized injury support."