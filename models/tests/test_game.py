import unittest
from src.game import Game
from src.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        
        self.rock = Player("Ron", "Rock")
        self.paper = Player("Neville", "Paper")
        self.scissors = Player("Shuffle", "Scissors")

    def test_result_1(self):
        rock_wins = Game.decide_winner(self.rock, self.scissors)
        self.assertEqual(self.rock, rock_wins)

    def test_result_2(self):
        draw = Game.decide_winner(self.rock, self.rock)
        self.assertEqual("draw", draw)

    def test_result_3(self):
        paper_wins = Game.decide_winner(self.paper, self.rock)
        self.assertEqual(self.paper, paper_wins)   