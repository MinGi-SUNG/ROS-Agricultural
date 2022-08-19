# UTF-8.


import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import Float32

def callback(msg):
    print (msg.data)

PI = 3.14159265359
rospy.init_node('topic_subscriber')
sub_left = rospy.Subscriber('/sonar_dist_left',Float32, callback)
sub_right = rospy.Subscriber('/sonar_dist_right',Float32, callback)

def move_base_to(x, y, z, w):
    client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    while (not client.wait_for_server(rospy.Duration(5))):
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



if __name__ == '__main__':
    #point 3,4 (0.972,0.320,-0.015,1.000), (1.700,0.343,0.681,0.732)
    #point 1,4 (0.331,1.756,0.077,0.997), (1.698,0.187,0.669,0.743)

    #goal_positions_x = [0.2901204523206585, 0.963, 1.044, 1.562267100233113, 1.642]
    #goal_positions_y = [1.7223068558941679, 1.745, 0.168, 0.21538396925156483, 1.834]

    #goal_pose_z = [0.08259559621331584, -0.654, -0.070, 0.6439938729142963, 0.753]
    #goal_pose_w = [0.9965831462984747, 0.757, 0.998, 0.7650306475225978, 0.658]

    goal_positions_x = [0.3392991476038756, 0.3097560751961481, 0.2985686772100214, 0.27207405922819416, 0.2465783797525702, 0.9001910050442816, 0.9228648750382785, 0.9676714284011307, 1.0012134875460368, 1.0414035190834385, 1.0491457654512253, 1.5156476373814933, 1.6144767365019963, 1.6266209114294783, 1.6065405227817624, 1.565539853518207, 1.5472984715828735, 1.5572065999549918]
    goal_positions_y = [0.2596115423732532, 0.6723858884842863, 0.8772249417024484, 1.280877335970951, 1.5141497287942225, 1.722688480551652, 1.517811736252732, 1.1124147573720116, 0.8880914536287361, 0.48345834259302795, 0.18200092463088904, 0.2672085470828418, 0.29636418553039323, 0.8550722405832151, 1.0558806658554596, 1.4617162593233084, 1.6614124562135728, 1.9979267167090695]
    goal_pose_z = [0.7191293399464606, 0.7278992358893561, 0.7247925795514931, 0.7358247178981319, 0.735021383915894, -0.6655947062425257, -0.6681738095737081, -0.6545859617152052, -0.6571213109779029, -0.6578621844792023, 0.04643422107265426, 0.09404860809503693, 0.6163380833168112, 0.7459909620870157, 0.7405149991017972, 0.7424500117079691, 0.7425409503879753, 0.7215936496181795]
    goal_pose_w = [0.6948762425268028, 0.6856841126872428, 0.6889671375523599, 0.6771720494306707, 0.6780439257056757, 0.7463133973217457, 0.7440052151697313, 0.7559875784200293, 0.753784838437788, 0.7531383314054941, 0.9989213498135756, 0.9955676066020761, 0.7874816614076543, 0.6659560679838339, 0.6720398322311448, 0.6699014704528096, 0.6698006696002344, 0.69231683847117]

    avoid_left_positions_x = []
    avoid_left_positions_y = []
    avoid_left_pose_z =[]
    avoid_left_pose_w = []

    avoid_right_positions_x = []
    avoid_right_positions_y = []
    avoid_right_pose_z = []
    avoid_right_pose_w = []

    rospy.init_node("set_navigation_goal")

    while True:
        for x, y, z, w in zip(goal_positions_x, goal_positions_y, goal_pose_z, goal_pose_w):
            result = move_base_to(x, y, z, w)
            if result:
                continue
            elif not result:
                continue
            else:
                break
            if sub_left < 7:
                for x1, y1, z1, w1 in zip(avoid_left_positions_x, avoid_left_positions_y, avoid_left_pose_z,
                                          avoid_left_pose_w):
                    left_result = move_base_to(x1, y1, z1, w1)
                    if left_result:
                        continue
                    elif not left_result:
                        continue
                    else:
                        break
            elif sub_right < 7:
                for x2, y2, z2, w2 in zip(avoid_right_positions_x, avoid_right_positions_y, avoid_right_pose_z,
                                          avoid_right_pose_w):
                    right_result = move_base_to(x2, y2, z2, w2)
                    if right_result:
                        continue
                    elif not right_result:
                        continue
                    else:
                        break
            rospy.logininfo("Good job!!!")
