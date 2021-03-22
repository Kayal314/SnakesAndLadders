"""
Let S be the set of points (as numbers on the board) {(a,b): the mouth of the snake lies at a and the tail lies at b}

S = {(98,79), (95,75), (93,73), (86,24) ,(64,60),
     (62,19), (54,34) ,(17,7)}

Let L be the set of points (as numbers on the board) {(a,b): the bottom of the ladder lies at a and the top lies at b}

L = {(80,100), (71,91), (28,84), (21, 42), (51,67),
     (1,38), (4,14), (9,31)}
"""


class Board:
    SNAKES = {}
    LADDERS = {}

    def __init__(self):
        Board.SNAKES = {98: 79, 95: 75, 93: 73, 86: 24, 64: 60,
                        62: 19, 54: 34, 17: 7}
        Board.LADDERS = {80: 100, 71: 91, 28: 84, 21: 42, 51: 67,
                         1: 38, 4: 14, 9: 31}

    @staticmethod
    def get_coordinates(board_pos):
        board_pos -= 1
        if int(board_pos / 10) % 2 == 1:
            x = int(board_pos / 10) + 1
            x = x * 10 - board_pos - 1
        else:
            x = board_pos % 10
        x = 120 + 60 * x
        y = int(board_pos / 10)
        y = 560 - 60 * y
        return x, y
