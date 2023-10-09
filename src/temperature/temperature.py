import os
import requests
from dotenv import load_dotenv


def get_city_temperature(city_name: str):
    load_dotenv()
    api_key = os.getenv("API_KEY")
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    response_json = response.json()

    if response_json["cod"] != "404":
        data = response_json["main"]
        temperature = data["temp"]
        return temperature
    else:
        return None
