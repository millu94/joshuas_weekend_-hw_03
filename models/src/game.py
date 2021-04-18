

class Game():

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def decide_winner(player_1, player_2):
        if player_1.move == "Rock" and player_2.move == "Scissors":
            return player_1
                
        if player_1.move == "Scissors" and player_2.move == "Paper":
            return player_1
                
        if player_1.move == "Paper" and player_2.move == "Rock":
            return player_1
            
        if player_1.move == player_2.move:
            return "draw"
                
        return player_2

def decide_mvp(move_1, move_2):
    if move_1 == "Rock" and move_2 == "Scissors":
        return move_1
            
    if move_1 == "Scissors" and move_2 == "Paper":
        return move_1
            
    if move_1 == "Paper" and move_2 == "Rock":
        return move_1
        
    if move_1 == move_2:
        return None
            
    return move_2