from flask import render_template, request
from app import app
from models.src.game import Game
from models.src.player import Player, computer_choice


@app.route('/rps_home')
def index():
    return render_template('index.html', title='Home')

@app.route('/rps_home/<player_1>/<player_2>', methods=['POST'])
def play_game(player_1, player_2):
    player_1_name = request.form['name']
    player_1_move = request.form['move']
    player_1 = Player(player_1_name, player_1_move)
    player_2 = Player("Bleep-Bloop", computer_choice)
    return Game.decide_winner(player_1, player_2)

