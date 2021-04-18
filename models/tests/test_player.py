import unittest
from src.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Neville", "Paper")

    def test_player_has_name(self):
        self.assertEqual("Neville", self.player.name)
    
    def test_player_has_gesture(self):
        self.assertEqual("Paper", self.player.move)