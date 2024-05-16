from math import sin
from utime import ticks_ms, sleep

while True:
    print((sin(ticks_ms()) + 1) / 2)
    sleep(0.1)
    
