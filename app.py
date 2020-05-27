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
        WHERE type='table' AND name <> 'sqlite_sequence'
        ORDER BY name;
        '''
    )
    lista = results.fetchall()
    x = []
    for i in lista:
        x.append(i[0])
    bib.Close()
    return render_template("biblioteca.html", x=x)
    

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

@app.route("/create-biblio")
def createBiblio():
    return render_template("create-biblio.html")

@app.route("/create-biblio/result", methods=["POST"])
def createBiblioResult():
    result = request.form['Nueva_biblio']
    db = DB_Biblioteca()
    result = db.Create_Biblio(result)
    if result == "La biblioteca se creo exitosamente":
        return render_template("Create-biblio-success.html")
    else:
        return render_template("error.html", result = result)

@app.route("/biblioteca/<biblio>")
def showBiblioteca(biblio):
    db = DB_Biblioteca()
    bibliotecas = db.Show_juego(biblio)
    if type(bibliotecas) == list:
        return render_template("biblioteca-result.html", bibliotecas = bibliotecas, nombre = biblio)
    else:
        error = True
        return render_template("biblioteca-result.html", bibliotecas = bibliotecas, nombre = biblio, error = error)
    
    
if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
    