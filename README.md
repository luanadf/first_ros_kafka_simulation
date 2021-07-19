# kafka_ros_with_turtlesim

## Como usar
Primeiro, rodar os comandos em terminais <b>diferentes</b>:
<br/>

```roscore``` , para iniciar o ROS <br/>
```zookeeper-server-start.sh /home/luana/kafka/config/zookeeper.properties``` , para iniciar o Zookeeper <br/>
```kafka-server-start.sh /home/luana/kafka/config/server.properties``` , para iniciar o servidor do Kafka <br/>
```roslaunch ros_kafka_connector ros_publish.launch```, para iniciar o conector ROS-Kafka <br/>
```rosrun turtlesim turtlesim_node``` , para iniciar o turtlesim <br/>
```rosservice call /spawn 5 5 0.2 ""``` , para plotar mais turtles no mapa (os argumentos "5 5" são as coordenadas para o plot, você pode colocar as coordenadas que quiser) <br/>
<br/>

### Obs:
1) Quando rodar o servidor ROS-Kafka, tenha certeza que nos arquivos do conector, os nomes dos tópicos estão como: "ros-topic" e "kafka-topic" (por padrão o nome é "test" para ambos). Para saber o nome dos tópicos que estão sendo utilizados pelo conector, basta rodá-lo no terminal que aparecerá a mensagem:
```Using std_msgs/String MSGs from KAFKA: kafka_topic -> ROS: ros_topic```<br/>
2) Se houver um erro ao executar o código do conector, pode ser porque o path do catkin ainda não foi configurado. Para resolver, basta executar: ```cd ~/catkin_ws``` e ```source ./devel/setup.bash	```

<br/>

Depois, clone os arquivos desse repositório no seu computador. Para iniciar o listener do ros_topic, executar: ```python ros_order_process.py```. E, para enviar mensagens com o produtor do Kafka: ```python kafka_order_publisher.py```. <br/>
O produtor de mensagens do kafka apenas envia n mensagens por execução, sendo n = n_pedidos em "kafka_order_publisher". 
