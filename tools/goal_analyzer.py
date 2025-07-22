import asyncio
from context import UserSessionContext

async def analyze_goal(input: str, context) -> str:
    await asyncio.sleep(0)
    input_lower = input.lower()
    
    # Weight Loss/Fat Reduction
    if any(word in input_lower for word in [
        "lose", "weight loss", "fat", "slim", "lean", 
        "burn fat", "reduce weight", "cutting"
    ]):
        return (
            "For weight loss focus on:\n"
            "1. Cardio 3-5x weekly (walking/running)\n"
            "2. Moderate calorie deficit (300-500cal)\n"
            "3. High-protein meals (1.6-2.2g/kg)\n"
            "4. Strength training to maintain muscle"
        )
    
    # Weight Gain
    elif any(word in input_lower for word in [
        "gain weight", "increase weight", "put on weight",
        "weight gain", "bulk up", "add pounds"
    ]):
        return (
            "For healthy weight gain:\n"
            "1. Calorie surplus (300-500cal above maintenance)\n"
            "2. Strength training 3-4x weekly\n"
            "3. Eat protein-rich meals (1.6-2.2g/kg)\n"
            "4. Include healthy carbs (rice, oats, potatoes)\n"
            "5. Track progress weekly"
        )
    
    # Muscle Building
    elif any(word in input_lower for word in [
        "build", "muscle", "gain mass", "bulk",
        "get bigger", "hypertrophy"
    ]):
        return (
            "For muscle building:\n"
            "1. Progressive overload training\n"
            "2. Compound lifts (squats, deadlifts)\n"
            "3. High-protein diet (1.6-2.2g/kg)\n"
            "4. Calorie surplus (200-500cal)\n"
            "5. 7-9 hours sleep nightly"
        )
    
    # General Fitness
    elif any(word in input_lower for word in [
        "fitness", "tone", "endurance", "get fit",
        "in shape", "toned"
    ]):
        return (
            "For general fitness:\n"
            "1. Mix strength & cardio\n"
            "2. Full-body workouts 3x weekly\n"
            "3. Balanced nutrition\n"
            "4. Include flexibility work"
        )
    
    # Strength Training
    elif any(word in input_lower for word in [
        "strength", "power", "get stronger",
        "lift more", "powerlifting"
    ]):
        return (
            "For strength gains:\n"
            "1. Heavy compound lifts\n"
            "2. Low reps (3-6) with max weight\n"
            "3. Longer rest between sets (2-5min)\n"
            "4. Focus on form first"
        )
    
    # Health/Wellness
    elif any(word in input_lower for word in [
        "health", "wellness", "healthy lifestyle",
        "wellbeing", "overall health"
    ]):
        return (
            "For overall health:\n"
            "1. Balanced whole-food diet\n"
            "2. 150min exercise weekly\n"
            "3. 7-9 hours quality sleep\n"
            "4. Stress management"
        )
    
    else:
        # ✅ Instead of a message, return fallback trigger
        return "__FALLBACK__"
