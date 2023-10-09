import os
import requests
from dotenv import load_dotenv


def kelvin_to_celsius(temperature):
    return temperature - 273.15


def kelvin_to_fahrenheit(temperature):
    return (temperature - 273.15) * 1.8 + 32


def get_city_temperature(city_name, temperature_unit):
    load_dotenv()
    api_key = os.getenv("API_KEY")
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    response_json = response.json()

    if response_json["cod"] != "404":
        data = response_json["main"]
        temperature = data["temp"]
        if temperature_unit == "C":
            temperature = kelvin_to_celsius(temperature)
        if temperature_unit == "F":
            temperature = kelvin_to_fahrenheit(temperature)
        return temperature
    else:
        return None


def set_temperature_unit():
    unit = input("Enter C for Celsius, F for Fahrenheit and K for Kelvin. If you enter anything else we will put "
                 "Celsius as default ")
    if unit == "C":
        return "C"
    elif unit == "F":
        return "F"
    elif unit == "K":
        return "K"
    else:
        return "C"
