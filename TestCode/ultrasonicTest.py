import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

left_trig = 2
left_echo = 3

right_trig = 23
right_echo = 24

GPIO.setup(left_trig, GPIO.OUT)
GPIO.setup(right_trig, GPIO.OUT)

GPIO.setup(left_echo, GPIO.IN)
GPIO.setup(right_echo, GPIO.IN)


def dist(trig, echo):
    try:
        GPIO.output(trig, False)
        time.sleep(0.5)
        GPIO.output(trig, True)
        time.sleep(0.0001)
        GPIO.output(trig,False)


        while GPIO.input(echo)==0:
            pulse_start = time.time()

        while GPIO.input(echo)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        distance = round(distance, 2)

        if (trig == left_trig):
            print("Left distance: ", distance, " cm")
        else :
            print("Right distance: ", distance, " cm")

    except KeyboardInterrupt:
        GPIO.cleanup()

while True:
#        print("left distance")
        dist(left_trig, left_echo)
#       print("right distance")
        dist(right_trig, right_echo)
