from flask import Flask, render_template, request
from game_of_life import GameOfLife

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/live/', methods=['GET', 'POST'])
def live():
    game = GameOfLife()

    width = int(request.form.get('width', 10))
    height = int(request.form.get('height', 10))

    if len(game.world[0]) != width or len(game.world) != height and (width > 0 and height > 0):
        game = GameOfLife(width=width, height=height)

    if game.counter > 0:
        game.form_new_generation()

    game.counter += 1

    return render_template('live.html', game=game)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
