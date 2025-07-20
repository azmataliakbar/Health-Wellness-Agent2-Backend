# tools/meal_planner.py
import asyncio
from context import UserSessionContext

async def generate_meal_plan(input: str, context) -> str:
    await asyncio.sleep(0)
    
    plans = {
        "vegetarian": ["Lentil curry", "Veg stir fry", "Falafel wrap"],
        "vegan": ["Tofu scramble", "Chickpea salad", "Vegan chili"],
        "gluten-free": ["Grilled salmon", "Quinoa bowl", "Roast chicken"]
    }
    
    for diet_type in plans:
        if diet_type in input.lower():
            return f"{diet_type.capitalize()} meal plan:\n" + "\n".join(f"- {meal}" for meal in plans[diet_type])
    
    return "Standard meal plan:\n- Grilled chicken\n- Steamed veggies\n- Brown rice"