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

vehicleResponceSystem()