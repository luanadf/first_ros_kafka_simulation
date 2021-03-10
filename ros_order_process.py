#!/usr/bin/env python
import rospy
import json
from std_msgs.msg import String
from threading import Thread, Lock
import threading
from turtle_thread import TurtleThread
from time import sleep

mutex = threading.Lock()
high_priority_msgs = []
normal_priority_msgs = []

# Funcao que recebe o pedido da vez e manda para os robos executarem 
def processOrder(order):
    # separacao dos dados da mensagem
    items = order['items']

    unload_area_goal = order['unload_area_goal']
    unload_area_goal_params = eval('[' + unload_area_goal + ']')

    initial_coord = order['initial_coord']
    initial_coord_params = eval('[' + initial_coord + ']')
    
    # define quantos item e quantos robos temos
    n_items = len(items)
    n_robots = 2

    more_items = False
    more_robots = False
    equal = False

    # array com a quantidade de items que o robo vai receber
    indexesPerRobot = []
    indexesPerRobot = [0 for i in range(n_robots)] 
    
    # distribui items do pedido para os robos (3 pedidos e 2 robos = robo1 ganha 2 pedidos, e robo2 ganha 1)
    if (n_items > n_robots):
        more_items = True
    elif (n_robots > n_items):
        more_robots = True
    elif (n_robots == n_items):
        equal = True

    if (more_items or equal):
        q = n_items / n_robots
        r = n_items % n_robots

        for i in range(n_robots):
            indexesPerRobot[i] = q
        
        for i in range(r): 
            indexesPerRobot[i] = indexesPerRobot[i] + 1
    
    elif (more_robots):
        for i in range(n_items):
            indexesPerRobot[i] = 1

    
    try:
        accumulated = 0
        # para cada robo vai ser criada uma thread, paralelizando o processo
        for i in range(n_robots):
            # pega o indice do primeiro pedido dividido para aquele robo
            inicio = accumulated
            # pega o indice do ultimo pedido dividido para aquele robo
            fim = accumulated + (indexesPerRobot[i]-1)
            # vetor com os determinados pedidos para cada robo
            itemsPerTurtle = []
            for j in range(inicio, fim+1):
                item = items[str(j)]
                itemsPerTurtle.append(item)

            # pega o nome da turtle
            n_turtle = 'turtle'+str(i+1)

            accumulated = accumulated + indexesPerRobot[i]

            thread = TurtleThread(n_turtle, itemsPerTurtle, 
                     unload_area_goal_params, initial_coord_params)
            thread.start()
            
        # espera todas as threads desse pedido terminarem, para processar o proximo
        thread.join()
    except rospy.ROSInterruptException:
            pass

# Funcao que pega os pedidos das filas e manda para a funcao que envia para os robos
def getOrder():
    while True:
        if (len(high_priority_msgs) != 0):
            mutex.acquire()
            order = high_priority_msgs.pop(0)
            mutex.release()
            print(order['order_id'] + ": prioridade " + order['order_priority'])
            processOrder(order)
            
        elif (len(high_priority_msgs) == 0 and len(normal_priority_msgs) != 0):
            mutex.acquire()
            order = normal_priority_msgs.pop(0)
            mutex.release()
            print(order['order_id'] + ": prioridade " + order['order_priority'])
            processOrder(order)

        else:
            continue

# Funcao "principal" que processa a mensagem recebida e divide entre:
# fila de prioridade alta e fila de prioridade normal
def callback(data):
    order = json.loads(data.data)

    priority = order['order_priority']

    if priority == "1":
        mutex.acquire()
        high_priority_msgs.append(order)
        mutex.release()
    else:
        mutex.acquire()
        normal_priority_msgs.append(order)
        mutex.release()

# Funcao que fica "ouvindo" o topico ros_topic 
def listener():
    rospy.init_node('listener', anonymous=True)

    get_order_thread = Thread(target=getOrder)
    get_order_thread.start()

    rospy.Subscriber("ros_topic", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

    
