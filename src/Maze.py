from src.Node import Node
import csv


class Maze:

    def __init__(self, file_path):
        self.start = None
        self.ending = None
        self.counter = 2
        self.maze = []
        self.width = 0
        self.height = 0
        self.file_path = file_path

    def create_maze(self):
        file = open(self.file_path, "r")
        if file.mode == 'r':
            h = 0
            for i in file:
                i = i.split(',')
                i.pop(-1)
                if 'O' in i:                                    # Indica o começo do labirinto
                    self.start = Node(0, [h, i.index('O')])
                elif 'X' in i:                                  # Indica o final do labirinto
                    self.ending = Node(1, [h, i.index('X')])
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
