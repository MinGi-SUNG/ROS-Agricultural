import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from detection_msgs.msg import BoundingBoxes

class count:
    def __init__(self):
        self.cnt_normal = 0
        self.cnt_disease = 0
        self.left_sub = rospy.Subscriber("/yolov5/detections_left", BoundingBoxes, self.callback)
        self.right_sub = rospy.Subscriber("/yolov5/detections_right", BoundingBoxes, self.callback)
        self.coor_sub = rospy.Subscriber("/amcl_pose",PoseWithCovarianceStamped, self.result)

    def Arr(self, fruit_tree):
        fruit_tree = []
        for i in range(24):
            fruit_tree.append([]) # 새로운 내부 배열 선언
            for j in range(2):
                fruit_tree[i].append(0) #해당 내부 배열에 0이라는 값 추가
    
    def callback(self):
        cnt_normal = 0
        cnt_disease = 0

        for i in range(24):
            for each in self.bounding_boxes:
                if each.Class == "normal fruit":
                    cnt_normal = cnt_normal + 1
                elif each.Class == "disease fruit":
                    cnt_disease = cnt_disease + 1

    def result(self, data):
        pose = data.pose

        x = pose.pose.point.x
        y = pose.pose.point.y
        z = pose.pose.quaternion.z
        w = pose.pose.quaternion.w
        fruit_tree = count.Arr()
        cnt_normal = count.callback(self.cnt_normal)
        cnt_disease = count.callback(self.cnt_disease)

        for i in range(24):
            if goal_x[i]-0.0001 < x < goal_x[i]+0.0001 and goal_y[i]-0.01 < y < goal_y[i]+0.01 and goal_w[i]-0.001 < w < goal_w[i]+0.001 and goal_z[i]-0.001 < z < goal_z[i]+0.001:
                fruit_tree[i][0] = cnt_normal
                fruit_tree[i][1] = cnt_disease
            print(fruit_tree)    

# class imgproc:

#     def __init__(self):
#         self.left_sub = rospy.Subscriber("/yolov5/detections_left", BoundingBoxes, self.callback)
#         self.right_sub = rospy.Subscriber("/yolov5/detections_right", BoundingBoxes, self.callback)
#         self.coor_sub = rospy.Subscriber("/amcl_pose",PoseWithCovarianceStamped, self.coordinate)

#     def callback(self):
#         cnt_n = 0
#         cnt_d = 0

#         for i in range(24):
#             for each in self.bounding_boxes:
#                 if each.Class == "normal fruit":
#                     cnt_n = cnt_n + 1
#                 elif each.Class == "disease fruit":
#                     cnt_d = cnt_d + 1
#         # print("normal count :" + str(cnt_n))
#         # print("disease fruit:" + str(cnt_d))

#     def coordinate(self, data):
#         pose = data.pose
#         x = pose.pose.point.x
#         y = pose.pose.point.y
#         z = pose.pose.quaternion.z
#         w = pose.pose.quaternion.w
                
if __name__ == '__main__':

    goal_x = [0.3571159702204996, 0.36525658182705034, 0.3675446268195606, 0.3559700612411263,
                  0.9360162491430987,0.9225821606404762, 0.885864804891293, 0.8624954249733435,
                  1.467515392151751, 1.4851977588557084, 1.5290351522300707, 1.550165613207711
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
                  0.7316800329573059, 0.7346375328504462, 0.7373369389739239, 0.7365763274043428
                  ]
    
    Untitled = count()
    Untitled.result()
