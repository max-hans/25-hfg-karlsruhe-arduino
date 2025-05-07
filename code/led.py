from machine import Pin
from time import sleep

# the onboard led is located at pin 25
led = Pin(25, Pin.OUT)

while True:
    led.value(1)
    sleep(0.3)
    led.value(0)
    sleep(0.3)
