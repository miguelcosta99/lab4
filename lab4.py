import rospy
from std_msgs.msg import String

rospy.init_node('lab4')
matricula = 'matricula: 2017014453'

def matriculaCallBack(msg):
    global matricula
    matricula = msg.data
    
def timerCallBack(event):
    print(matricula)
    msg = String()
    msg.data = '2017014453'
    pub.publish(msg)
    
pub = rospy.Publisher('/matricula', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(1), timerCallBack)
sub = rospy.Subscriber('/soma', String, matriculaCallBack)

rospy.spin()