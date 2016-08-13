from uwaterlooapi import UWaterlooAPI, UWaterlooAPIFunction

API_KEY = "500e199350d1bce9904f550fbfe7c721"
uw = UWaterlooAPI(api_key=API_KEY)

print uw.current_weather()
