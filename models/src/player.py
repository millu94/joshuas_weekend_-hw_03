import random

choices = ["Rock", "Paper", "Scissors"]
computer_choice = choices[random.randint(0, len(choices)-1)]


class Player():

    def __init__(self, name, move):
        self.name = name
        self.move = move

