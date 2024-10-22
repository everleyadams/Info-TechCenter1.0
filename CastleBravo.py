import random
from time import sleep

# Define gas levels with associated messages, delays, and distance ranges (if needed)
gas_levels = {
    "Empty": {"message": "**** WARNING - YOU ARE ON EMPTY ***\nCalling Triple AAA", "sleep": 2, "distance_range": None},
    "Low": {"message": "Your gas tank is extremely low, checking GPS for the closest gas station.", "sleep": 2, "distance_range": (1, 25)},
    "Quarter Tank": {"message": "Your gas tank is on a quarter of a tank, checking GPS for the closest gas station.", "sleep": 2, "distance_range": (25.1, 50)},
    "Half Tank": {"message": "Your gas tank is half full, plenty to get to your destination.", "sleep": 0, "distance_range": None},
    "Three Quarter Tank": {"message": "Your gas tank is three-quarters full.", "sleep": 0, "distance_range": None},
    "Full Tank": {"message": "Your gas tank is full! VROOM!", "sleep": 0, "distance_range": None},
}

# Function to get a random gas level
def gasLevelGauge():
    return random.choice(list(gas_levels.keys()))

# Function to get a random gas station
def gasStations():
    return random.choice(["VP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway"])

# Main function to check gas level and provide alerts
def gasLevelAlert():
    gas_level = gasLevelGauge()
    level_info = gas_levels[gas_level]

    # Print gas level message
    print(level_info["message"])

    # Add delay (if needed)
    if level_info["sleep"] > 0:
        sleep(level_info["sleep"])

    # If the gas level requires a gas station, calculate and display distance
    if level_info["distance_range"]:
        distance = round(random.uniform(*level_info["distance_range"]), 1)
        print(f"The closest gas station is {gasStations()}, which is {distance} miles away.")

# Run the gas level alert
gasLevelAlert()
