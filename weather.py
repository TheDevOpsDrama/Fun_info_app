import requests

def get_weather(city):
    try:
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo_response = requests.get(geo_url).json()

        if "results" not in geo_response:
            return f"❌ City '{city}' not found."

        lat = geo_response["results"][0]["latitude"]
        lon = geo_response["results"][0]["longitude"]

        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_response = requests.get(weather_url).json()

        temp = weather_response["current_weather"]["temperature"]
        wind = weather_response["current_weather"]["windspeed"]

        return f"🌡️ Temp: {temp}°C | 💨 Wind: {wind} km/h"
    except:
        return "⚠️ Could not get weather."