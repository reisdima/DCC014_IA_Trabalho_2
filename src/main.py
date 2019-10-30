from src.Maze import Maze
from src.Ordered_search import OrderedSearch

file = "/home/caio/Workspaces/python_workspace/DCC014_IA_Trabalho_2/teste"
busca = OrderedSearch(file)
busca.start_search()
# maze = Maze(file)
# maze.create_maze_from_file()
# for i in maze.maze:
#     print(i)
#
# print(maze.height, maze.width)
