# Import the HCSR04 class from the library module
from library import HCSR04
# Import the sleep function from the time module
from time import sleep

# Create an instance of the HCSR04 sensor
# trigger_pin is connected to GPIO16 (physical pin 36)
# echo_pin is connected to GPIO0 (physical pin 11)
sensor = HCSR04(trigger_pin=16, echo_pin=0)

# Start an infinite loop
while True:
    # Measure the distance in centimeters using the sensor
    distance = sensor.distance_cm()
    
    # Print the measured distance
    print('Distance:', distance, 'cm')
    
    # Wait for 0.3 seconds before the next measurement
    sleep(0.3)