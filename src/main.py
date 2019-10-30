from src.Maze import Maze

file = "/home/caio/Workspaces/python_workspace/DCC014_IA_Trabalho_2/teste"
maze = Maze(file)
maze.create_maze_from_file()
for i in maze.maze:
    print(i)

print(maze.height, maze.width)