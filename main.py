yfrom fastapi import FastAPI, Query
import requests
import openai
import os

from openai import OpenAI

app = FastAPI()

# Load your keys here
OPENWEATHER_API_KEY = "key"

client = OpenAI(api_key ='your api secret key here'
)
@app.get("/")
def read_root():
    return {"message": "Use /weather?city=YourCity to get weather forecast"}

@app.get("/weather")
def get_weather(city: str = Query(..., description="City name to get weather forecast")):
    # Step 1: Call OpenWeatherMap API
    weather_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    weather_response = requests.get(weather_url, params=params)
    if weather_response.status_code != 200:
        return {"error": "Weather API call failed", "details": weather_response.json()}

    weather_data = weather_response.json()
    desc = weather_data["weather"][0]["description"]
    temp = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]

    # Step 2: Compose prompt for OpenAI
    prompt = (
        f"The weather in {city} is currently {desc}, "
        f"with a temperature of {temp}°C and it feels like {feels_like}°C. "
        f"Describe this in a fun way to a Minecraft player."
    )

    try:
        gpt_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a fun assistant for Minecraft players."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )
        response_text = gpt_response.choices[0].message.content

        return {
            "city": city,
            "weather": {
                "description": desc,
                "temperature": f"{temp}°C",
                "feels_like": f"{feels_like}°C"
            },
            "message": response_text
        }

    except Exception as e:
        return {"error": "OpenAI API call failed", "details": str(e)}
