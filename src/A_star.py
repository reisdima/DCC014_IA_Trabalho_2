from abc import ABC
from src.Search import Search


class AStar(Search, ABC):

    def __init__(self, file_path):
        super().__init__(file_path)

    def calculate_cost(self, node):
        father = node.get_father()
        node.set_real_cost(father.get_real_cost() + 1)
        node.set_heuristic_cost(0)
        node.set_total_cost(node.get_real_cost() + node.get_heuristic_cost())

    def add_to_opened_list(self, node):
        for i in range(len(self.opened_list)):
            if node.get_total_cost() < self.opened_list[i].get_total_cost():
                self.opened_list.insert(i, node)
                break
