from flask import Flask, jsonify
import aiohttp
import asyncio
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)


API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


@app.route("/")
def home():
    return jsonify({
        "message": "Weather API Integration is running"
    })


@app.route("/weather/<city>")
def get_weather(city):

    async def fetch_weather():
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    BASE_URL,
                    params=params,
                    timeout=aiohttp.ClientTimeout(total=10)
                ) as response:

                    if response.status == 404:
                        return {
                            "error": "City not found"
                        }, 404

                    if response.status != 200:
                        return {
                            "error": "Weather API request failed"
                        }, response.status

                    data = await response.json()

                    
                    weather_data = {
                        "city": data["name"],
                        "country": data["sys"]["country"],
                        "temperature": data["main"]["temp"],
                        "feels_like": data["main"]["feels_like"],
                        "humidity": data["main"]["humidity"],
                        "weather": data["weather"][0]["description"],
                        "wind_speed": data["wind"]["speed"]
                    }

                    return weather_data, 200

        except asyncio.TimeoutError:
            return {
                "error": "Weather API request timed out"
            }, 504

        except aiohttp.ClientError:
            return {
                "error": "Unable to connect to weather service"
            }, 503

   
    weather_data, status_code = asyncio.run(fetch_weather())

    return jsonify(weather_data), status_code


if __name__ == "__main__":
    app.run(debug=True)