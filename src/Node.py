class Node:

    def __init__(self, id, position, father, custo):
        self.position = position
        self.id = id
        self.edges = []
        self.father = father
        self.custo = custo

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def add_edge(self, edge):
        self.edges.append(edge)

    def get_edges(self):
        return self.edges

    def get_father(self):
        return self.father

    def sef_father(self, node):
        self.father = node
