from temperature.temperature import get_city_temperature, set_temperature_unit

if __name__ == "__main__":
    print("Welcome abroad ! We are pleased to welcome you to our temperature alert agent")
    city_name = input("Enter city name : ")
    temperature_unit = set_temperature_unit()
    city_temperature = get_city_temperature(city_name, temperature_unit)
    if city_temperature is not None:
        print(f"The Temperature of {city_name} is {city_temperature}")
    else:
        print("ERROR : City Temperature cannot be found")
