# Primeira análise de tempo da simulação

Cada robô leva aproximadamente 9 segundos para:
    - Sair da sua base
    - Ir até o item
    - Ir até a plataforma de descarga
    - Voltar à sua base

Obs: isso considerando que a base do robô fica no meio do galpão, assim a distância até cada item é sempre a mesma.

Ao fazer a análise para um pedido com diversas quantidades de itens e robôs, chegamos aos seguintes resultados:
    - 1 pedido / 1 items / 1 robo = 9s
    - 1 pedido / 2 items / 2 robos = 9s 
    - 1 pedido / 30 items / 30 robos = 9s
    - 1 pedido / 2 items / 1 robo = 18s
    - 1 pedido / 30 items / 15 robos = 18s
    - 1 pedido / 30 items / 20 robos = 18s

Assim podemos calcular o tempo como, o número de pedidos * a divisão entre items e robos (arredondada para cima) * 9

Tempo = pedidos * items/robos * 9

Essa análise considera que todos os robôs do galpão, recebem um pedido por vez para processarem, isto é, se tivermos um pedido com 3 itens e 5 robôs no galpão, 3 robôs buscarão os itens e os 2 que sobraram ficam inativos; somente depois que esse pedido é entregue, é processado o próximo pedido.

# Próximos passos

O próximo passo, seria ajustar a simulação para que, se houver robôs inativos no processamento de um pedido, eles devem receber o próximo pedido da fila para processar e assim por diante, até que todos os robôs do galpão estejam ocupados com algum pedido. 