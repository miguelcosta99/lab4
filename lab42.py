import rospy
from std_msgs.msg import String

rospy.init_node('lab42')

x = '0'

def topicCallBack(total):
    global x
    x = total.data
   
    
rospy.Subscriber('/matricula', String, topicCallBack)
 
def timerCallBack(event):
    
    total = 0
    
    for i in x:
        total = total + int(i)
        
    msg = String()
    msg.data = str(total)
    
    pub.publish(msg)
    
pub = rospy.Publisher('/soma', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(1), timerCallBack)


rospy.spin()