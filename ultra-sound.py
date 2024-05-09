from library import HCSR04
from time import sleep

sensor = HCSR04(trigger_pin=16, echo_pin=0)


while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    sleep(0.3)
