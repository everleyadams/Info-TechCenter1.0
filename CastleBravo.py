print("\n*********************************\n")  # Print a decorative separator

print("Welcome Branch")

print("Weather Branch\n")  # Print the section title

# Import Libraries Here
import random  # Import random module for choosing weather conditions
from time import sleep  # Import sleep to pause the program


# Function to randomly select a weather condition
def weather():
    weatherForcast = ["snowy", "blizzard", "raining", "windy", "icy", "sunny"]
    return random.choice(weatherForcast)


weatherAlert = weather()

# Define a dictionary to map weather conditions to delay time and speed limits
weather_responses = {
    "snowy": {"delay": 30, "speed_limit": 55},
    "blizzard": {"delay": 45, "speed_limit": 45},
    "raining": {"delay": 15, "speed_limit": 65},
    "windy": {"delay": 5, "speed_limit": 70},
    "icy": {"delay": 50, "speed_limit": 30},
}


# Function to handle vehicle response system based on weather conditions
def vehicleResponseSystem():
    if weatherAlert in weather_responses:
        response = weather_responses[weatherAlert]  # Get the delay and speed limit for the current weather
        print(f"\nThe National Weather Service has Updated our alarm by {response['delay']} minutes because"
              f" of the forecast of {weatherAlert} weather conditions.")
        sleep(1)  # Pause for 1 second
        print(f"VRS system has been engaged only allowing you to drive {response['speed_limit']}mph.")

        # Adjust speed to 45mph if weather condition is either "raining" or "windy"
        if weatherAlert in ["raining", "windy"]:
            sleep(1)
            print("VRS system has been further engaged only allowing you to drive 45mph.")
    else:
        # Handle case for "sunny" or any other weather condition not in the dictionary
        print(f"\nThe NWS is calling for {weatherAlert} skies, drive carefully to get to your destination!")
        sleep(1)
        print("VRS system has been disengaged.")


# Call the vehicle response system to output the response based on the current weather
vehicleResponseSystem()
