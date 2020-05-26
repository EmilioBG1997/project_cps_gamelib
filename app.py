from flask import Flask, render_template,request
from DB_biblio import *
from juego import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/juegos')
def juegos():
    return render_template('juegos.html')

@app.route('/resultado', methods=['POST'])
def get_juego():
    game = request.form['search']
    rawg = rawg_juego()
    game = build_juego(rawg, game)
    data = game.get_everything()
    return render_template("resultados.html", data= data)
if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
    