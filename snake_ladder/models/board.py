from snake_ladder.models.ladder import Ladder
from snake_ladder.models.snake import Snake


class Board:

    def __init__(self, size):
        self.board = {}
        self.size = size

    def set_snakes(self, snake):
        if snake[0] in self.board:
            raise Exception("The place is already occupied")
        self.board[snake[0]] = ("snake", Snake(snake[0], snake[1]))

    def set_ladder(self, ladder):
        if ladder[0] in self.board:
            raise Exception("The place is already occupied")
        self.board[ladder[0]] = ("ladder", Ladder(ladder[0], ladder[1]))

    def get_new_position(self, curr_pos):
        if curr_pos > self.size:
            return -1

        if curr_pos in self.board:
            if self.board[curr_pos][0] == "snake":
                curr_pos = self.board[curr_pos][1].tail
            else:
                curr_pos = self.board[curr_pos][1].end

        return curr_pos

    def check_player_status(self, pos):
        return self.size == pos
