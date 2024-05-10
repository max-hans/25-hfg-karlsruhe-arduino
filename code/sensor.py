from machine import ADC, Pin
from time import sleep

# Set up the analog input pin
analog_pin = Pin(28, Pin.IN)
adc = ADC(analog_pin)

while True:
    # Read the analog value
    analog_value = adc.read_u16()
    
    # Print the value to the command line
    print("Sensor Value:", analog_value)
    sleep(0.3)