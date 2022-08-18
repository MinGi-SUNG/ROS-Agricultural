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
        rospy.init_node('sonar_right', anonymous=True)
        self.distance_publisher = rospy.Publisher('/sonar_dist_right', Float32, queue_size=1)
        self.r = rospy.Rate(15)

    def dist_sendor(self, dist):
        data = Float32()
        data.data = dist
        self.distance_publisher.publish(data)


# left_sensor=sonar()
# right_sensor=sonar()

GPIO.setmode(GPIO.BCM)

trig = 23
echo = 24

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

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

        sensor = sonar()

        print("Right distance: ", distance, " cm")
        sensor.dist_sendor(distance)

    except KeyboardInterrupt:
        GPIO.cleanup()


while True:
    #        print("left distance")

    dist(trig, echo)