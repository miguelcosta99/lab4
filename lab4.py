import rospy
from std_msgs.msg import String

rospy.init_node('lab4')

matricula = '2017014453'

def matriculaCallBack(msg):
    global matricula
    matricula = msg.data
    
def timerCallBack(event):
    print(matricula)
    msg = String()
    msg.data = '2017014453'
    pub.publish(msg)
    
pub = rospy.Publisher('/mat', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(1), timerCallBack)
sub = rospy.Subscriber('/sum', String, matriculaCallBack)

rospy.spin()

#- Criar um código no Development Environment do Robomaker;

#- Criar um repositório no Github com o email da UNIFEI do aluno;

#- Criar um nó que envia o seu número de matrícula por um tópico;

#- Criar um nó que recebe o número de matrícula pelo tópico mencionado acima e retorna por um tópico para o primeiro nó a soma dos números;

#- A soma deve ser printada na tela durante a calback do tópico, no primeiro nó;

#- Utilizar os comandos de terminal (git add, git commit, git push, etc.) para enviar o código para o Github (link nos comentários da tarefa);

#- Disponibilizar o link do github do aluno com o código.