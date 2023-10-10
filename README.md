# Temperature-Alert-Agent
A Temperature Alert Agent implement in Python with fetch.ai's uAgents library and OpenWeatherMap API, with the goal to be submitted in IIT Bombay Techfest's HackAI competition.  

## Project Description
The program takes a city, a unit for measurement of temperature and a range. A notification is sent as soon as the threshold is broken.  

## Installation Instruction
Here are the steps to get up and running with the project.
1. Clone the project repo or download the source code.
2. Creat a OpenWeatherMap API Account and copy the API Key
3. In the root directory create a `.env` file copying the format shown in `.env.example`
4. Install Poetry if not already install
5. In the project repo run
```
poetry install
```
6. Then run
```
poetry shell
```
to activate the virtual env
7. Navigate to `src` directory and run
```
poetry run python main.py
```

The project must be up and running now! Enjoy the Experience!! 