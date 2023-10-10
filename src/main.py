from temperature.temperature_utils import set_temperature_unit, get_city_temperature
from uagents import Agent, Context

if __name__ == "__main__":
    print("Welcome abroad ! We are pleased to welcome you to our temperature alert agent")
    city_name = input("Enter city name : ")
    temperature_unit = set_temperature_unit()
    temperature_alert_agent = Agent(name="temperature_alert_agent")


    @temperature_alert_agent.on_interval(period=3.0)
    async def check_temperature_range(ctx: Context):
        city_temperature = get_city_temperature(city_name, temperature_unit)
        if city_temperature is not None:
            ctx.logger.info(f"The Temperature of {city_name} is {city_temperature}")
        else:
            ctx.logger.info("ERROR : City Temperature cannot be found")


    temperature_alert_agent.run()
