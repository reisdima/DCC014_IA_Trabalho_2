class Player:

    def __init__(self, position):
        self.position  = position
        self.moves = [self.move_down, self.move_left, self.move_up, self.move_right]

    def move_right(self):
        new_position = self.add([0, 1])
        return new_position

    def move_left(self):
        new_position = self.add([0, -1])
        return new_position

    def move_up(self):
        new_position = self.add([-1, 0])
        return new_position

    def move_down(self):
        new_position = self.add([1, 0])
        return new_position

    def add(self, movement):
        for i in range(len(movement)):
            movement[i] = movement[i] + self.position[i]
        return movement

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def get_moves(self):
        return self.moves