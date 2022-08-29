# UTF-8.

import rospy
import actionlib
from std_msgs.msg import Float32
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

PI = 3.14159265359


def sonar_left_callback(data):
    global left_sonar
    left_sonar = data.data


def sonar_right_callback(data):
    global right_sonar
    right_sonar = data.data


left_sonar = None
right_sonar = None

rospy.init_node("set_navigation_goal")
rate = rospy.Rate(5.35)
rospy.Subscriber('/sonar_dist_left', Float32, sonar_left_callback)
rospy.Subscriber('/sonar_dist_right', Float32, sonar_right_callback)


def move_base_to(x, y, z, w):
    client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    while not client.wait_for_server(rospy.Duration(5)):
        rospy.loginfo("Waiting for the move_base action server to come up")

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"

    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.z = z
    goal.target_pose.pose.orientation.w = w

    rospy.loginfo("Sending goal")
    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available")
    else:
        return client.get_result()

while not rospy.is_shutdown():
    if left_sonar is not None:
            print(left_sonar)
    
    if right_sonar is not None:
            print(right_sonar)
    rate.sleep()

if __name__ == '__main__':

    goal_positions_x = [0.3458243520930942, 0.3458243520930942, 0.3458243520930942, 0.3458243520930942,
                        0.3458243520930942, 0.9428930232051557, 0.9428930232051557, 0.9428930232051557,
                        0.9428930232051557, 0.9428930232051557, 0.9428930232051557, 1.4932274084450738,
                        1.4932274084450738, 1.4932274084450738, 1.4932274084450738, 1.4932274084450738,
                        1.4932274084450738]

    goal_positions_y = [0.300026188169096, 0.793989172685527, 1.0433756843422264, 1.2993974382926154,
                        1.5612097353480232, 1.605179606396488, 1.4042942998545676, 1.1124147573720116,
                        0.8880914536287361, 0.48345834259302795, 0.30145834259302795, 0.17145834259302795,
                        0.33622629277772825, 0.8880914536287361, 1.1124147573720116, 1.4042942998545676,
                        1.7731646001211447]

    goal_pose_z = [0.7118179508158713, 0.7118179508158713, 0.7118179508158713, 0.7118179508158713,
                   0.7118179508158713, -0.7005033842350507, -0.7281633426560493, -0.7281633426560493,
                   -0.7281633426560493, -0.7281633426560493, -0.7281633426560493, 0.6541658939362884,
                   0.6541658939362884, 0.6541658939362884, 0.6541658939362884, 0.6541658939362884,
                   0.6541658939362884]

    goal_pose_w = [0.7023640116750671, 0.7023640116750671, 0.7023640116750671, 0.7023640116750671,
                   0.7023640116750671, 0.7136490795028331, 0.6854036375829712, 0.7559875784200293,
                   0.753784838437788, 0.7531383314054941, 0.7527383314054941, 0.7563510978444711,
                   0.7563510978444711, 0.7563510978444711, 0.7563510978444711, 0.7563510978444711,
                   0.7563510978444711]

    
    for x, y, z, w in zip(goal_positions_x, goal_positions_y, goal_pose_z, goal_pose_w):
        result = move_base_to(x, y, z, w)
        if result:
            if left_sonar <= 7:
                x1, y1, z1, w1 = zip(left_position_x, left_position_y, left_pose_z, left_pose_w)
                result = move_base_to(x1, y1, z1, w1)
            else:
                x, y, z, w = zip(goal_positions_x, goal_positions_y, goal_pose_z, goal_pose_w)
                result = result = move_base_to(x, y, z, w) 

            if right_sonar <= 7:
                x2, y2, z2, w2 = zip(right_position_x, right_position_y, right_pose_z, right_pose_w)
                result = move_base_to(x2, y2, z2, w2)
            else:
                x, y, z, w = zip(goal_positions_x, goal_positions_y, goal_pose_z, goal_pose_w)
                result = result = move_base_to(x, y, z, w)

            continue
            
        elif not result:
            continue
        else:
            break
        rospy.logininfo("Good job!!!")
