from src.Maze import Maze
from src.Ordered_search import OrderedSearch
from src.Heuristic_Search import HeuristicSearch
from src.A_star import AStar

# MAIN BEGIN
maze1 = ['#,O,#,#,#,#,#,#,#,#,#,#,#,',
         '#, , , , , , , ,#, , , ,#,',
         '#, ,#,#,#,#,#, ,#,#,#, ,#,',
         '#, , , , , ,#, , , , , ,#,',
         '#, ,#,#,#, ,#, ,#,#,#,#,#,',
         '#, , , , , ,#, , , , ,#,#,',
         '#,#,#, ,#,#,#,#,#,#,#,#,#,',
         '#,#,#, , , , , ,#,#, ,#,#,',
         '#, ,#,#,#, ,#,#,#,#, ,#,#,',
         '#, ,#,#,#, ,#,#,#,#, ,#,#,',
         '#, , , ,#, , , , , , , ,#,',
         '#,#,#, ,#, ,#, ,#,#,#,#,#,',
         '#, , , , , ,#, , , , , ,X,',
         '#,#,#,#,#,#,#,#,#,#,#,#,#,']
maze2 = ['#,O,#,#,#,#,#,#,#,#,#,#,#,#,#,',
         '#, , , , , , , , , , , , , ,#,',
         '#,#,#,#,#,#,#,#, , ,#,#,#, ,#,',
         '#, ,#,#,#,#,#,#, , ,#,#,#,#,#,',
         '#, , , , , , , , , , , , ,#,#,',
         '#, ,#, , , , , , , , , , ,#,#,',
         '#, ,#,#,#, ,#,#,#,#, , , ,#,#,',
         '#, , , ,#, ,#,#,#,#, , , ,#,#,',
         '#, ,#, ,#, ,#, , , , , , , ,#,',
         '#, , , , , ,#, , , , , , , ,X,',
         '#,#,#,#,#,#,#,#,#,#,#,#,#,#,#,']
maze3 = ['#,#,#,#,#,#,#,',
         'O, , , ,#, ,#,',
         '#, ,#, ,#, ,#,',
         '#, ,#, , , ,#,',
         '#, ,#,#,#, ,#,',
         '#, , , , , ,#,',
         '#,#,#,#,#,X,#,']
mazes = [maze1, maze2, maze3]


def print_mazes():
    for i in range(len(mazes)):
        print('Labirinto {}:'.format(i))
        for j in mazes[i]:
            maze_aux = j.split(',')
            for k in maze_aux:
                print(k, end=' ')
            print()
        print()


file = r""
code = 3
maze_number = -1
reading_type = -1

while code != 0:
    print("\n--------------Menu-----------------\n"
          "Digite 1 para selecionar o tipo de leitura do labirinto\n"
          "Digite 2 para Busca Ordenada\n"
          "Digite 3 para Busca Gulosa (Heuristica)\n"
          "Digite 4 para Busca A*\n"
          "Digite 0 para Sair\n")
    code = int(input())
    if code == 1:
        reading_type = -1
        while reading_type != 1 and reading_type != 2:
            print("Digite 1 para ler o labirinto de um arquivo")
            print("Digite 2 para ler um labirinto pré criado")
            reading_type = int(input())
        if reading_type == 1:
            print('Digite o caminho do arquivo para leitura:')
            file = str(input())
            reading_type = -1
        else:
            file = None
            print_mazes()
            print('Selecione o labirinto (0, 1 ou 2): ')
            maze_number = int(input())
            while maze_number != 0 and maze_number != 1 and maze_number != 2:
                print('Por favor, digite um labirinto válido')
                maze_number = int(input())
    elif code == 2:
        if reading_type == 1:
            busca = OrderedSearch(file, maze_number)
            busca.start_search()
        elif reading_type == 2:
            busca = OrderedSearch(file, maze_number)
            busca.start_search()
        else:
            print("Selecione um tipo de leitura de labirinto")
    elif code == 3:
        if reading_type == 1:
            busca = HeuristicSearch(file, maze_number)
            busca.start_search()
        elif reading_type == 2:
            busca = HeuristicSearch(file, maze_number)
            busca.start_search()
        else:
            print("Selecione um tipo de leitura de labirinto")
    elif code == 4:
        if reading_type == 1:
            busca = AStar(file, maze_number)
            busca.start_search()
        elif reading_type == 2:
            busca = AStar(file, maze_number)
            busca.start_search()
        else:
            print("Selecione um tipo de leitura de labirinto")
    else:
        break

# maze = Maze(file)
# maze.create_maze_from_file()
# for i in maze.maze:
#     print(i)
#
# print(maze.height, maze.width)
