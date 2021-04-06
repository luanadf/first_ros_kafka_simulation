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
                2: {
                    "item_id": "2",
                    "status": "01",
                    "item_goal": "1, 1, 0.1"
                },
                3: {
                    "item_id": "3",
                    "status": "01",
                    "item_goal": "10, 10, 0.1"
                },
                4: {
                    "item_id": "4",
                    "status": "01",
                    "item_goal": "1, 1, 0.1"
                },
                5: {
                    "item_id": "5",
                    "status": "01",
                    "item_goal": "10, 10, 0.1"
                },
                6: {
                    "item_id": "6",
                    "status": "01",
                    "item_goal": "1, 1, 0.1"
                },
                7: {
                    "item_id": "7",
                    "status": "01",
                    "item_goal": "10, 10, 0.1"
                },
                8: {
                    "item_id": "8",
                    "status": "01",
                    "item_goal": "1, 1, 0.1"
                },
                9: {
                    "item_id": "9",
                    "status": "01",
                    "item_goal": "10, 10, 0.1"
                },
                10: {
                    "item_id": "10",
                    "status": "01",
                    "item_goal": "1, 1, 0.1"
                },
                11: {
                    "item_id": "11",
                    "status": "01",
                    "item_goal": "10, 10, 0.1"
                },
                12: {
                    "item_id": "12",
                    "status": "01",
                    "item_goal": "1, 1, 0.1"
                },
                13: {
                    "item_id": "13",
                    "status": "01",
                    "item_goal": "10, 10, 0.1"
                },
                14: {
                    "item_id": "14",
                    "status": "01",
                    "item_goal": "1, 1, 0.1"
                },
                15: {
                    "item_id": "15",
                    "status": "01",
                    "item_goal": "10, 10, 0.1"
                },
                16: {
                    "item_id": "16",
                    "status": "01",
                    "item_goal": "1, 1, 0.1"
                },
                17: {
                    "item_id": "17",
                    "status": "01",
                    "item_goal": "10, 10, 0.1"
                },
                18: {
                    "item_id": "18",
                    "status": "01",
                    "item_goal": "1, 1, 0.1"
                },
                19: {
                    "item_id": "19",
                    "status": "01",
                    "item_goal": "10, 10, 0.1"
                },
                20: {
                    "item_id": "20",
                    "status": "01",
                    "item_goal": "1, 1, 0.1"
                },
                21: {
                    "item_id": "21",
                    "status": "01",
                    "item_goal": "10, 10, 0.1"
                },
                22: {
                    "item_id": "22",
                    "status": "01",
                    "item_goal": "1, 1, 0.1"
                },
                23: {
                    "item_id": "23",
                    "status": "01",
                    "item_goal": "10, 10, 0.1"
                },
                24: {
                    "item_id": "24",
                    "status": "01",
                    "item_goal": "1, 1, 0.1"
                },
                25: {
                    "item_id": "25",
                    "status": "01",
                    "item_goal": "10, 10, 0.1"
                },
                26: {
                    "item_id": "26",
                    "status": "01",
                    "item_goal": "1, 1, 0.1"
                },
                27: {
                    "item_id": "27",
                    "status": "01",
                    "item_goal": "10, 10, 0.1"
                },
                28: {
                    "item_id": "28",
                    "status": "01",
                    "item_goal": "1, 1, 0.1"
                },
                29: {
                    "item_id": "29",
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