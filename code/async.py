from machine import Pin, Timer
from utime import sleep_us

class HCSR04:
    """
    Driver to use the ultrasonic sensor HC-SR04 asynchronously.
    The sensor range is between 2cm and 4m.

    The timeouts received listening to echo pin are converted to OSError('Out of range')
    """
    # echo_timeout_us is based in chip range limit (400cm)
    def __init__(self, trigger_pin, echo_pin, echo_timeout_us=500*2*30):
        """
        trigger_pin: Output pin to send pulses
        echo_pin: Readonly pin to measure the distance. The pin should be protected with 1k resistor
        echo_timeout_us: Timeout in microseconds to listen to echo pin.
        By default is based in sensor limit range (4m)
        """
        self.echo_timeout_us = echo_timeout_us
        self.pulse_start = 0
        self.pulse_end = 0
        self.distance = -1

        # Init trigger pin (out)
        self.trigger = Pin(trigger_pin, mode=Pin.OUT, pull=None)
        self.trigger.value(0)

        # Init echo pin (in)
        self.echo = Pin(echo_pin, mode=Pin.IN, pull=None)

        # Setup interrupt handler
        self.echo.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self.handle_interrupt)

        # Setup timer for timeout
        self.timer = Timer(-1)

    def handle_interrupt(self, pin):
        print(pin.value())
        if pin.value() == 1:
            # Rising edge detected
            self.pulse_start = Timer.counter()
        else:
            # Falling edge detected
            self.pulse_end = Timer.counter()
            self.timer.deinit()
            self.calculate_distance()

    def calculate_distance(self):
        pulse_duration = self.pulse_end - self.pulse_start
        self.distance = pulse_duration * 100 // 582  # Calculate distance in mm

    def timeout(self, t):
        self.timer.deinit()
        self.distance = -1  # Set distance to -1 to indicate timeout

    def measure(self):
        self.distance = -1
        self.trigger.value(0)  # Stabilize the sensor
        sleep_us(5)
        self.trigger.value(1)
        # Send a 10us pulse
        sleep_us(10)
        self.trigger.value(0)
        # Start timeout timer
        self.timer.init(mode=Timer.ONE_SHOT, period=self.echo_timeout_us, callback=self.timeout)

    def update(self):
        if self.distance != -1:
            # Measurement completed
            distance = self.distance
            self.distance = -1
            return distance
        else:
            # Measurement not completed yet
            return -1
        
hc = HCSR04(28,27)
hc.measure()
while True:
    val = hc.update()
#     print(val)
    if(val != -1):
        print("dist")
        print(val)
        hc.measure()