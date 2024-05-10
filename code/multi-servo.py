import time
from library import Servo

servo1 = Servo(pin=28)  #To be changed according to the pin used
servo2 = Servo(pin=27)  #To be changed according to the pin used

while True:
    print(0)
    servo1.move(0)  # turns the servo to 0°.
    servo2.move(0)  # turns the servo to 0°.
    time.sleep(0.5)
    print(1)
    servo1.move(90)  # turns the servo to 90°.
    servo2.move(90)  # turns the servo to 90°.
    time.sleep(0.5)
