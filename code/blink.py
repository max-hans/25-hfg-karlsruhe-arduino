from machine import Pin
from library import Blinky

led = Pin(16, Pin.OUT)
blinky = Blinky(led)
blinky.start(100)



while True:
    blinky.update()