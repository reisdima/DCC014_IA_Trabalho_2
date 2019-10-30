from src import Player, Maze
from src import Node


class OrderedSearch:

    def __init__(self, file_path):
        self.maze = Maze(file_path)
        self.player = None
        self.closed_list = []
        self.opened_list = []
        self.current_cost = 0
        self.root_node = None

    def start_search(self):
        if self.maze.create_maze_from_file():
            self.player = Player(self.maze.get_start())
            self.root_node = Node(0, self.player.get_position(), None, 0)
            self.opened_list.append(self.root_node)
            success = False
            while len(self.opened_list) != 0:
                current_node = self.opened_list.pop(0)
                if not self.is_sucess(current_node):
                    self.explore_node(current_node)
                else:
                    success = True
                    print('sucesso')
                    break
                        
        else:
            print('Não foi possível criar o labirinto')

    def is_success(self, node):
        print('função que verifica se o nó passado como param é o nó final')

    def explore_node(self, node):
        print('função para explorar e adicionar possiveis caminhos a lista de abertos')

