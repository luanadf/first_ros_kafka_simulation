from threading import Thread
from turtlesim_move import TurtleBot

import sys

class TurtleThread(Thread):
    def __init__ (self, n_turtle, items, unload_area_goal_params, initial_coord_params):
        Thread.__init__(self)
        self.n_turtle = n_turtle
        self.items = items
        self.unload_area_goal_params = unload_area_goal_params
        self.initial_coord_params = initial_coord_params
        
    def run(self):
        # Para cada item recebido...
        for i in range(len(self.items)):

            # extrai a coordenada do item no estoque
            item_goal = self.items[i]["item_goal"]
            goal_params = eval('[' + item_goal + ']')

            x = float(goal_params[0])
            y = float(goal_params[1])
            tolerance = float(goal_params[2])

            # extrai a coordenada da area de descarga
            unload_x = float(self.unload_area_goal_params[0])
            unload_y = float(self.unload_area_goal_params[1])
            unload_tolerance = float(self.unload_area_goal_params[2])

            # extrai a coordenada inicial do robo
            initial_x = float(self.initial_coord_params[0])
            initial_y = float(self.initial_coord_params[1])
            initial_tolerance = float(self.initial_coord_params[2])

            # inicia uma funcao de movimento
            turtle = TurtleBot(self.n_turtle)
            # faz a turtle ir ate o item
            turtle.move2goal(x, y, tolerance)
            # faz a turtle ir ate a area de descarga
            turtle.move2goal(unload_x, unload_y, unload_tolerance)
            # faz a turtle ir ate a coordenada inicial
            turtle.move2goal(initial_x, initial_y, initial_tolerance)


        