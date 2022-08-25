#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped   

def callback(msg):
    global d
    d = msg.pose.pose.position

d = None
ddd = [None]*5
rospy.init_node("read_pose")
sub = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, callback)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    if d is not None:
        print(d)
        print(type(d))
        for i in range(5):
            ddd[i] = d
    rate.sleep() #Sleep at 10Hz
