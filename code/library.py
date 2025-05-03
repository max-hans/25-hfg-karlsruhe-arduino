from machine import Pin, time_pulse_us, PWM, const
from utime import sleep_us, ticks_ms, ticks_diff

class Servo:
    _SERVO_PWM_FREQ = 50
    _MIN_U16_DUTY = 1638
    _MAX_U16_DUTY = 7864
    
    def __init__(self, pin, min_angle=0, max_angle=180):
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.current_angle = -0.001
        self.__initialise(pin)

    def update_settings(self, servo_pwm_freq, min_u16_duty, max_u16_duty, min_angle, max_angle, pin):
        self._SERVO_PWM_FREQ = servo_pwm_freq
        self._MIN_U16_DUTY = min_u16_duty
        self._MAX_U16_DUTY = max_u16_duty
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.__initialise(pin)

    def move(self, angle):
        if angle < self.min_angle or angle > self.max_angle:
            raise ValueError(f"Angle must be between {self.min_angle} and {self.max_angle}")
            
        angle = round(angle, 2)
        
        if angle == self.current_angle:
            return
            
        self.current_angle = angle
        duty_u16 = self.__angle_to_u16_duty(angle)
        self.__motor.duty_u16(duty_u16)

    def __angle_to_u16_duty(self, angle):
        return int((angle - self.min_angle) * self.__angle_conversion_factor) + self._MIN_U16_DUTY

    def __initialise(self, pin):
        self.current_angle = -0.001
        self.__angle_conversion_factor = (self._MAX_U16_DUTY - self._MIN_U16_DUTY) / (self.max_angle - self.min_angle)
        self.__motor = PWM(Pin(pin))
        self.__motor.freq(self._SERVO_PWM_FREQ)


class HCSR04:
    MAX_RANGE_IN_CM = const(500)
    
    def __init__(self, trigger_pin, echo_pin, echo_timeout_us=30000):
        self.echo_timeout_us = echo_timeout_us
        self.trigger = Pin(trigger_pin, mode=Pin.OUT, pull=None)
        self.trigger.value(0)
        self.echo = Pin(echo_pin, mode=Pin.IN, pull=None)

    def _send_pulse_and_wait(self):
        self.trigger.value(0)
        sleep_us(5)
        self.trigger.value(1)
        sleep_us(10)
        self.trigger.value(0)
        
        try:
            pulse_time = time_pulse_us(self.echo, 1, self.echo_timeout_us)
            
            if pulse_time < 0:
                raise OSError('Out of range')
                
            return pulse_time
            
        except OSError as ex:
            if ex.args[0] == 110:
                raise OSError('Out of range')
            raise ex

    def distance_mm(self):
        pulse_time = self._send_pulse_and_wait()
        mm = pulse_time * 100 // 582
        return mm

    def distance_cm(self):
        pulse_time = self._send_pulse_and_wait()
        cms = (pulse_time / 2) / 29.1
        return cms


class HCSR04Async:
    MAX_RANGE_IN_CM = const(500)
    
    def __init__(self, trigger_pin, echo_pin, echo_timeout_us=30000):
        self.echo_timeout_us = echo_timeout_us
        self.trigger = Pin(trigger_pin, mode=Pin.OUT, pull=None)
        self.trigger.value(0)
        self.echo = Pin(echo_pin, mode=Pin.IN, pull=None)
        self.pulse_sent = False
        self.measurement_start_time = 0
        self.pulse_time = -1
        self.measurement_in_progress = False
        
    def start_measurement(self):
        """Start the measurement process."""
        if not self.measurement_in_progress:
            self.trigger.value(0)
            sleep_us(5)
            self.trigger.value(1)
            sleep_us(10)
            self.trigger.value(0)
            self.measurement_start_time = time.ticks_us()
            self.pulse_sent = True
            self.measurement_in_progress = True
            
    def check(self):
        """
        Check if measurement is complete.
        Returns distance in cm if complete, -1 otherwise.
        """
        # If no measurement is in progress, start one
        if not self.measurement_in_progress:
            self.start_measurement()
            return -1
            
        # If we've sent the pulse but haven't detected echo yet
        if self.pulse_sent:
            # Check if echo pin is high
            if self.echo.value() == 1:
                # Echo started, record the time
                self.pulse_start_time = time.ticks_us()
                self.pulse_sent = False
                return -1
                
        # If we're waiting for echo to end
        elif self.echo.value() == 0:
            # Echo ended, calculate pulse time
            pulse_end_time = time.ticks_us()
            self.pulse_time = time.ticks_diff(pulse_end_time, self.pulse_start_time)
            
            # Check for timeout
            if time.ticks_diff(pulse_end_time, self.measurement_start_time) > self.echo_timeout_us:
                # Timeout occurred, reset and return error
                self.reset_measurement()
                return -1
                
            # Valid measurement completed
            cms = (self.pulse_time / 2) / 29.1
            self.reset_measurement()
            return cms
            
        # Check for timeout even if echo is still high
        if time.ticks_diff(time.ticks_us(), self.measurement_start_time) > self.echo_timeout_us:
            self.reset_measurement()
            return -1
            
        return -1
        
    def reset_measurement(self):
        """Reset the measurement state."""
        self.pulse_sent = False
        self.measurement_in_progress = False
        self.pulse_time = -1
        
    def distance_cm(self):
        """
        Start a measurement and wait for completion.
        This blocks until measurement is complete (not async).
        Included for backwards compatibility.
        """
        self.start_measurement()
        result = -1
        while result == -1:
            result = self.check()
        return result
        
    def distance_mm(self):
        """
        Get distance in mm (blocking call).
        Included for backwards compatibility.
        """
        cm = self.distance_cm()
        return cm * 10
    

class Blinky:
    def __init__(self, pin):
        if isinstance(pin, int):
            self.pin = Pin(pin, Pin.OUT)
        else:
            self.pin = pin
            self.pin.init(Pin.OUT)
            
        self.interval = 0
        self.last_update = 0
        self.state = False
        self.running = False

    def start(self, interval):
        self.interval = interval
        self.last_update = ticks_ms()
        self.state = False
        self.pin.value(self.state)
        self.running = True

    def stop(self):
        self.running = False
        self.pin.value(False)

    def change_frequency(self, new_interval):
        self.interval = new_interval

    def update(self):
        if self.running:
            current_time = ticks_ms()
            if ticks_diff(current_time, self.last_update) >= self.interval:
                self.state = not self.state
                self.pin.value(self.state)
                self.last_update = current_time