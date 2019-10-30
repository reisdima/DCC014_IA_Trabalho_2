class Node:

    def __init__(self, id, position, father, real_cost, heuristic_cost):
        self.position = position
        self.id = id
        self.children = []
        self.father = father
        self.real_cost = real_cost
        self.heuristic_cost = heuristic_cost

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def get_father(self):
        return self.father

    def sef_father(self, node):
        self.father = node

    def add_child(self, node):
        self.children.append(node)

    def get_real_cost(self):
        return self.real_cost

    def get_heuristic_cost(self):
        return self.heuristic_cost

    def set_real_cost(self, cost):
        self.real_cost = cost

    def set_heuristic_cost(self, cost):
        self.heuristic_cost = cost
