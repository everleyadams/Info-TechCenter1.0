# Print a separator and label to indicate the start of the program
print("\n***************************************************\n")
print("Gasoline Branch\n")

# Import necessary modules
import random  # Used to generate random choices and values
from time import sleep  # Used to pause the program for a brief moment


# Function to randomly determine the gas level in the vehicle
def gasLevelGauge():
    # List of possible gas levels in the vehicle
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    # Randomly select and return one gas level from the list
    return random.choice(gasLevelList)


# Function to randomly select a nearby gas station
def gasStations():
    # List of possible gas stations
    gasStationsList = ["VP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway"]
    # Randomly select and return one gas station from the list
    return random.choice(gasStationsList)


# Function to display a gas level alert based on the current gas level
def gasLevelAlert():
    # Generate random distances to the closest gas stations
    # If the gas level is low, a gas station between 1 and 25 miles away is selected
    milesToGasStationLow = round(random.uniform(1, 25), 1)
    # If the gas level is at a quarter tank, a gas station between 25.1 and 50 miles away is selected
    milesToGasStationQuarterTank = round(random.uniform(25.1, 50), 1)

    # Get the current gas level by calling the gasLevelGauge function
    gasLevelIndicator = gasLevelGauge()

    # Condition to check if the gas tank is empty
    if gasLevelIndicator == "Empty":
        print("**** WARNING - YOU ARE ON EMPTY***\n")
        sleep(2)  # Pause for 2 seconds to simulate real-time response
        print("Calling Triple AAA")  # Alert the user to call roadside assistance

    # Condition for low gas level
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking GPS for the closest gas station")
        sleep(2)
        print("The closest gas station is", gasStations(), "which is", milesToGasStationLow, "miles away.")

    # Condition for a quarter tank of gas
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter of a tank, checking GPS for the closest gas station")
        sleep(2)
        print("The closest gas station is", gasStations(), "which is", milesToGasStationQuarterTank, "miles away.")

    # Condition for half tank of gas
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is half a tank full which is plenty to get to your destination.")

    # Condition for three-quarter tank of gas
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is three quarter tanks full.")

    # Condition for a full tank of gas
    else:
        print("Your gas tank is full!!! VROOM")


# Call the function to display the gas level alert based on a random gas level
gasLevelAlert()
