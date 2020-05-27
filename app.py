from flask import Flask, render_template,request
from DB_biblio import *
from juego import *
import ast

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/juegos')
def juegos():
    return render_template('juegos.html')

@app.route('/resultado', methods=['POST'])
def get_juego():
    try:
        game = request.form['search']
        rawg = rawg_juego()
        game = build_juego(rawg, game)
        data = game.get_everything()
        return render_template("resultados.html", data = data)
    except:
        return render_template("error.html")

@app.route('/biblioteca')
def get_biblio_list():
    bib = DB_Biblioteca()
    results = bib.cursor.execute(
        '''
        SELECT name FROM sqlite_master
        WHERE type='table'
        ORDER BY name;
        '''
    )
    lista = results.fetchall()
    x = ""
    for i in lista:
        x+=f"nombre: {i} \n"
    bib.Close()
    return x
    

@app.route('/data-add',methods=['POST'])
def add():
    try:
        game = ast.literal_eval(request.form['juego'])
        table = request.form['table']
        db = DB_Biblioteca()
        
        try:
            db.Create_Biblio(table)
        
        except:
            return render_template("error.html")
        
        try:
            db.Add_juego(game,table)
        
        except:
            return render_template("error.html")
        
        return render_template('data-add.html', dict=game)

    except:
        return render_template("error.html")


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
    