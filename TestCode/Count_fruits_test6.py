import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from detection_msgs.msg import BoundingBoxes

point_1 = [0.3458243520930942, 0.300026188169096, 0.7118179508158713, 0.7023640116750671]
point_2 = [0.33226260798655033, 0.793989172685527, 0.7101006407629823, 0.7041001917255825]
point_3 = [0.3675446268195606, 1.0522210161642764, 0.6988597872148938, 0.715258692931413]
point_4 = [0.3559700612411263, 1.252957380530777, 0.7234542222897506, 0.6903723547848161]
point_5 = [0.9360162491430987, 1.4042942998545676, -0.7281633426560493, 0.6854036375829712]
point_6 = [0.9225821606404762, 1.2014037770427746, -0.7332120319008505, 0.6800000854969257]
point_7 = [0.885864804891293, 0.8001815056501693, -0.7458937121655593, 0.6660649894356269]
point_8 = [0.8624954249733435, 0.5985026748388733, -0.7503769339072462, 0.6610101792408043]
point_9 = [1.467515392151751, 0.3562987097651186, 0.6816482446039128, 0.7316800329573059]
point_10 = [1.4851977588557084, 0.5892779632001173, 0.6784597963972586, 0.7346375328504462]
point_11 = [1.5290351522300707, 1.0640185250550112, 0.675525157506783, 0.7373369389739239]
point_12 = [1.550165613207711, 1.298339546550991, 0.6763544292067071, 0.7365763274043428]


def odom_callback(msg):
    global pose_position
    global pose_orientation
    pose_position = msg.pose.pose.position
    pose_orientation = msg.pose.pose.orientation

def left_callback(data):
    global left_fruit
    global cnt_n_left
    global cnt_d_left
    global img_left
    img_left = data
    cnt_n_left = 0
    cnt_d_left = 0


def right_callback(data):
    global right_fruit
    global cnt_n_right
    global cnt_d_right
    global img_right
    img_right = data
    cnt_n_right = 0
    cnt_d_right = 0


left_fruit = [[0 for col in range(2)] for row in range(12)]
right_fruit = [[0 for col in range(2)] for row in range(12)]

rospy.init_node("current_position", anonymous=True)

sub_right = rospy.Subscriber("/yolov5/detections_right", BoundingBoxes, right_callback)
sub_left = rospy.Subscriber("/yolov5/detections_left", BoundingBoxes, left_callback)

img_right = None
img_left = None
pose_position = None
pose_orientation = None

rate = rospy.Rate(3.5)
# rospy.init_node("read_pose")
sub = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, odom_callback)

# while not rospy.is_shutdown():
#     if pose_position is not None:
#         pose_position
#         # print(d)
#     rate.sleep()  # Sleep at 10Hz


while not rospy.is_shutdown():
    if (pose_position is not None) and (pose_orientation is not None):
        x = pose_position.x
        y = pose_position.y
        z = pose_orientation.z
        w = pose_orientation.w

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

        if (point_1[0] - 0.05 < x < point_1[0] + 0.05) and (
                point_1[1] - 0.1 < y < point_1[1] + 0.3):

            # left_fruit.append([cnt_d_left, cnt_d_left])
            # right_fruit.append([cnt_d_right, cnt_d_right])
            left_fruit[0][0] = cnt_n_left
            left_fruit[0][1] = cnt_d_left
            right_fruit[0][0] = cnt_n_right
            right_fruit[0][1] = cnt_d_right

        if (point_2[0] - 0.05 < x < point_2[0] + 0.05) and (
                point_2[1] - 0.1 < y < point_2[1] + 0.3):

            left_fruit[1][0] = cnt_n_left
            left_fruit[1][1] = cnt_d_left
            right_fruit[1][0] = cnt_n_right
            right_fruit[1][1] = cnt_d_right

    print("left_fruit: ", left_fruit)
    print("right_fruit: ", right_fruit)

    rate.sleep()
print("left_fruit: ", left_fruit)
print("right_fruit: ", right_fruit)
#
# print(cnt_n_right)
