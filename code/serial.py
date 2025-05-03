from machine import Pin
from time import sleep
pins = [Pin(16,Pin.IN), Pin(17,Pin.IN), Pin(18,Pin.IN), Pin(19,Pin.IN)]

while True:
    counter = 0
    for pin in pins:
        print(counter,pin.value())
        counter = counter + 1
    sleep(0.1)