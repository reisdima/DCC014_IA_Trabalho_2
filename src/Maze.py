from src.Node import Node
import csv


class Maze:

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
             '#, , , , , , , , , , , , , ,#,',
             '#, ,#,#,#,#,#,#,#,#,#,#,#,#,#,',
             '#, , , , , , , , , , , , ,#,#,',
             '#, ,#,#,#,#,#,#,#,#,#,#,#,#,#,',
             '#, ,#, , , , , , , , , , ,#,#,',
             '#, ,#,#,#, ,#,#,#,#, , , ,#,#,',
             '#, , , ,#, ,#,#,#,#, , , ,#,#,',
             '#, ,#, ,#, ,#, , , , , , , ,#,',
             '#,#,#, ,#, ,#, ,#,#,#,#,#,#,#,',
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

    def __init__(self, file_path, maze_number):
        self.start = None
        self.ending = None
        self.counter = 2
        self.maze = []
        self.width = 0
        self.height = 0
        self.file_path = file_path
        self.maze_number = maze_number

    def create_maze(self):
        if self.maze_number == -1:
            return self.create_maze_from_file()
        return self.create_predefined_maze(self.maze_number)

    def create_maze_from_file(self):
        file = open(self.file_path, "r")
        if file.mode == 'r':
            h = 0
            for i in file:
                i = i.split(',')
                i.pop(-1)
                if 'O' in i:  # Indica o  X, Y do começo do labirinto
                    # self.start = Node([h, i.index('O'), None])
                    self.start = [h, i.index('O')]
                elif 'X' in i:  # Indica o X, Y do final do labirinto
                    # self.ending = Node(1, [h, i.index('X')])
                    self.ending = [h, i.index('X')]
                self.maze.append(i)
                h += 1
            if self.start is None or self.ending is None:
                return False
            self.width = len(self.maze[0])
            self.height = h
            return True

    def create_predefined_maze(self, maze_number):
        maze = self.mazes[maze_number]
        h = 0
        for i in maze:
            i = i.split(',')
            i.pop(-1)
            if 'O' in i:  # Indica o  X, Y do começo do labirinto
                # self.start = Node([h, i.index('O'), None])
                self.start = [h, i.index('O')]
            elif 'X' in i:  # Indica o X, Y do final do labirinto
                # self.ending = Node(1, [h, i.index('X')])
                self.ending = [h, i.index('X')]
            self.maze.append(i)
            h += 1
        if self.start is None or self.ending is None:
            return False
        self.width = len(self.maze[0])
        self.height = h
        return True

    def get_start(self):
        return self.start

    def get_ending(self):
        return self.ending

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_info_position(self, position):
        return self.maze[position[0]][position[1]]

    def get_maze(self):
        return self.maze

    def print_mazes(self):
        for i in self.mazes:
            for j in i:
                print(j)

