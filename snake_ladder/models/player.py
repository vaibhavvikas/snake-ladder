from snake_ladder.models.board import Board
from snake_ladder.models.dice import Dice
from snake_ladder.service.utils import player_move

class Player:

    def __init__(self, name):
        self.name = name
        self.position = 0
        self.win_status = False

    def get_name(self):
        return self.name
    
    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def play(self, dice: Dice, board: Board):
        curr_pos = self.get_position()
        dice_face = dice.get_random_face()
        new_pos = curr_pos + dice_face
        new_pos = board.get_new_position(new_pos)
        if new_pos != -1:
            self.set_position(new_pos)
        else:
            new_pos = curr_pos
        return player_move(self.get_name(), dice_face, curr_pos, new_pos)

    def set_win_status(self):
        self.win_status = True

    def get_win_status(self):
        return self.win_status
