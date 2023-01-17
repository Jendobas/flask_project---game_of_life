from flask import Flask, render_template
from game_of_life import GameOfLife

app = Flask(__name__)


@app.route('/')
def index():
    GameOfLife(25, 25)
    return render_template('index.html')


@app.route('/live')
def live():
    gof = GameOfLife()
    if gof.counter > 0:
        gof.form_new_generation()
    gof.counter += 1
    return render_template('live.html', gof=gof)


if __name__ == '__main__':
    app.run(debug=True)
