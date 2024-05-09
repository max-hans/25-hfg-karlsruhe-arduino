import time
from library import Servo

sg90_servo = Servo(pin=28)  #To be changed according to the pin used

while True:
    print(0)
    sg90_servo.move(0)  # turns the servo to 0°.
    time.sleep(0.5)
    print(1)
    sg90_servo.move(90)  # turns the servo to 90°.
    time.sleep(0.5)
