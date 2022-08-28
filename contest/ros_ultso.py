import RPi.GPIO as GPIO
import time
import sys
import signal
import rospy
from std_msgs.msg import Float32


def signal_handler(signal, frame):  # ctrl + c -> exit program
    print('You pressed Ctrl+C!')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


class sonar():
    def __init__(self):
        rospy.init_node('sonar', anonymous=True)
        self.distance_publisher_left = rospy.Publisher('/sonar_dist_left', Float32, queue_size=1)
        self.distance_publisher_right = rospy.Publisher('/sonar_dist_right', Float32, queue_size=1)
        self.r = rospy.Rate(15)

    def dist_sendor_left(self, dist):
        data = Float32()
        data.data = dist
        self.distance_publisher_left.publish(data)

    def dist_sendor_right(self, dist):
        data = Float32()
        data.data = dist
        self.distance_publisher_right.publish(data)


# left_sensor=sonar()
# right_sensor=sonar()

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
        GPIO.output(trig, False)

        while GPIO.input(echo) == 0:
            pulse_start = time.time()

        while GPIO.input(echo) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        distance = round(distance, 2)

        if trig == left_trig:
            left_sensor = sonar()
            left_distance = distance
            print("Left distance: ", distance, " cm")
            left_sensor.dist_sendor_left(left_distance)
        else:
            right_sensor = sonar()
            right_distance = distance
            print("Right distance: ", distance, " cm")
            right_sensor.dist_sendor_right(right_distance)

    except KeyboardInterrupt:
        GPIO.cleanup()


while True:
    #        print("left distance")
    dist(left_trig, left_echo)
    #       print("right distance")
    dist(right_trig, right_echo)
