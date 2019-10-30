from src.Maze import Maze
from src.Ordered_search import OrderedSearch
from src.Heuristic_Search import HeuristicSearch
from src.A_star import AStar

# MAIN BEGIN
file = r"C:\Users\Adriana\Desktop\IA\DCC014_IA_Trabalho_2\teste"
code = 3

while code != 0:
    print("\n--------------Menu-----------------\n"
          "Digite 1 para Busca Ordenada\n"
          "Digite 2 para Busca Gulosa (Heuristica)\n"
          "Digite 3 para Busca A*\n"
          "Digite 0 para Sair\n")
    code = int(input())
    if code == 1:
        busca = OrderedSearch(file)
        busca.start_search()
    elif code == 2:
        busca = HeuristicSearch(file)
        busca.start_search()
    elif code == 3:
        busca = AStar(file)
        busca.start_search()
    else:
        break

# maze = Maze(file)
# maze.create_maze_from_file()
# for i in maze.maze:
#     print(i)
#
# print(maze.height, maze.width)
