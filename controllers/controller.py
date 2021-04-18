from flask import render_template, request
from app import app
from models.src.game import Game, decide_mvp
from models.src.player import Player, computer_choice


@app.route('/')
def mvp():
    return render_template('mvp.html', title='mvp')

@app.route('/<move_1>/<move_2>')
def mvp_result(move_1, move_2):
    result = decide_mvp(move_1, move_2)
    return render_template('mvp_result.html', title='result', result=result)

@app.route('/rps_home')
def index():
    return render_template('index.html', title='Home')

# @app.route('/rps_home/<player_1>/player_2', methods=['POST'])
# def play_game(player_1, player_2):
#     player_1_name = request.form['name']
#     player_1_move = request.form['move']
#     player_1 = Player(player_1_name, player_1_move)
#     player_2 = Player("Bleep-Bloop", computer_choice)
#     result = Game.decide_winner(player_1, player_2)
#     return render_template('result.html', title='result', result=result)









