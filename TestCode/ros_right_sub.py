# ! /usr/bin/env python3

import rospy
from std_msgs.msg import Float32

right_dist = None


def right_callback(data):
    global right_dist
    right_dist = data.data
    print(right_dist)


def right_dist_logger_node():
    rospy.init_node('sonar_right_logger', anonymous=True)

    rospy.Subscriber('/sonar_dist_right', Float32, right_callback)

    rospy.spin()


if __name__ == '__main__':
    right_dist_logger_node()
