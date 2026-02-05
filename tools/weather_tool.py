import requests
import os
from dotenv import load_dotenv
load_dotenv()


def weather_lookup(city: str):

    api_key = os.getenv("WEATHER_API_KEY")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    res = requests.get(url).json()

    return {
        "city": city,
        "temperature": res["main"]["temp"],
        "weather": res["weather"][0]["description"]
    }
