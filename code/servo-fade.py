import time
from library import Servo

# Create a Servo object and specify the pin number connected to the servo
sg90_servo = Servo(pin=28)  # Change the pin number according to your setup

while True:
    print("Fading from 0 to 90 degrees")
    # Loop from 0 to 90 degrees in steps of 5
    for angle in range(0, 91, 5):
        # Move the servo to the specified angle
        sg90_servo.move(angle)
        # Wait for a short duration to control the fading speed
        time.sleep(0.01)  # Adjust the delay to control the fading speed

    # Wait for 0.5 seconds before starting the next fading sequence
    time.sleep(0.5)

    print("Fading from 90 to 0 degrees")
    # Loop from 90 to 0 degrees in steps of 5
    for angle in range(90, -1, -5):
        # Move the servo to the specified angle
        sg90_servo.move(angle)
        # Wait for a short duration to control the fading speed
        time.sleep(0.01)  # Adjust the delay to control the fading speed

    # Wait for 0.5 seconds before starting the next fading sequence
    time.sleep(0.5)