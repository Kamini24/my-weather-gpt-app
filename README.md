# my-weather-gpt-app
# 🧱 MCP Weather Server ⛅
### Ask the Weather Like a Minecraft Pro! Built with FastAPI + OpenAI + Docker + AWS

---

![Banner](https://yourdomain.com/path-to-thumbnail.png) <!-- Replace with real URL if hosted -->

## 🧩 What is this?

**MCP Weather Server** is a fun, intelligent weather bot that responds like a Minecraft villager with LLM flair. It combines:
- 🌐 Real-time weather from [OpenWeatherMap API](https://openweathermap.org)
- 🤖 AI responses from [OpenAI](https://openai.com)
- 🚀 FastAPI-powered backend
- 📦 Docker for containerized deployment
- ☁️ Hosted on AWS (Free Tier friendly!)

---

## 🌦️ Features

- 🔍 Ask weather for any city
- 🧠 LLM-generated quirky responses (e.g., *"In Bangalore, the skies are clear as diamond armor!"*)
- ⚡ FastAPI for blazing-fast APIs
- 📦 Docker support
- 🧱 Minecraft-themed UI (Tailwind CSS)
- 🛡️ Scalable for future Agentic AI integrations

---

## 🛠️ Tech Stack

| Layer         | Technology           |
|---------------|----------------------|
| Backend       | FastAPI              |
| AI/LLM        | OpenAI API           |
| Weather Data  | OpenWeatherMap       |
| UI            | HTML + Tailwind CSS  |
| Container     | Docker               |
| Deployment    | AWS EC2 (Free Tier)  |

---

## 🚀 Quick Start

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/mcp-weather-server.git
cd mcp-weather-server
2. Setup Environment Variables
Create a .env file:

env
Copy
Edit
OPENAI_API_KEY=your_openai_key
OPENWEATHER_API_KEY=your_weather_key
3. Run with Docker
bash
Copy
Edit
docker build -t mcp-weather .
docker run -p 8000:8000 --env-file .env mcp-weather
Visit http://localhost:8000

🌐 API Usage
GET /weather?city=London
Example response:

json
Copy
Edit
{
  "city": "London",
  "weather": {
    "description": "light rain",
    "temperature": 19
  },
  "message": "Ah, brave adventurer! Rain drizzles softly over London, like a creeper sneaking in the night."
}
🧠 LLM Prompt Design
We craft custom prompts to convert weather data into immersive Minecraft-style replies using OpenAI's GPT API.

python
Copy
Edit
prompt = f"""
You're a Minecraft villager NPC giving weather updates.
Current city: {city}
Weather: {description}, Temp: {temp}°C

Reply in a blocky, immersive Minecraft voice.
"""
📁 Project Structure
pgsql
Copy
Edit
.
├── app/
│   ├── main.py         # FastAPI app
│   ├── ai.py           # OpenAI logic
│   ├── weather.py      # Weather API wrapper
│   └── templates/      # Static HTML + CSS
├── Dockerfile
├── .env
├── requirements.txt
└── README.md
🌍 Deployment on AWS EC2 (Free Tier)
Create EC2 instance (Ubuntu)

SSH into it

Install Docker

Pull your repo and run the Docker container

Use Nginx as reverse proxy (optional)

Add HTTPS with Let's Encrypt

🔮 Future Scope
🎤 Voice-based weather commands

🎮 Minecraft server integration

💬 Telegram/Discord bot version

🧠 Multi-agent LLMs for immersive storytelling

📈 Weather analytics and trend visualizations

📸 Preview
<!-- Replace with real UI screenshot -->

👨‍💻 Author
Kamini Kumari
Staff Engineer | Cloud | AI Enthusiast
🔗 LinkedIn
💻 Portfolio

