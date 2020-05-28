from flask import Flask, render_template,request
from DB_biblio import *
from juego import *
import ast

app = Flask(__name__)

@app.route('/') ##Pagina principal
def index():
    return render_template("index.html")

@app.route('/juegos') ##Pagina Busqueda de Juegos
def juegos():
    return render_template('juegos.html')

@app.route('/resultado', methods=['POST']) ##Pagina Resultado busqueda del juego
def get_juego():
    try:
        game = request.form['search']
        rawg = rawg_juego()
        game = build_juego(rawg, game)
        data = game.get_everything()

        db = DB_Biblioteca()
        res = db.cursor.execute(
        '''
        Select name FROM sqlite_master
        Where type = 'table' and name <>
        'sqlite_sequence' ORDER by name;
        '''
        )
        
        lista = res.fetchall()
        
        x = []
        for i in lista:
            x.append(i[0])
        db.Close()

        return render_template("resultados.html", data = data, dict = x)
        
    except Exception as e:
        print(str(e))
        return render_template("error.html")

@app.route('/biblioteca') ##Pagina Lista de Bibliotecas
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
    

@app.route('/data-add',methods=['POST']) ##Pagina Exito al agregar a la base de datos
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

@app.route("/create-biblio") ##Pagina Crear Biblio
def createBiblio():
    return render_template("create-biblio.html")

@app.route("/create-biblio/result", methods=["POST"]) ##Pagina resultado de la creacion de la tabla
def createBiblioResult():
    result = request.form['Nueva_biblio']
    db = DB_Biblioteca()
    result = db.Create_Biblio(result)
    if result == "La biblioteca se creo exitosamente":
        return render_template("Create-biblio-success.html")
    else:
        return render_template("error.html", result = result)

@app.route("/biblioteca/<biblio>") ##Pagina resultados de biblioteca
def showBiblioteca(biblio):
    db = DB_Biblioteca()
    bibliotecas = db.Show_juego(biblio)
    if type(bibliotecas) == list:
        return render_template("biblioteca-result.html", bibliotecas = bibliotecas, nombre = biblio)
    else:
        error = True
        return render_template("biblioteca-result.html", bibliotecas = bibliotecas, nombre = biblio, error = error)

@app.route("/biblioteca-borrado", methods= ["POST"]) ##Pagina borrado
def deleteJuego():
    name = request.form['name']
    table = request.form['table']
    db = DB_Biblioteca()
    db.Remove_juego(name, table)
    db.Close()
    dic = {'name': name, 'table': table}
    return(render_template("borrado.html", dic = dic))

@app.route("/biblioteca/remove-biblio/<biblioteca>")
def removeBiblioteca(biblioteca):
    db = DB_Biblioteca()
    resultado = db.Remove_Biblio(biblioteca)
    return render_template("remove-biblio.html", resultado = resultado)
if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
    