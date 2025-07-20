# tools/workout_recommender.py
import asyncio
from context import UserSessionContext

async def recommend_workout(input: str, context) -> str:
    await asyncio.sleep(0)  # Makes it truly async
    
    workouts = {
        "cardio": "30 min running + 15 min cycling",
        "strength": "3 sets of squats, pushups, pullups",
        "hiit": "20 sec sprint, 40 sec walk (10 rounds)"
    }
    
    for workout_type in workouts:
        if workout_type in input.lower():
            return f"Recommended {workout_type} workout: {workouts[workout_type]}"
    
    return "Recommended balanced workout: 20 min cardio + 20 min strength training"