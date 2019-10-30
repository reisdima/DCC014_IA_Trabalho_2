from src.Player import Player
from src.Node import Node
from src.Search import Search

class HeuristicSearch(Search):

    def __init__(self, file_path):
        super().__init__(file_path)

    def calculate_cost(self, node):
        father = node.get_father()
        node.set_heuristic_cost(father.get_total_cost() + node)

    def add_to_opened_list(self, node):
        self.opened_list.append(node)