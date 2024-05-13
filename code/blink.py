from machine import Pin
from library import Blinky

led = Pin(16, Pin.OUT)
blinky = Blinky(led)
blinky.start(100)

a = 0

while a < 30000:
    blinky.update()
    a = a + 1

print("done!")

