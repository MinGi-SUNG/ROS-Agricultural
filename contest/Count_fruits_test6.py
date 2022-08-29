import rospy
import string
from geometry_msgs.msg import PoseWithCovarianceStamped
from detection_msgs.msg import BoundingBoxes

point_1 = [0.3458243520930942, 0.300026188169096, 0.7118179508158713, 0.7023640116750671]
point_2 = [0.3458243520930942, 0.793989172685527, 0.7101006407629823, 0.7041001917255825]
point_3 = [0.3458243520930942, 1.0433756843422264, 0.7054060238993953, 0.7088034575581905]
point_4 = [0.3458243520930942, 1.2993974382926154, 0.6967426618160805, 0.7173211715859521]
point_5 = [0.9428930232051557, 1.4042942998545676, -0.7281633426560493, 0.6854036375829712]
point_6 = [0.9428930232051557, 1.1124147573720116, -0.6545859617152052, 0.7559875784200293]
point_7 = [0.9428930232051557, 0.8880914536287361, -0.6571213109779029, 0.753784838437788]
point_8 = [0.9428930232051557, 0.48345834259302795, -0.6578621844792023, 0.7531383314054941]
point_9 = [1.4932274084450738, 0.33622629277772825, 0.6541658939362884, 0.7563510978444711]
point_10 = [1.4932274084450738, 0.8880914536287361, 0.6541658939362884, 0.7563510978444711]
point_11 = [1.4932274084450738, 1.1124147573720116, 0.6541658939362884, 0.7563510978444711]
point_12 = [1.4932274084450738, 1.4042942998545676, 0.6541658939362884, 0.7563510978444711]
point_13 = [1.4932274084450738, 1.7731646001211447, 0.6541658939362884, 0.7563510978444711]


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

rate = rospy.Rate(5.35)
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
                point_1[1] - 0.2 < y < point_1[1] + 0.1):
            left_fruit[0][0] = cnt_n_left
            left_fruit[0][1] = cnt_d_left
            right_fruit[0][0] = cnt_n_right
            right_fruit[0][1] = cnt_d_right

        if (point_2[0] - 0.05 < x < point_2[0] + 0.05) and (
                point_2[1] - 0.2 < y < point_2[1] + 0.1):
            left_fruit[1][0] = cnt_n_left
            left_fruit[1][1] = cnt_d_left
            right_fruit[1][0] = cnt_n_right
            right_fruit[1][1] = cnt_d_right

        if (point_3[0] - 0.05 < x < point_3[0] + 0.05) and (
                point_3[1] - 0.2 < y < point_3[1] + 0.1):
            left_fruit[2][0] = cnt_n_left
            left_fruit[2][1] = cnt_d_left
            right_fruit[2][0] = cnt_n_right
            right_fruit[2][1] = cnt_d_right

        if (point_4[0] - 0.05 < x < point_4[0] + 0.05) and (
                point_4[1] - 0.2 < y < point_4[1] + 0.1):
            left_fruit[3][0] = cnt_n_left
            left_fruit[3][1] = cnt_d_left
            right_fruit[3][0] = cnt_n_right
            right_fruit[3][1] = cnt_d_right

        if (point_5[0] - 0.05 < x < point_5[0] + 0.05) and (
                point_5[1] - 0.1 < y < point_5[1] + 0.2):
            left_fruit[4][0] = cnt_n_left
            left_fruit[4][1] = cnt_d_left
            right_fruit[4][0] = cnt_n_right
            right_fruit[4][1] = cnt_d_right

        if (point_6[0] - 0.05 < x < point_6[0] + 0.05) and (
                point_6[1] - 0.1 < y < point_6[1] + 0.2):
            left_fruit[5][0] = cnt_n_left
            left_fruit[5][1] = cnt_d_left
            right_fruit[5][0] = cnt_n_right
            right_fruit[5][1] = cnt_d_right

        if (point_7[0] - 0.05 < x < point_7[0] + 0.05) and (
                point_7[1] - 0.1 < y < point_7[1] + 0.2):
            left_fruit[6][0] = cnt_n_left
            left_fruit[6][1] = cnt_d_left
            right_fruit[6][0] = cnt_n_right
            right_fruit[6][1] = cnt_d_right

        if (point_8[0] - 0.05 < x < point_8[0] + 0.05) and (
                point_8[1] - 0.1 < y < point_8[1] + 0.2):
            left_fruit[7][0] = cnt_n_left
            left_fruit[7][1] = cnt_d_left
            right_fruit[7][0] = cnt_n_right
            right_fruit[7][1] = cnt_d_right

        if (point_9[0] - 0.05 < x < point_9[0] + 0.05) and (
                point_9[1] - 0.2 < y < point_9[1] + 0.1):
            left_fruit[8][0] = cnt_n_left
            left_fruit[8][1] = cnt_d_left
            right_fruit[8][0] = cnt_n_right
            right_fruit[8][1] = cnt_d_right

        if (point_10[0] - 0.05 < x < point_10[0] + 0.05) and (
                point_10[1] - 0.2 < y < point_10[1] + 0.1):
            left_fruit[9][0] = cnt_n_left
            left_fruit[9][1] = cnt_d_left
            right_fruit[9][0] = cnt_n_right
            right_fruit[9][1] = cnt_d_right

        if (point_11[0] - 0.05 < x < point_11[0] + 0.05) and (
                point_11[1] - 0.2 < y < point_11[1] + 0.1):
            left_fruit[10][0] = cnt_n_left
            left_fruit[10][1] = cnt_d_left
            right_fruit[10][0] = cnt_n_right
            right_fruit[10][1] = cnt_d_right

        if (point_12[0] - 0.05 < x < point_12[0] + 0.05) and (
                point_12[1] - 0.2 < y < point_12[1] + 0.1):
            left_fruit[11][0] = cnt_n_left
            left_fruit[11][1] = cnt_d_left
            right_fruit[11][0] = cnt_n_right
            right_fruit[11][1] = cnt_d_right

        if (point_13[0] - 0.05 < x < point_13[0] + 0.05) and (
                point_13[1] - 0.1 < y < point_13[1] + 0.3):
            break

        print("left_fruit: ", left_fruit)
        print("right_fruit: ", right_fruit)

    rate.sleep()

for i in range(4):
    i = 4 + i
    left_fruit[i][0] = left_fruit[i][0] + left_fruit[15 - i][0]
    left_fruit[i][1] = left_fruit[i][1] + left_fruit[15 - i][1]
    del left_fruit[15 - i]
left_fruit[4:8] = left_fruit[7], left_fruit[6], left_fruit[5], left_fruit[4]

for i in range(4):
    right_fruit[i][0] = right_fruit[i][0] + right_fruit[7 - i][0]
    right_fruit[i][1] = right_fruit[i][1] + right_fruit[7 - i][1]
    del right_fruit[7 - i]

fruits = left_fruit[0:4] + right_fruit[0:4] + left_fruit[4:8] + right_fruit[4:8]

for i in range(16):
    for j in range(2):
        fruits[i][j] = str(fruits[i][j])

f = open("store_fruits_count.txt", 'w')
f.write("tree_number / normal_fruit / disease_fruit\n")
for i in range(16):
    f.write(str(i + 1) + " / " + fruits[i][0] + " / " + fruits[i][1] + "\n")
f.close()

