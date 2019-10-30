from src import Player, Maze
from src import Node


class Search:

    def is_success(self, node):  # Função que verifica se o nó é o final do labirinto
        print('função que verifica se o nó passado como param é o nó final')

    def explore_node(self, node):   #Função que explora o nó e adiciona na lista de abertos
        print('função para explorar e adicionar possiveis caminhos a lista de abertos')
        moves = self.player.get_moves()
        for m in moves:
            new_position = m()
            if self.can_move_to_position(new_position) and not self.is_in_way(new_position):
                new_node = Node(0, new_position, node, self.current_cost)
                self.opened_list.append(new_node)

    def is_on_way(self, position, current_node):
        print('Função que verifica se o nó está no caminho')
        aux_node = current_node
        while aux_node is not None:
            if aux_node.get_position() == position:
                return True
            aux_node = aux_node.get_father()
        return False

    def can_move_to_position(self, position):
        width = self.maze.get_width()
        height = self.maze.get_height()
        if(0 <= position[0] < height) and (0 <= position[1] < width):
            if self.maze.get_info_position(position) != '#':
                return True