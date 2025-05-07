from machine import Pin
from time import sleep

sensor = Pin(16,Pin.IN)

while True:
    value = sensor.value()
    print(value)
    
    if(value is True):
        print("move!")
    else:
        sleep(0.1)



