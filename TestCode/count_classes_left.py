import rospy
from detection_msgs.msg import BoundingBoxes


def callback(data):
    cnt = 0
    for each in data.bounding_boxes:
        if each.Class == "normal fruit":
            cnt = cnt + 1
    print("normal count :" + str(cnt))


rospy.init_node("count_classes", anonymous=True)
rospy.loginfo("--> Start count")

rospy.Subscriber("/yolov5/detections_left", BoundingBoxes, callback)

rospy.spin()
