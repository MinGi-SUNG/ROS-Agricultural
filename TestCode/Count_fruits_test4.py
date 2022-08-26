#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from detection_msgs.msg import BoundingBoxes
import os 
os.system('Python3 odome_test.py')
import odome_test

left_fruit = [[0 for col in range(2)] for row in range(12)]
right_fruit = [[0 for col in range(2)] for row in range(12)]

def left_callback(msg):
    global left_cnt_n
    global left_cnt_d
    for each in msg.bounding_boxes:
        if each.Class == "normal fruit":
            left_cnt_n = left_cnt_n + 1
        elif each.Class == "disease fruit":
            left_cnt_d = left_cnt_d + 1

def right_callback(msg):
    global right_cnt_n 
    global right_cnt_d
    for each in msg.bounding_boxes:
        if each.Class == "normal fruit":
            right_cnt_n = right_cnt_n + 1
        elif each.Class == "disease fruit":
            right_cnt_d = right_cnt_d + 1

# goal_x = [0.3571159702204996, 0.36525658182705034, 0.3675446268195606, 0.3559700612411263,
#                   0.9360162491430987, 0.9225821606404762, 0.885864804891293, 0.8624954249733435,
#                   1.467515392151751, 1.4851977588557084, 1.5290351522300707, 1.550165613207711
#                    ]
# goal_y = [0.2467059225612903, 0.8500968436670182, 1.0522210161642764, 1.252957380530777,
#                   1.4042942998545676, 1.2014037770427746, 0.8001815056501693, 0.5985026748388733,
#                   0.3562987097651186, 0.5892779632001173, 1.0640185250550112, 1.298339546550991
#                    ]
# goal_z = [0.6870837036357698, 0.7029967546694268, 0.6988597872148938, 0.7234542222897506,
#                   -0.7281633426560493, -0.7332120319008505, -0.7458937121655593, -0.7503769339072462,
#                   0.6816482446039128, 0.6784597963972586, 0.675525157506783, 0.6763544292067071
#                   ]
# goal_w = [0.7265782712125058, 0.7111930560152101, 0.715258692931413, 0.6903723547848161,
#                   0.6854036375829712, 0.6800000854969257, 0.6660649894356269, 0.6610101792408043,
#                   0.7316800329573059, 0.7346375328504462, 0.7373369389739239, 0.7365763274043428
#                   ]

point_1 = [0.3571159702204996, 0.2467059225612903, 0.6870837036357698, 0.7265782712125058]
point_2 = [0.36525658182705034, 0.8500968436670182, 0.7029967546694268, 0.7111930560152101]
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

right_cnt_n, right_cnt_d, left_cnt_n, left_cnt_d = 0
rospy.init_node("topic_subscriber")
left_sub = rospy.Subscriber("/yolov5/detections_left", BoundingBoxes, left_callback)
right_sub = rospy.Subscriber("/yolov5/detections_right", BoundingBoxes, right_callback)

if (point_1[0]-0.01 < odome_test.d.x < point_1[0]+0.01) and (point_1[1]-0.06 < odome_test.d.y < point_1[1]+0.06) and (point_1[2]-0.001 < odome_test.d.z < point_1[2]+0.01) and (point_1[3]-0.001 < odome_test.d.w < point_1[3]+0.001):
    left_fruit[0][0] = left_cnt_n
    left_fruit[1][0] = left_cnt_d
    right_fruit[0][0] = right_cnt_n
    right_fruit[1][0] = right_cnt_d
elif (point_2[0]-0.01 < odome_test.d.x < point_2[0]+0.01) and (point_2[1]-0.06 < odome_test.d.y < point_2[1]+0.06) and (point_2[2]-0.001 < odome_test.d.z < point_2[2]+0.01) and (point_2[3]-0.001 < odome_test.d.w < point_2[3]+0.001):
    left_fruit[0][1] = left_cnt_n
    left_fruit[1][1] = left_cnt_d
    right_fruit[0][1] = right_cnt_n
    right_fruit[1][1] = right_cnt_d
elif (point_3[0]-0.01 < odome_test.d.x < point_3[0]+0.01) and (point_3[1]-0.06 < odome_test.d.y < point_3[1]+0.06) and (point_3[2]-0.001 < odome_test.d.z < point_3[2]+0.01) and (point_3[3]-0.001 < odome_test.d.w < point_3[3]+0.001):
    left_fruit[0][2] = left_cnt_n
    left_fruit[1][2] = left_cnt_d
    right_fruit[0][2] = right_cnt_n
    right_fruit[1][2] = right_cnt_d
elif (point_4[0]-0.01 < odome_test.d.x < point_4[0]+0.01) and (point_4[1]-0.06 < odome_test.d.y < point_4[1]+0.06) and (point_4[2]-0.001 < odome_test.d.z < point_4[2]+0.01) and (point_4[3]-0.001 < odome_test.d.w < point_4[3]+0.001):
    left_fruit[0][3] = left_cnt_n
    left_fruit[1][3] = left_cnt_d
    right_fruit[0][3] = right_cnt_n
    right_fruit[1][3] = right_cnt_d
