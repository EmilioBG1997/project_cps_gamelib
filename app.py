from flask import Flask, render_template
from DB_biblio import *
from juego import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")