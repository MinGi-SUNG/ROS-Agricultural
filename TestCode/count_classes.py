import rospy
from detection_msgs.msg import BoundingBox

def callback(dat):
	cnt = 0
	for each in data.bounding_boxes:
		if each.Class == "normal fruit":
			cnt=cnt+1
	print "normal count :" + str(cnt)

rospy.init_node("count_classes",anonymous=False)
rospy.loginfo("--> Start count)

rospy.Subscriber("detectedd_object",BoundingBox,callback)

rospy.spin() 
