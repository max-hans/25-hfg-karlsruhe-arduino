import time
from library import Servo

sg90_servo = Servo(pin=28)  # To be changed according to the pin used

while True:
    print("Fading from 0 to 90 degrees")
    for angle in range(0, 91, 5):  # Fade from 0 to 90 degrees in steps of 5
        sg90_servo.move(angle)
        time.sleep(0.01)  # Adjust the delay to control the fading speed

    time.sleep(0.5)

    print("Fading from 90 to 0 degrees")
    for angle in range(90, -1, -5):  # Fade from 90 to 0 degrees in steps of 5
        sg90_servo.move(angle)
        time.sleep(0.01)  # Adjust the delay to control the fading speed

    time.sleep(0.5)

