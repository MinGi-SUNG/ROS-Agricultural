import rospy
# import odeme
from detection_msgs.msg import BoundingBoxes

def left_callback(data):
    global left_fruit
    global cnt_n_left
    global cnt_d_left
    global img_left
    img_left = data
    cnt_n_left = 0
    cnt_d_left = 0

    # count_fruits 노드 종료 코드 추가
    
def right_callback(data):
    global right_fruit
    global cnt_n_right
    global cnt_d_right
    global img_right
    img_right = data
    cnt_n_right = 0
    cnt_d_right = 0
    # count_fruits 노드 종료 코드 추가

left_fruit = [[0 for col in range(2)] for row in range(12)]
right_fruit = [[0 for col in range(2)] for row in range(12)]

rospy.init_node("current_position", anonymous=True)

sub_right = rospy.Subscriber("/yolov5/detections_right", BoundingBoxes, right_callback)
sub_left = rospy.Subscriber("/yolov5/detections_left", BoundingBoxes, left_callback)

img_right = None
img_left = None
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    if img_left is not None:
        for each in img_left.bounding_boxes:
            if each.Class == "normal fruit":
                cnt_n_left = cnt_n_left + 1

            elif each.Class == "disease fruit":
                cnt_d_left = cnt_d_left + 1

    if img_right is not None:
        for each in img_right.bounding_boxes:
            if each.Class == "normal fruit":
                cnt_n_right = cnt_n_right + 1

            elif each.Class == "disease fruit":
                cnt_d_right = cnt_d_right + 1

        left_fruit[0][0] = cnt_n_left
        left_fruit[0][1] = cnt_d_left

        right_fruit[0][0] = cnt_n_right
        right_fruit[0][1] = cnt_d_right

        # print(right_fruit)
    rate.sleep()
print("left_fruit: ", left_fruit)
print("right_fruit: ", right_fruit)
#
# print(cnt_n_right)