elif (point_5[0]-0.01 < odome_test.d.x < point_5[0]+0.01) and (point_5[1]-0.06 < odome_test.d.y < point_5[1]+0.06) and (point_5[2]-0.001 < odome_test.d.z < point_5[2]+0.01) and (point_5[3]-0.001 < odome_test.d.w < point_5[3]+0.001):
    left_fruit[0][4] = left_cnt_n
    left_fruit[1][4] = left_cnt_d
    right_fruit[0][4] = right_cnt_n
    right_fruit[1][4] = right_cnt_d
elif (point_6[0]-0.01 < odome_test.d.x < point_6[0]+0.01) and (point_6[1]-0.06 < odome_test.d.y < point_6[1]+0.06) and (point_6[2]-0.001 < odome_test.d.z < point_6[2]+0.01) and (point_6[3]-0.001 < odome_test.d.w < point_6[3]+0.001):
    left_fruit[0][5] = left_cnt_n
    left_fruit[1][5] = left_cnt_d
    right_fruit[0][5] = right_cnt_n
    right_fruit[1][5] = right_cnt_d
elif (point_7[0]-0.01 < odome_test.d.x < point_7[0]+0.01) and (point_7[1]-0.06 < odome_test.d.y < point_7[1]+0.06) and (point_7[2]-0.001 < odome_test.d.z < point_7[2]+0.01) and (point_7[3]-0.001 < odome_test.d.w < point_7[3]+0.001):
    left_fruit[0][6] = left_cnt_n
    left_fruit[1][6] = left_cnt_d
    right_fruit[0][6] = right_cnt_n
    right_fruit[1][6] = right_cnt_d
elif (point_8[0]-0.01 < odome_test.d.x < point_8[0]+0.01) and (point_8[1]-0.06 < odome_test.d.y < point_8[1]+0.06) and (point_8[2]-0.001 < odome_test.d.z < point_8[2]+0.01) and (point_8[3]-0.001 < odome_test.d.w < point_8[3]+0.001):
    left_fruit[0][7] = left_cnt_n
    left_fruit[1][7] = left_cnt_d
    right_fruit[0][7] = right_cnt_n
    right_fruit[1][7] = right_cnt_d
elif (point_9[0]-0.01 < odome_test.d.x < point_9[0]+0.01) and (point_9[1]-0.06 < odome_test.d.y < point_9[1]+0.06) and (point_9[2]-0.001 < odome_test.d.z < point_9[2]+0.01) and (point_9[3]-0.001 < odome_test.d.w < point_9[3]+0.001):
    left_fruit[0][8] = left_cnt_n
    left_fruit[1][8] = left_cnt_d
    right_fruit[0][8] = right_cnt_n
    right_fruit[1][8] = right_cnt_d
elif (point_10[0]-0.01 < odome_test.d.x < point_10[0]+0.01) and (point_10[1]-0.06 < odome_test.d.y < point_10[1]+0.06) and (point_10[2]-0.001 < odome_test.d.z < point_10[2]+0.01) and (point_10[3]-0.001 < odome_test.d.w < point_10[3]+0.001):
    left_fruit[0][9] = left_cnt_n
    left_fruit[1][9] = left_cnt_d
    right_fruit[0][9] = right_cnt_n
    right_fruit[1][9] = right_cnt_d
elif (point_11[0]-0.01 < odome_test.d.x < point_11[0]+0.01) and (point_11[1]-0.06 < odome_test.d.y < point_11[1]+0.06) and (point_11[2]-0.001 < odome_test.d.z < point_11[2]+0.01) and (point_11[3]-0.001 < odome_test.d.w < point_11[3]+0.001):
    left_fruit[0][10] = left_cnt_n
    left_fruit[1][10] = left_cnt_d
    right_fruit[0][10] = right_cnt_n
    right_fruit[1][10] = right_cnt_d
elif (point_12[0]-0.01 < odome_test.d.x < point_12[0]+0.01) and (point_12[1]-0.06 < odome_test.d.y < point_12[1]+0.06) and (point_12[2]-0.001 < odome_test.d.z < point_12[2]+0.01) and (point_12[3]-0.001 < odome_test.d.w < point_12[3]+0.001):
    left_fruit[0][11] = left_cnt_n
    left_fruit[1][11] = left_cnt_d
    right_fruit[0][11] = right_cnt_n
    right_fruit[1][11] = right_cnt_d

print("left_fruit: ", left_fruit)
print("right_fruit: ", right_fruit)



# rate = rospy.Rate(10)
# while not rospy.is_shutdown():
#     if  is not 0:
#         print(d)
#     rate.sleep() #Sleep at 10Hz
