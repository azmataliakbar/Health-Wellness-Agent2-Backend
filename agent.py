import asyncio
from typing import Optional
from context import UserSessionContext
from tools.goal_analyzer import analyze_goal
from tools.meal_planner import generate_meal_plan
from tools.workout_recommender import recommend_workout

class HealthWellnessAgent:
    def __init__(self):
        self.tools = {
            "analyze_goal": analyze_goal,
            "generate_meal_plan": generate_meal_plan,
            "recommend_workout": recommend_workout
        }

    async def handle_message(self, input: str, context: Optional[UserSessionContext] = None) -> str:
        if context is None:
            context = UserSessionContext()
        
        try:
            if any(kw in input.lower() for kw in ["meal", "diet", "food"]):
                return await generate_meal_plan(input, context)
            elif any(kw in input.lower() for kw in ["workout", "exercise"]):
                return await recommend_workout(input, context)
            else:
                return await analyze_goal(input, context)
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"