print("\n*********************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

def weather():
    weatherForcast = ["snowy", "blizzard", "raining", "windy", "icy", "sunny"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition

weatherAlert = weather()

def vehicleResponceSystem():
    if weatherAlert == "snowy":
        print("\nThe National Weather Service has Updated our alarm by 30 minutes because"
              "of the forcast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("VRS system has been engaged only allowing you to drive 55mph.")
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has Updated our alarm by 45 minutes because"
              "of the forcast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("VRS system has been engaged only allowing you to drive 45mph.")
    elif weatherAlert == "raining":
        print("\nThe National Weather Service has Updated our alarm by 15 minutes because"
              "of the forcast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("VRS system has been engaged only allowing you to drive 65mph.")
        sleep(1)
        print("VRS system has been engaged only allowing you to drive 45mph.")
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has Updated our alarm by 5 minutes because"
              "of the forcast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("VRS system has been engaged only allowing you to drive 70mph.")
        sleep(1)
        print("VRS system has been engaged only allowing you to drive 45mph.")
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has Updated our alarm by 50 minutes because"
              "of the forcast of", weatherAlert, "weather conditions.")
        sleep(1)
        print("VRS system has been engaged only allowing you to drive 30mph.")
    else:
        print("The NWS is calling for", weatherAlert, "skies, drive carefully to get to your destination!")
        sleep(1)
        print("VRS system has been disengaged")

vehicleResponceSystem()