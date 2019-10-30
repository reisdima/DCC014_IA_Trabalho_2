from src import Player, Maze
from src import Node
from src import Search


class OrderedSearch(Search):

    def __init__(self, file_path):
        super.__init__(file_path)

    def start_search(self):
        if self.maze.create_maze_from_file():  # Verifica se conseguiu ler o arquivo e criar a matriz do labirinto
            self.player = Player(self.maze.get_start())  # Posiciona o jogador no inicio do labirinto
            self.root_node = Node(0, self.player.get_position(), None, 0)  # Cria o no raiz da árvore
            self.opened_list.append(self.root_node)  # Adiciona o nó raiz na lista de abertos
            success = False
            while len(self.opened_list) != 0:
                current_node = self.opened_list.pop(0)  # Pega o primeiro nó da lista de abertos
                self.player.set_position(current_node.get_position())
                if not self.is_sucess(current_node):  # Se não for sucesso, explora esse nó
                    self.explore_node(current_node)
                    if len(current_node.children) > 0:
                        for child in current_node.children:
                            self.calculate_cost(child)
                            self.opened_list.append(child)
                        self.closed_list.append(current_node)

                else:
                    success = True
                    print('sucesso')
                    break
        else:
            print('Não foi possível criar o labirinto')

    def calculate_cost(self, node):
        father = node.get_father()
        node.set_real_cost(father.get_real_cost() + 1)