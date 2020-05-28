from abc import abstractmethod, ABCMeta
import requests
import json
import sqlite3
######################################################### INTERFACE BASE DE DATOS #########################################################     

class DataBase(metaclass=ABCMeta):
    @abstractmethod
    def Add_juego(self):
        pass
    
    @abstractmethod
    def Create_Biblio(self):
        pass
    
    @abstractmethod
    def Remove_Biblio(self):
        pass
    
    @abstractmethod
    def Remove_juego(self):
        pass
    
    @abstractmethod
    def Show_juego(self):
        pass

######################################################### CLASE BASE DE DATOS #########################################################     
class DB_Biblioteca(DataBase):
    def __init__(self):
        self.conexion = sqlite3.connect("Bibliotecas.db")
        self.cursor = self.conexion.cursor()

    def Close(self):
        self.conexion.close()
    def Commit(self):
        self.conexion.commit()
######################################################### CREAR BIBLIOTECA #########################################################     

    def Create_Biblio(self, nombre: str):
        if type(nombre) != str:
            return 'Error: Ingrese un valor de tipo String'
        elif " " in nombre:
            return "Error: Remplace los espacios por guiones bajos"
        try:
            self.cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {nombre} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCAHR(50),
                    description  VARCHAR(1500),
                    rating FLOAT,
                    release VARCHAR (20),
                    picture VARCHAR (50),
                    platforms VARCHAR (50),
                    developers VARCHAR (50),
                    genre VARCHAR(50),
                    esrb VARCHAR(30)
                )
            ''')
            self.conexion.commit()
            return "La biblioteca se creo exitosamente"
        except:
            return "Error al crear biblioteca"

######################################################### BORRAR BIBLIOTECA #########################################################     

    def Remove_Biblio(self, nombre:str):
        if type(nombre) != str:
            return 'Error: Ingrese un valor de tipo String'
        elif " " in nombre:
            return "Error: Remplace los espacios por guiones bajos"
        try:
            self.cursor.execute(f'''
                DROP TABLE {nombre};
            ''')
            self.conexion.commit()
            return "La biblioteca se borro exitosamente"
        except:
            return "Error: la biblioteca no existe"

######################################################### AGREGAR JUEGO A BIBLIOTECA #########################################################     

    def Add_juego(self, juego: dict, nombre: str):
        if type(juego) != dict:
            return 'Error: Ingrese valor "juego" de tipo dict'
        elif type(nombre) != str:
            return 'Error: Ingrese valor "biblioteca" de tipo string'
        try:
            select = f"SELECT id FROM {nombre} WHERE name = '{juego['name']}'"
            if self.conexion.execute(select).fetchone():
                return "El juego ya existe en la biblioteca"
        except:
               return "La biblioteca no existe"
        self.cursor.execute(f'''
        INSERT INTO {nombre} (name, description, rating, release, picture, platforms, developers, genre, esrb) 
        VALUES ("{juego.get('name')}", "{juego.get('desc')}", {juego.get("rating")},"{juego.get("fecha")}","{juego.get('picture')}","{juego.get('platforms')}","{juego.get('devs')}","{juego.get('genres')}","{juego.get('esrb')}");
        ''')
        self.conexion.commit()
        return "Juego agregado a biblioteca"
    
######################################################### REMOVER JUEGO DE BIBLIOTECA #########################################################     
    
    def Remove_juego(self,juego: str,nombre:str):
        ##NOMBRE = TABLA
        ##juego = titulo
        if type(juego) != str:
            return 'Error: Ingrese valor "juego" de tipo string'
        elif type(nombre) != str:
            return 'Error: Ingrese valor "biblioteca" de tipo string'
        try:
            select = f"SELECT id from {nombre} WHERE name = '{juego}'"
            if self.conexion.execute(select).fetchone():   
                self.cursor.execute(f"DELETE FROM {nombre} WHERE NAME = '{juego}'")
                self.conexion.commit()    
                return f"El juego ha sido eliminado de biblioteca: {nombre} con exito"
            else:
                return f"El juego no existe en la biblioteca: {nombre}"
        except:
            return f"La biblioteca: {nombre} no Existe"

######################################################### REMOVER JUEGO DE BIBLIOTECA #########################################################     

    def Show_juego(self, nombre: str):
        if type(nombre) != str:
            return 'Error: Ingrese un valor de tipo String'
        try:
            lista = []
            resultados = f"SELECT NAME FROM {nombre}"
            if self.cursor.execute(resultados).fetchone():
                for resultado in self.cursor.execute(resultados).fetchall():
                    lista.append(resultado[0])
                return lista
            else:
                return f"La biblioteca: {nombre} esta vacia"
        except:
            return f"La biblioteca: {nombre} no existe"

######################################################### FUNCION MOCK CREAR BIBLIO ######################################################### 
def addBiblio(db, biblio):
    r = db.Create_Biblio(biblio)
    return r

######################################################### FUNCION MOCK CREAR BIBLIO ######################################################### 
def removeBiblio(db,biblio):
    r = db.Remove_Biblio(biblio)
    return r
######################################################### FUNCION MOCK AGREGAR JUEGO A BIBILIOTECA #########################################################     

def addGame(db, juego,biblio):
    r = db.Add_juego(juego,biblio)
    return r
######################################################### FUNCION MOCK VER JUEGOS EN BIBLIOTECA #########################################################     
def showGames(db,biblio):
    r = db.Show_juego(biblio)
    return r
######################################################### FUNCION MOCK ELIMINAR JUEGO DE BIBLIOTECA #########################################################     
def removeGame(db,juego,biblio):
    r = db.Remove_juego(juego,biblio)
    return r

if __name__ == '__main__':
    db = DB_Biblioteca()
    db.Create_Biblio("Aventura")
    juego = {
                    'name': 'The Legend of Zelda: Ocarina of Time', 
                    'desc': "The Legend of Zelda™: Ocarina of Time™ – one of the most critically\nacclaimed games ever made –returns on the Nintendo eShop for Wii U™. Set\noff on a legendary journey to stop Ganondorf, who has plunged Hyrule\ninto darkness. Travel through time as child and adult Link™ and\nexperience Hyrule in peace and war to save the world and protect the\nTriforce.\n\nYour quest takes you through dense forests and across wind-whipped\ndeserts. Swim raging rivers, climb treacherous mountains, dash on\nhorseback across rolling hills, and delve into dungeons full of\ncreatures that fight to the finish to put an end to your adventures. As\nLink, you'll also travel through time to solve puzzles, save friends,\nand right Ganondorf's wrongs with the help from your trusty Ocarina of\nTime and the mysterious youth, Sheik. The Legend of Zelda: Ocarina of\nTime is one of Nintendo's most epic challenges ever and one of its most\ntouching stories, and is an absolute must-play for Nintendo fans.\nThis classic game is part of the Virtual Console service, which brings you great games created for consoles such as NES™, Super NES™ and Game Boy™ Advance. We hope you'll enjoy the new features (including off-TV play) that have been added to this title. See more Virtual Console games for Wii U.", 
                    'rating': 4.37, 
                    'fecha': '1998-11-21', 
                    'picture': 'https://media.rawg.io/media/games/3a0/3a0c8e9ed3a711c542218831b893a0fa.jpg', 
                    'platforms': ['GameCube', 'Wii', 'Nintendo 64', 'Wii U'], 
                    'devs': ['Nintendo'], 
                    'genres': ['Action', 'Adventure', 'RPG'], 
                    'esrb': 'Everyone'
                }
    # print(db.Add_juego(juego,"Aventura"))
    print(db.Remove_Biblio("Aventura"))