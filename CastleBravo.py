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
    time.sleep(.5)

    # Resetting the ellipsis count to 0 after reaching 3 dots (creating a loop effect)
    if ellipsis == 4:
        ellipsis = 0

    # Once the loop reaches 20 iterations, print the final message
    if x == 20:
        print(
            "\n\n" + GREEN + "Operating System Booted Up " + RED + "- Retina Scanned - " + CYAN + "Access Granted" + RESET)

