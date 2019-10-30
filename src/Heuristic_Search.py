from src.Player import Player
from src.Node import Node
from src.Search import Search
import math

class HeuristicSearch(Search):

    def __init__(self, file_path):
        super().__init__(file_path)

    def calculate_cost(self, node):
        if node.get_father() is not None:
            father = node.get_father()
            node.set_real_cost(father.get_real_cost() + 1)
        heuristic_cost = self.calculate_heuristic(node)
        node.set_heuristic_cost(heuristic_cost)
        node.set_total_cost(heuristic_cost)

    def calculate_heuristic(self, node):
        point_node = node.get_position()
        point_end_node = self.maze.get_ending()
        distance = math.sqrt(((point_node[0] - point_end_node[0]) ** 2.0) + ((point_node[1] - point_end_node[1]) ** 2.0))
        return distance