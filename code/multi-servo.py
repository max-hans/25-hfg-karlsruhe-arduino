# Import the time module to add delays in the code
import time
# Import the Servo class from the library module
from library import Servo

# Create an instance of the Servo class for the first servo, specifying the pin number
servo1 = Servo(pin=28)  #To be changed according to the pin used
# Create an instance of the Servo class for the second servo, specifying the pin number
servo2 = Servo(pin=27)  #To be changed according to the pin used

# Start an infinite loop
while True:
    # Print the value 0 to the console
    print(0)
    # Move the first servo to the 0° position
    servo1.move(0)  # turns the servo to 0°.
    # Move the second servo to the 0° position
    servo2.move(0)  # turns the servo to 0°.
    # Wait for 0.5 seconds (500 milliseconds)
    time.sleep(0.5)
    # Print the value 1 to the console
    print(1)
    # Move the first servo to the 90° position
    servo1.move(90)  # turns the servo to 90°.
    # Move the second servo to the 90° position
    servo2.move(90)  # turns the servo to 90°.
    # Wait for 0.5 seconds (500 milliseconds)
    time.sleep(0.5)