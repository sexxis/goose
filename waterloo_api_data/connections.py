from uwaterlooapi import UWaterlooAPI

API_KEY = "500e199350d1bce9904f550fbfe7c721"
uw = UWaterlooAPI(api_key=API_KEY)


def get_temperature():
    weather_values = uw.current_weather().values()
    rain = False
    if weather_values[9] != 0:
        rain = True
    return str(weather_values[4]) + " Degrees Celsius", rain  # Temperature and rain


def get_menu(location):
    menu = uw.menu()
    # Will return the menu at asked Waterloo location
    pass


def get_buildings():
    buildings = uw.building_list()
    for i in range(len(buildings)):
        return buildings[i]["building_name"] + ",",
