print("\n*********************************\n")  # Prints a decorative separator line
print("Weather Branch\n")  # Prints the section title "Weather Branch"

# Import Libraries Here
import random  # Import the random module to randomly choose weather conditions
from time import sleep  # Import the sleep function to pause the program for a specified time

# Function to randomly select a weather condition
def weather():
    weatherForcast = ["snowy", "blizzard", "raining", "windy", "icy", "sunny"]  # List of possible weather conditions
    weatherCondition = random.choice(weatherForcast)  # Randomly select a weather condition from the list
    return weatherCondition  # Return the randomly selected condition

# Assign the result of the weather function to the variable weatherAlert
weatherAlert = weather()

# Function that adjusts vehicle response based on the weather condition
def vehicleResponceSystem():
    # Check for each specific weather condition and respond accordingly
    if weatherAlert == "snowy":
        print("\nThe National Weather Service has Updated our alarm by 30 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")  # Alert for snowy weather
        sleep(1)  # Pause for 1 second
        print("VRS system has been engaged only allowing you to drive 55mph.")  # Limit speed to 55mph
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has Updated our alarm by 45 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")  # Alert for blizzard weather
        sleep(1)  # Pause for 1 second
        print("VRS system has been engaged only allowing you to drive 45mph.")  # Limit speed to 45mph
    elif weatherAlert == "raining":
        print("\nThe National Weather Service has Updated our alarm by 15 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")  # Alert for rainy weather
        sleep(1)  # Pause for 1 second
        print("VRS system has been engaged only allowing you to drive 65mph.")  # Limit speed to 65mph
        sleep(1)  # Pause for 1 second
        print("VRS system has been engaged only allowing you to drive 45mph.")  # Further limit speed to 45mph
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has Updated our alarm by 5 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")  # Alert for windy weather
        sleep(1)  # Pause for 1 second
        print("VRS system has been engaged only allowing you to drive 70mph.")  # Limit speed to 70mph
        sleep(1)  # Pause for 1 second
        print("VRS system has been engaged only allowing you to drive 45mph.")  # Further limit speed to 45mph
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has Updated our alarm by 50 minutes because"
              " of the forecast of", weatherAlert, "weather conditions.")  # Alert for icy weather
        sleep(1)  # Pause for 1 second
        print("VRS system has been engaged only allowing you to drive 30mph.")  # Limit speed to 30mph
    else:  # If the weather is sunny or any other condition
        print("The NWS is calling for", weatherAlert, "skies, drive carefully to get to your destination!")  # Sunny weather or other
        sleep(1)  # Pause for 1 second
        print("VRS system has been disengaged")  # No speed limit imposed

# Call the vehicleResponceSystem function to execute the response based on the current weather
vehicleResponceSystem()
