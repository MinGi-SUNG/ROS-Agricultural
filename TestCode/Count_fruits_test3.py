import rospy
# import odeme
from detection_msgs.msg import BoundingBoxes

goal_x = [0.3571159702204996, 0.36525658182705034, 0.3675446268195606, 0.3559700612411263,
          0.9360162491430987, 0.9225821606404762, 0.885864804891293, 0.8624954249733435,
          1.467515392151751, 1.4851977588557084, 1.5290351522300707, 1.550165613207711,
          ]
goal_y = [0.2467059225612903, 0.8500968436670182, 1.0522210161642764, 1.252957380530777,
          1.4042942998545676, 1.2014037770427746, 0.8001815056501693, 0.5985026748388733,
          0.3562987097651186, 0.5892779632001173, 1.0640185250550112, 1.298339546550991
          ]
goal_z = [0.6870837036357698, 0.7029967546694268, 0.6988597872148938, 0.7234542222897506,
          -0.7281633426560493, -0.7332120319008505, -0.7458937121655593, -0.7503769339072462,
          0.6816482446039128, 0.6784597963972586, 0.675525157506783, 0.6763544292067071
          ]
goal_w = [0.7265782712125058, 0.7111930560152101, 0.715258692931413, 0.6903723547848161,
          0.6854036375829712, 0.6800000854969257, 0.6660649894356269, 0.6610101792408043,
          0.7316800329573059, 0.7346375328504462, 0.7373369389739239, 0.7365763274043428,
          ]


def callback(data):
    global normal
    global disease
    global img
    global cnt_n
    global cnt_d
    img = data
    cnt_n = 0
    cnt_d = 0
    # normal.append(cnt_n)
    # disease.append(cnt_d)

    # count_fruits 노드 종료 코드 추가


# for i in range(0, 11): if (goal_x[i] - 0.01 <= odeme.d.x <= goal_x[i] + 0.01) and (goal_y[i] - 0.06 <= odeme.d.y <=
# goal_y[i] + 0.06) and ( goal_z[i] - 0.001 <= odeme.d.z <= goal_z[i] + 0.001) and ( goal_w[i] - 0.001 <= odeme.d.w
# <= goal_w[i] + 0.001):


rospy.init_node("current_position", anonymous=True)
rospy.Subscriber("/yolov5/detections_left", BoundingBoxes, callback)
rospy.Subscriber("/yolov5/detections_right", BoundingBoxes, callback)

normal = [None] * 12
disease = [None] * 12
img = None
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    if img is not None:
        for each in img.bounding_boxes:
            if each.Class == "normal fruit":
                cnt_n = cnt_n + 1
            elif each.Class == "disease fruit":
                cnt_d = cnt_d + 1
        normal.append(cnt_n)
        disease.append(cnt_d)
    print(disease)
    # print(type(disease))
    rate.sleep()
