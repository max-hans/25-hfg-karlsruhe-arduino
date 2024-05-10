from machine import ADC, Pin
from time import sleep

# Set up the analog input pin connected to GP28
analog_pin = Pin(28, Pin.IN)
# Create an ADC object to read analog values
adc = ADC(analog_pin)

while True:
    # Read the current analog value from the sensor
    analog_value = adc.read_u16()
    
    # Print the analog value to the command line
    print("Sensor Value:", analog_value)
    # Wait for 0.3 seconds before the next reading
    sleep(0.3)