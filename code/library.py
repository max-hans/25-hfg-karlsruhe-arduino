from machine import Pin, time_pulse_us, PWM
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
