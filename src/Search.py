from abc import abstractmethod
from src.Maze import Maze
from src.Node import Node
from src.Player import  Player


class Search:
    def __init__(self, file_path):
        self.maze = Maze(file_path)
        self.player = None
        self.closed_list = []
        self.opened_list = []
        self.root_node = None
        self.success_way = []

    def start_search(self):
        if self.maze.create_maze_from_file():  # Verifica se conseguiu ler o arquivo e criar a matriz do labirinto
            self.player = Player(self.maze.get_start())  # Posiciona o jogador no inicio do labirinto
            self.root_node = Node(self.player.get_position(), None, 0, 0)  # Cria o no raiz da árvore
            self.opened_list.append(self.root_node)  # Adiciona o nó raiz na lista de abertos
            success = False
            while len(self.opened_list) != 0:
                self.print_fluxograma()
                current_node = self.opened_list.pop(0)  # Pega o primeiro nó da lista de abertos
                self.player.set_position(current_node.get_position())
                if not self.is_success(current_node):  # Se não for sucesso, explora esse nó
                    self.explore_node(current_node)
                else:
                    success = True
                    print("------------- Final ---------------")
                    self.create_success_way(current_node)
                    print("\n A arvore gerada eh: \n")
                    self.pprint_tree(self.root_node, "", True)
                    self.maze_solution()
                    break
            if not success:
                print('Não encontrou solução')
        else:
            print('Não foi possível criar o labirinto')

    def is_success(self, node):  # Função que verifica se o nó é o final do labirinto
        # print('função que verifica se o nó passado como param é o nó final')
        position = node.get_position()
        if position == self.maze.get_ending():
            return True
        return False

    def explore_node(self, node):   #Função que explora o nó e adiciona na lista de abertos
        # print('função para explorar e adicionar possiveis caminhos a lista de abertos')
        moves = self.player.get_moves()
        for m in moves:
            new_position = m()
            if self.can_move_to_position(new_position) and not self.is_on_way(new_position, node):
                new_node = Node(new_position, node, 0, 0)
                node.add_child(new_node)
                self.calculate_cost(new_node)
                self.add_to_opened_list(new_node)
        self.closed_list.append(node)

    def is_on_way(self, position, current_node):
        # print('Função que verifica se o nó está no caminho')
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

    @abstractmethod
    def calculate_cost(self, node):
        pass

    @abstractmethod
    def add_to_opened_list(self, node):
        pass

    def create_success_way(self, node):
        current_node = node
        self.success_way = []
        i = 0
        while current_node is not None:
            self.success_way.append(current_node.get_position())
            current_node = current_node.get_father()
            i += 1
        self.success_way.reverse()
        print('Caminho do sucesso: {}'.format(self.success_way))
        print("O nivel da solucao eh: {}".format(len(self.success_way) - 1))

    # Funcoes para Printar Informacoes
    def pprint_tree(self, node, _prefix, _last):
        print(_prefix, "`- " if _last else "|- ", node.get_information(), sep="")
        _prefix += "   " if _last else "|  "
        child_count = len(node.children)
        for i, child in enumerate(node.children):
            _last = i == (child_count - 1)
            self.pprint_tree(child, _prefix, _last)

    def print_opened_list(self):
        print("Lista de Abertos: ")
        for i in self.opened_list:
            print("{}({})".format(i.get_position(), i.get_total_cost()), end="  ")
        print("\n")

    def print_closed_list(self):
        print("Lista de Fechados: ")
        for j in self.closed_list:
            print("{}({})".format(j.get_position(), j.get_total_cost()), end="  ")
        print("\n")

    def print_fluxograma(self):
        print("------------ Fluxograma ---------------")
        self.print_opened_list()
        self.print_closed_list()
        print("Arvore Atual")
        self.pprint_tree(self.root_node, "", True)
        print("\n\n")

    def maze_solution(self):
        maze = self.maze.get_maze()
        for i in self.success_way:
            maze[i[0]][i[1]] = '*'
        for i in maze:
            for j in i:
                print(j, end=' ')
            print()