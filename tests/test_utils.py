from snake_ladder.service import utils
import unittest



class TestUtils(unittest.TestCase):

    def test_player_turn_with_moves(self):
        expected = "vaibh rolled a 2 and moved from 42 to 44"
        assert utils.player_move("vaibh", 2, 42, 44) == expected

    def test_player_turn_with_no_move(self):
        expected = "vaibh rolled a 6 and but can't move from 99"
        assert utils.player_move("vaibh", 6, 99, 99) == expected
