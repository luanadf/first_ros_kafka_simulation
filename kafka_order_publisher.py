import json
from threading import Thread, Lock
from kafka import KafkaProducer
import random
from time import sleep

# Quantos pedidos devem ser criados, para simulacao
n_pedidos = 1

# Funcao de producao de mensagens (so produz uma por vez)
def talker():
    # Nome do topico que vai receber a mensagem
    kafka_topic = 'kafka_topic'
    i = 0

    while (i < n_pedidos):
        n = random.randint(0,1)

        msg = {
            "order_id": str(i),
            "order_status": "01",
            "order_priority": str(n), # 0 = normal, 1 = high
            "items" : {
                0: {
                    "item_id": "0",
                    "status": "01",
                    "item_goal": "1, 1, 0.1"
                },
                1: {
                    "item_id": "1",
                    "status": "01",
                    "item_goal": "10, 10, 0.1"
                },
            },
            "unload_area_goal": "10, 1, 0.1",
            "initial_coord": "5, 5, 0.1",
        }

        print("pedido " + msg['order_id'] + ": prioridade " + msg['order_priority'])

        # Transforma o JSON em string (pq o conector kafka-ros so funciona com string, velocidade angular e imagem)
        # Talvez tentar adicionar o tipo json no conector mais pra frente
        msg = json.dumps(msg)
        
        #print(msg)
        
        # Pega a mensagem e envia para o topico
        producer = KafkaProducer(bootstrap_servers="localhost:9092", value_serializer=lambda x: json.dumps(x).encode('ascii'))
        producer.send(kafka_topic, {"data": msg})
        sleep(0.5)
        i+=1


if __name__ == '__main__':
    talker()