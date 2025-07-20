# Health & Wellness Planner Agent

🌿 An AI-powered health and wellness assistant built with OpenAI Agents SDK

## Features

- Natural language understanding of health/fitness goals
- Personalized meal plan generation
- Custom workout recommendations
- Progress tracking
- Specialized agent handoffs (nutrition, injury support)
- Real-time streaming responses

## Project Structure
health_wellness_agent/
├── main.py # CLI interface
├── agent.py # Main agent logic
├── context.py # User session management
├── guardrails.py # Input/output validation
├── requirements.txt # Dependencies
├── tools/ # All agent tools
└── agents/ # Specialized agents


## Installation

1. Clone this repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac)
   venv\Scripts\activate    # Windows

Install dependencies:
   pip install -r requirements.txt

   (.venv) C:\Users\WWW.SZLAIWIIT.COM\python_projects\health_wellness_agent1>python main.py
🌿 Health & Wellness Assistant 🌿
You: "I want to lose 10 pounds in 2 months
Assistant: Focus on cardio and calorie deficit
You: How can I build muscle effectively?
Assistant: Focus on strength training and protein
You: My goal is to improve my endurance
Assistant: Your goal has been recorded. How can I help further?
You: Can you suggest a vegetarian meal plan?
Assistant: Vegetarian meal plan:
- Lentil curry
- Veg stir fry
- Falafel wrap
You: I need gluten-free meal ideas
Assistant: Gluten-free meal plan:
- Grilled salmon
- Quinoa bowl
- Roast chicken
You: What's a good vegan diet for weight loss?
Assistant: Vegan meal plan:
- Tofu scramble
- Chickpea salad
- Vegan chili
You: Recommend a cardio workout routine
Assistant: Recommended cardio workout: 30 min running + 15 min cycling
You: Suggest strength training exercises
Assistant: Recommended strength workout: 3 sets of squats, pushups, pullups
You: What's a good HIIT workout?
Assistant: Recommended hiit workout: 20 sec sprint, 40 sec walk (10 rounds)
You: I want to lose weight - suggest meals and workouts
Assistant: Standard meal plan:
- Grilled chicken
- Steamed veggies
- Brown rice
You: Help me build muscle with diet and exercise plans
Assistant: Standard meal plan:
- Grilled chicken
- Steamed veggies
- Brown rice
You: How can I improve my sleep quality?
Assistant: Your goal has been recorded. How can I help further?
You: What are some healthy breakfast options?
Assistant: Your goal has been recorded. How can I help further?
You: Suggest ways to reduce stress
Assistant: Your goal has been recorded. How can I help further?
You: exit

(.venv) C:\Users\WWW.SZLAIWIIT.COM\python_projects\health_wellness_agent1>

https://www.microsoft.com/en-gb/windows/laptop-buying-guide?persona=GP_T2_EOS_WW&OCID=CGE_inp_Devices_EOS_868dk7xtu&form=M7001T&msclkid=32578b2bdb9e125cabbde350e87b2587#retailer-panel-banner

# -----------------------------------------------------------------

🎯 Goal
Keep fast_api.py always online (as backend API)

Deploy Next.js frontend that communicates with the backend

Ensure both work even after system restart

Use a free or affordable hosting solution

✅ Your Deployment Options
🔁 Backend (FastAPI) Hosting Options
| Platform           | Free Tier                                | Notes                          |
| ------------------ | ---------------------------------------- | ------------------------------ |
| **Render**         | ✅ Yes                                    | Easiest for FastAPI            |
| **Railway**        | ✅ Yes                                    | Good, simple UI                |
| **Replit**         | ✅ Free basic plan                        | Easy but can sleep             |
| **Deta**           | ❌ No longer supports new Python projects |                                |
| **Fly.io**         | ✅ Yes                                    | Lightweight, more setup        |
| **PythonAnywhere** | ✅ Yes                                    | Best for small FastAPI apps    |
| **Vercel**         | ❌ Not for Python                         | Only for frontend like Next.js |

⚠️ Note: Free plans on Render and Railway can sleep after 15 minutes of inactivity (can be re-woken when visited).

🌐 Step-by-Step Guide to Deploy FastAPI on Render
1. Prepare Your Backend Project for Deployment

Inside backend/, create these 2 files:

requirements.txt
fastapi
uvicorn
openai

start.sh
#!/bin/bash
uvicorn fast_api:app --host=0.0.0.0 --port=10000

Make sure fast_api.py has this line:
app = FastAPI()

2. Push backend/ to GitHub

Create a new GitHub repo

Only push the backend/ folder (or full project if you want)

3. Deploy on Render

Go to: https://dashboard.render.com/

Click "New + → Web Service"

Connect GitHub
Choose your repo and backend/ folder
Build Command: (leave empty or pip install -r requirements.txt)
Start Command: bash start.sh
Set environment variable (in Render Dashboard):

OPENAI_API_KEY=your-key

Now your FastAPI backend is always online ✅

🚀 Update Next.js to Talk to Live Backend
In frontend/.env.local:

NEXT_PUBLIC_BACKEND_URL=https://your-backend-name.onrender.com

Make sure your API calls use:

fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/query`, { ... })

✅ Frontend (Next.js) Hosting
Best options:

Vercel → Best for Next.js

Netlify → Also easy

Steps for Vercel:

Push frontend/ to GitHub

Go to https://vercel.com/

Click “New Project”

Connect GitHub and select your repo

Set environment variable:

ini
Copy
Edit
NEXT_PUBLIC_BACKEND_URL=https://your-backend-name.onrender.com
Deploy

🌍 Result:
Your backend (FastAPI) runs on Render ✅

Your frontend (Next.js) runs on Vercel ✅

User opens frontend → It talks to live backend → AI gives response ✅

🆓 Free Hosting Summary

| Use                | Platform | Free? | Sleeps?          |
| ------------------ | -------- | ----- | ---------------- |
| Backend (FastAPI)  | Render   | ✅     | Yes (wakes up)   |
| Backend (FastAPI)  | Railway  | ✅     | Yes (wakes up)   |
| Frontend (Next.js) | Vercel   | ✅     | No (very stable) |

Press Ctrl + Shift + P → type Python: Select Interpreter


