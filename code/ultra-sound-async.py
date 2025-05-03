# Import the HCSR04 class from the library module
from library import HCSR04Async
# Import the sleep function from the time module
from time import sleep_ms

# Create an instance of the HCSR04 sensor
# trigger_pin is connected to GPIO16 (physical pin 36)
# echo_pin is connected to GPIO0 (physical pin 11)
sensor = HCSR04(trigger_pin=16, echo_pin=0)

# Start an infinite loop
while True:
    distance = sensor.check()
    if distance != -1:
        print(f"Distance: {distance} cm")
    # Do other tasks here
    sleep_ms(10)  