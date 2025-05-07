from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)
sensor = Pin(15,Pin.IN)

while True:
    
    value = sensor.value()
    print(value)
    
    if(value):    
        led.value(1)
    else:
        led.value(0)

sleep(0.1)

