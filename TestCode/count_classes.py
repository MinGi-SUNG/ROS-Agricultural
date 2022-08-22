import rospy
from detection_msgs.msg import BoundingBoxes


def callback(dat):
    cnt = 0
    for each in data.bounding_boxes:
        if each.Class == "normal fruit":
            cnt = cnt + 1
    print("normal count :" + str(cnt))


rospy.init_node("/yolov5/detections", anonymous=False)
rospy.loginfo("--> Start count")

rospy.Subscriber("detected_object", BoundingBoxes, callback)

rospy.spin()

