import json
from juego import *

class Biblioteca(object):
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.juegos = []
    
    def __str__(self):
        return f'''
        Biblioteca: {self.nombre},
        Juegos: {self.juegos}
        '''

if __name__ == '__main__':
    rawg =rawg_juego()
    juego = build_juego(rawg,'the legend of zelda ocarina of time')
    juego2 = build_juego(rawg,'gta 5')
    biblio = Biblioteca("Aventura")
    biblio.addJuego(juego)
    biblio.addJuego(juego2)
    print(biblio.biblio_getjuegos())
