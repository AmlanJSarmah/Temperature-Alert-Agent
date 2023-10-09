from temperature.temperature import get_city_temperature

if __name__ == "__main__":
    city_name = input("Enter city name : ")
    city_temperature = get_city_temperature(city_name)
    if city_temperature is not None:
        print(f"The Temperature of {city_name} is {city_temperature}")
    else:
        print("ERROR : City Temperature cannot be found")
