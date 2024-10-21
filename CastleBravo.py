# Color definitions for console output
RESET = "\033[0m"  # Resets the text color to default
RED = "\033[31m"  # Red color
GREEN = "\033[32m"  # Green color
YELLOW = "\033[33m"  # Yellow color
CYAN = "\033[36m"  # Cyan color

import sys  # Importing system-specific parameters and functions
import time  # Importing time module to control the program's pace

# Displaying a colorful welcome message at the start of the program
print(CYAN + "\n\tWelcome to InfoTechCenter V1.0\n" + RESET)

timeToSleep = 2 #variable to set the time library to 2 seconds when called
time.sleep(timeToSleep)  # Calling the time to sleep library with the variable timeToSleeps value
x = 0  # Counter to track the number of iterations
ellipsis = 0  # Counter to track the number of ellipsis dots displayed

# Loop to simulate the system booting process
while x != 20:
    x += 1  # Incrementing the counter to avoid an infinite loop

    # Creating a message that displays the system booting process with an increasing number of dots
    message = (GREEN + "InfoTech Center System Booting" + "." * ellipsis + RESET)
    ellipsis += 1  # Incrementing the ellipsis count to increase the dots after each iteration

    # Overwriting the current line in the console to update the booting message
    sys.stdout.write("\r" + message)
    # Pausing for 0.5 seconds between each update to simulate a delay
    time.sleep(.75)

    # Resetting the ellipsis count to 0 after reaching 3 dots (creating a loop effect)
    if ellipsis == 4:
        ellipsis = 0

    # Once the loop reaches 20 iterations, print the final message
    if x == 20:
        print(
            "\n\n" + GREEN + "Operating System Booted Up " + RED + "- Retina Scanned - " + CYAN + "Access Granted" + RESET)


print("\n*********************************\n")  # Print a decorative separator


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

