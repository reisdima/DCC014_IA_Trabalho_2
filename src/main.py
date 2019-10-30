from src.Maze import Maze
from src.Ordered_search import OrderedSearch
from src.Heuristic_Search import HeuristicSearch
from src.A_star import AStar

file = r"C:\Users\Adriana\Desktop\IA\DCC014_IA_Trabalho_2\teste"
busca = HeuristicSearch(file)
busca.start_search()
# maze = Maze(file)
# maze.create_maze_from_file()
# for i in maze.maze:
#     print(i)
#
# print(maze.height, maze.width)
