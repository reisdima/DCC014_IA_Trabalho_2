from src.Player import Player
from src.Node import Node
from src.Search import Search


class OrderedSearch(Search):

    def __init__(self, file_path, maze_number):
        super().__init__(file_path, maze_number)

    def calculate_cost(self, node):
        if node.get_father() is not None:
            father = node.get_father()
            node.set_real_cost(father.get_real_cost() + 1)
            node.set_total_cost(father.get_real_cost() + 1)
