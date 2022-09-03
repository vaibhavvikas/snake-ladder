from typing import Dict
from snake_ladder.models.board import Board
from snake_ladder.models.player import Player
from snake_ladder.models.dice import Dice
import sys


class Game:
    def __init__(self, dice_faces, board_size):
        self.dice = Dice(dice_faces)
        self.board = Board(board_size)
        self.players = {}
        self.winners = []
        self.active_players = 0

    def set_players(self, players):
        self.active_players = len(players)

        if self.active_players < 2:
            raise Exception("Not enough Players!")

        for player in players:
            self.players[player] = Player(player)

    def set_snake_ladders(self, snakes, ladders):
        for snake in snakes:
            try:
                self.board.set_snakes(snake)
            except:
                continue

        for ladder in ladders:
            try:
                self.board.set_ladder(ladder)
            except:
                continue
    
    def add_winner(self, winner):
        self.winners.append(winner)

    def play_game(self):
        while True:
            for _, player in self.players.items():
                if not player.get_win_status():
                    if self.board.check_player_status(player.get_position()):
                        player.set_win_status()
                        self.add_winner(player.name)
                        self.active_players -= 1

                if self.active_players < 2:
                    print("Game Over")
                    sys.exit()
