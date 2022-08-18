import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

left_trig = 2
left_echo = 3

right_trig = 23
right_echo = 24

GPIO.setup(left_trig, GPIO.OUT)
GPIO.setup(left_echo, GPIO.IN)

GPIO.setup(right_trig, GPIO.OUT)
GPIO.setup(right_echo, GPIO.IN)

try:
    while True:
        GPIO.output(left_trig, False)
        time.sleep(0.5)

        GPIO.output(right_trig, False)
        time.sleep(0.5)

        GPIO.output(left_trig, True)
        time.sleep(0.0001)
        GPIO.output(left_trig, False)

        GPIO.output(right_trig, True)
        time.sleep(0.0001)
        GPIO.output(right_trig, False)

        while GPIO.input(left_echo)==0:
            le_pulse_start = time.time()

        while GPIO.input(left_echo)==1:
            le_pulse_end = time.time()
        
        while GPIO.input(right_echo)==0:
            ri_pulse_start = time.time()

        while GPIO.input(right_echo)==1:
            ri_pulse_end = time.time()
        
        le_pulse_duration = le_pulse_end - le_pulse_start
        ri_pulse_duration = ri_pulse_end - ri_pulse_start
        le_distance = le_pulse_duration * 17000
        ri_distance = ri_pulse_duration * 17000
        le_distance = round(le_distance,2)
        ri_distance = round(ri_distance,2)

        print("LEFT distance : ", le_distance, "cm  ", "RIGHT distance : ", ri_distance, "cm ")

except KeyboardInterrupt:
    GPIO.cleanup()
