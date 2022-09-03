#!/usr/bin/env python

"""Tests for `snake_ladder` package."""


import unittest
from snake_ladder.models import game
from snake_ladder.service import utils

class TestSnake_ladder(unittest.TestCase):
    """Tests for `snake_ladder` package."""

    def setUp(self):
        self.board_size = 100
        self.players = ["vaibh", "dwan"]
        self.dice_faces = 6
        self.snakes = [(87, 23), (43, 11), (98, 56), (76, 36)]
        self.ladders = [(12, 45), (40, 60), (73, 91), (62, 81)]

        self.snake_ladder_game = game.Game(self.dice_faces, self.board_size)
        self.snake_ladder_game.set_snake_ladders(self.snakes, self.ladders)
        self.snake_ladder_game.set_players(self.players)

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_add_winner(self):
        expected = ["vaibh"]
        self.snake_ladder_game.add_winner("vaibh")
        assert self.snake_ladder_game.winners == expected

    def test_dice_score(self):
        assert self.snake_ladder_game.dice.get_random_face() > 0
