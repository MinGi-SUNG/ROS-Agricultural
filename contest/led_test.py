import RPi.GPIO as GPIO
import rospy
import time
from detection_msgs.msg import BoundingBoxes


def left_callback(data):
    global img_left
    img_left = data.bounding_boxes


def right_callback(data):
    global img_right
    img_right = data.bounding_boxes


red_led = 5
yellow_led = 6
blue_led = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(yellow_led, GPIO.OUT)
GPIO.setup(blue_led, GPIO.OUT)

img_left = None
img_right = None

rospy.init_node('image_class')
rospy.Subscriber("/yolov5/detections_right", BoundingBoxes, right_callback)
rospy.Subscriber("/yolov5/detections_left", BoundingBoxes, left_callback)

rate = rospy.Rate(10)

while not rospy.is_shutdown():
    if img_left is not None:
        for each in img_left:
            if each.Class == "normal fruit":
                GPIO.output(red_led, 1)
                print("red led is on")
                time.sleep(0.5)
                GPIO.output(red_led, 0)
                print("red led is off")

        for each in img_left:
            if each.Class == "disease fruit":
                GPIO.output(blue_led, 1)
                print("yellow led is on")
                time.sleep(0.5)
                GPIO.output(blue_led, 0)
                print("yellow led is off")

        for each in img_left:
            if each.Class == "obstacle":
                GPIO.output(yellow_led, 1)
                print("yellow led is on")
                time.sleep(0.5)
                GPIO.output(yellow_led, 0)
                print("yellow led is off")

    if img_right is not None:
        for each in img_right:
            if each.Class == "normal fruit":
                GPIO.output(red_led, 1)
                print("red led is on")
                time.sleep(0.5)
                GPIO.output(red_led, 0)
                print("red led is off")

        for each in img_right:
            if each.Class == "disease fruit":
                GPIO.output(blue_led, 1)
                print("yellow led is on")
                time.sleep(0.5)
                GPIO.output(blue_led, 0)
                print("yellow led is off")

        for each in img_right:
            if each.Class == "obstacle":
                GPIO.output(yellow_led, 1)
                print("yellow led is on")
                time.sleep(0.5)
                GPIO.output(yellow_led, 0)
                print("yellow led is off")
    rate.sleep()
