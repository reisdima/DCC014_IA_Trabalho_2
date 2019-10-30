from abc import ABC
from src.Search import Search
import math

class AStar(Search):

    def __init__(self, file_path):
        super().__init__(file_path)

    def calculate_cost(self, node):
        if node.get_father() is not None:
            father = node.get_father()
            node.set_real_cost(father.get_real_cost() + 1)
<<<<<<< HEAD
        heuristic_cost = self.calculate_heuristic(node)
        node.set_heuristic_cost(heuristic_cost)
        node.set_total_cost(node.get_real_cost() + node.get_heuristic_cost())
=======
            heuristic_cost = self.calculate_heuristic(node)
            node.set_heuristic_cost(0)
            node.set_total_cost(node.get_real_cost() + node.get_heuristic_cost())
>>>>>>> 6a5e2f0bd8a220287a7356bedcf65bca3315c99b

    def calculate_heuristic(self, node):
        point_node = node.get_position()
        point_end_node = self.maze.get_ending()
        distance = math.sqrt(((point_node[0] - point_end_node[0]) ** 2.0) + ((point_node[1] - point_end_node[1]) ** 2.0))
<<<<<<< HEAD
        return distance
=======
        return distance
>>>>>>> 6a5e2f0bd8a220287a7356bedcf65bca3315c99b
