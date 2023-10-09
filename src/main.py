import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
base_url = "https://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)
response_json = response.json()

if response_json["cod"] != "404":
    data = response_json["main"]
    temperature = data["temp"]
    # weather = data["weather"][0]["description"]
    print(f"Temperature : {str(temperature)}")
    # print(f"Weather : {str(weather)}")
else:
    print("ERROR : Cannot Find City")
