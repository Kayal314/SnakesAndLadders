import random


class Player:
    def __init__(self, image, rank):
        self.pos_x = 60
        self.pos_y = 560
        self.image = image
        self.board_pos = 0
        self.rank = rank
        if rank == 1:
            self.shift = 4
            self.pos_x += self.shift
        elif rank == 2:
            self.shift = -4
            self.pos_x += self.shift

    def change_coordinates(self, x, y):
        self.pos_x = x + self.shift
        self.pos_y = y

    def reset(self):
        self.pos_x = 60 + self.shift
        self.pos_y = 560
        self.board_pos = 0

    @staticmethod
    def roll_dice():
        return random.randrange(1, 7)
