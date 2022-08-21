# ! /usr/bin/env python3

import rospy
from std_msgs.msg import Float32

left_dist = None


def left_callback(data):
    global left_dist
    left_dist = data.data
    print(left_dist)


def left_dist_logger_node():
    rospy.init_node('sonar_left_logger', anonymous=True)

    rospy.Subscriber('/sonar_dist_left', Float32, left_callback)

    rospy.spin()


if __name__ == '__main__':
    left_dist_logger_node()
