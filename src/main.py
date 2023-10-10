from temperature.temperature_utils import set_temperature_unit, get_city_temperature
from uagents import Agent, Context
from sys import exit

if __name__ == "__main__":
    print("Welcome abroad ! We are pleased to welcome you to our temperature alert agent")
    city_name = input("Enter city name : ")
    temperature_unit = set_temperature_unit()
    temperature_min = int(input("Enter minimum temperature "))
    temperature_max = int(input("Enter maximum temperature "))

    # Check if minimum temperature is greater than maximum temperature
    if temperature_min >= temperature_max:
        print("ERROR : Minimum temperature cannot be greater than or equal to maximum temperature")
        exit()

    temperature_alert_agent = Agent(name="temperature_alert_agent")

    # Periodically checks if the temperature exceeded the threshold and notify the user
    @temperature_alert_agent.on_interval(period=3.0)
    async def check_temperature_range(ctx: Context):
        # Collects the current temperature of given city
        city_temperature = get_city_temperature(city_name, temperature_unit)
        # Check if given temperature exceeds threshold
        if city_temperature is not None:
            if city_temperature > temperature_max:
                ctx.logger.info(
                    f"The Temperature of {city_name} is {city_temperature} which is more than {temperature_max}")
            elif city_temperature < temperature_min:
                ctx.logger.info(
                    f"The Temperature of {city_name} is {city_temperature} which is less than {temperature_min}")
            else:
                pass
        else:
            ctx.logger.info("ERROR : City Temperature cannot be found")


    temperature_alert_agent.run()
