# Import the time module to add delays in the code
import time

# Import the Servo class from the library module
from library import Servo

# Create an instance of the Servo class, specifying the pin number connected to the servo motor
servo1 = Servo(pin=28)  # To be changed according to the pin used

# Start an infinite loop
while True:
    # Print the value 0 to the console
    print(0)
    
    # Move the servo motor to the 0° position
    servo1.move(0)
    
    # Wait for 0.5 seconds (500 milliseconds)
    time.sleep(0.5)
    
    # Print the value 1 to the console
    print(1)
    
    # Move the servo motor to the 90° position
    servo1.move(90)
    
    # Wait for 0.5 seconds (500 milliseconds)
    time.sleep(0.5)