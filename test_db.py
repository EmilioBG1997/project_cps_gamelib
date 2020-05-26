import unittest
from unittest.mock import MagicMock
from DB_biblio import *
import os

class test_DB(unittest.TestCase):
######################################################### SETUP & TIERDOWN #########################################################     
    def setUp(self):
        self.db = DB_Biblioteca()
        self.db.Create_Biblio("Aventura")
        self.db.Create_Biblio("Estrategia")
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
        self.db.Add_juego(juego,"Aventura")

    def tearDown(self):
        self.db.Close()
        os.remove("Bibliotecas.db")
######################################################### TEST MOCK CREACION BIBLIOTECA #########################################################     
    def testCreateTables(self):
        testCases=[
            {
                "in": "Shooters",
                "ex": "La biblioteca se creo exitosamente"
            },
            {
                "in": "Accion",
                "ex": "La biblioteca se creo exitosamente"
            },
            {
                "in": 123456789,
                "ex":'Error: Ingrese un valor de tipo String'
            },
            {
                "in":True,
                "ex": 'Error: Ingrese un valor de tipo String'
            },
            {
                "in":"MEJORES JUEGOS",
                "ex": "Error: Remplace los espacios por guiones bajos"
            }
        ]

        for tc in testCases:
            dbMock = MagicMock()
            dbMock.Create_Biblio.return_value = tc['ex']
            real = addBiblio(dbMock,tc['in'])
            self.assertEqual(tc["ex"],real)
######################################################### TEST INTEGRACION CREACION BIBLIOTECA #########################################################     

    def testIntegrationCreateTables(self):
        testCases=[
            {
                "in": "Shooters",
                "ex": "La biblioteca se creo exitosamente"
            },
            {
                "in": "Accion",
                "ex": "La biblioteca se creo exitosamente"
            },
            {
                "in": 123456789,
                "ex":'Error: Ingrese un valor de tipo String'
            },
            {
                "in":True,
                "ex": 'Error: Ingrese un valor de tipo String'
            },
            {
                "in":"MEJORES JUEGOS",
                "ex": "Error: Remplace los espacios por guiones bajos"
            }
        ]
        for tc in testCases:
            real = self.db.Create_Biblio(tc["in"])
            self.assertEqual(tc["ex"],real)
######################################################### TEST MOCK AGREGAR JUEGO A BIBLIOTECA#########################################################     

    def testAddJuego(self):
        testCases = [
            {
                "inGame":{
                    'name': 'The Legend of Zelda: Ocarina of Time', 
                    'desc': "The Legend of Zelda™: Ocarina of Time™ – one of the most critically\nacclaimed games ever made –returns on the Nintendo eShop for Wii U™. Set\noff on a legendary journey to stop Ganondorf, who has plunged Hyrule\ninto darkness. Travel through time as child and adult Link™ and\nexperience Hyrule in peace and war to save the world and protect the\nTriforce.\n\nYour quest takes you through dense forests and across wind-whipped\ndeserts. Swim raging rivers, climb treacherous mountains, dash on\nhorseback across rolling hills, and delve into dungeons full of\ncreatures that fight to the finish to put an end to your adventures. As\nLink, you'll also travel through time to solve puzzles, save friends,\nand right Ganondorf's wrongs with the help from your trusty Ocarina of\nTime and the mysterious youth, Sheik. The Legend of Zelda: Ocarina of\nTime is one of Nintendo's most epic challenges ever and one of its most\ntouching stories, and is an absolute must-play for Nintendo fans.\nThis classic game is part of the Virtual Console service, which brings you great games created for consoles such as NES™, Super NES™ and Game Boy™ Advance. We hope you'll enjoy the new features (including off-TV play) that have been added to this title. See more Virtual Console games for Wii U.", 
                    'rating': 4.37, 
                    'fecha': '1998-11-21', 
                    'picture': 'https://media.rawg.io/media/games/3a0/3a0c8e9ed3a711c542218831b893a0fa.jpg', 
                    'platforms': ['GameCube', 'Wii', 'Nintendo 64', 'Wii U'], 
                    'devs': ['Nintendo'], 
                    'genres': ['Action', 'Adventure', 'RPG'], 
                    'esrb': 'Everyone'
                },
                "inBiblio": "Aventura",
                "ex": "El juego ya existe en la biblioteca"
            },
            {
                "inGame": {
                    'name': 'Grand Theft Auto V', 
                    'desc': 'Rockstar Games went bigger, since their previous installment of the series. You get the complicated and realistic world-building from Liberty City of GTA4 in the setting of lively and diverse Los Santos, from an old fan favorite GTA San Andreas. 561 different vehicles (including every transport you can operate) and the amount is rising with every update. \r\nSimultaneous storytelling from three unique perspectives: \r\nFollow Michael, ex-criminal living his life of leisure away from the past, Franklin, a kid that seeks the better future, and Trevor, the exact past Michael is trying to run away from. \r\nGTA Online will provide a lot of additional challenge even for the experienced players, coming fresh from the story mode. Now you will have other players around that can help you just as likely as ruin your mission. Every GTA mechanic up to date can be experienced by players through the unique customizable character, and community content paired with the leveling system tends to keep everyone busy and engaged.', 
                    'rating': 4.48, 
                    'fecha': '2013-09-17', 
                    'picture': 'https://media.rawg.io/media/games/b11/b115b2bc6a5957a917bc7601f4abdda2.jpg', 
                    'platforms': ['PC', 'PlayStation 4', 'PlayStation 3', 'Xbox 360', 'Xbox One'], 
                    'devs': ['Rockstar North'], 
                    'genres': ['Action', 'Adventure'],
                    'esrb': 'Mature'
                },
                "inBiblio": "Accion",
                "ex": "La biblioteca no existe"
            },
            {
                "inGame": {
                    'name': 'Grand Theft Auto V', 
                    'desc': 'Rockstar Games went bigger, since their previous installment of the series. You get the complicated and realistic world-building from Liberty City of GTA4 in the setting of lively and diverse Los Santos, from an old fan favorite GTA San Andreas. 561 different vehicles (including every transport you can operate) and the amount is rising with every update. \r\nSimultaneous storytelling from three unique perspectives: \r\nFollow Michael, ex-criminal living his life of leisure away from the past, Franklin, a kid that seeks the better future, and Trevor, the exact past Michael is trying to run away from. \r\nGTA Online will provide a lot of additional challenge even for the experienced players, coming fresh from the story mode. Now you will have other players around that can help you just as likely as ruin your mission. Every GTA mechanic up to date can be experienced by players through the unique customizable character, and community content paired with the leveling system tends to keep everyone busy and engaged.', 
                    'rating': 4.48, 
                    'fecha': '2013-09-17', 
                    'picture': 'https://media.rawg.io/media/games/b11/b115b2bc6a5957a917bc7601f4abdda2.jpg', 
                    'platforms': ['PC', 'PlayStation 4', 'PlayStation 3', 'Xbox 360', 'Xbox One'], 
                    'devs': ['Rockstar North'], 
                    'genres': ['Action', 'Adventure'],
                    'esrb': 'Mature'
                },
                "inBiblio": "Aventura",
                "ex": "Juego agregado a biblioteca"
            },
            {
                "inGame": "GTA V",
                "inBiblio": "Aventura",
                "ex": 'Error: Ingrese valor "juego" de tipo dict'
            },
            {
                "inGame": 123456789,
                "inBiblio": "Aventura",
                "ex": 'Error: Ingrese valor "juego" de tipo dict'
            },
            {
                "inGame": True,
                "inBiblio": "Aventura",
                "ex": 'Error: Ingrese valor "juego" de tipo dict'
            },
            {
                "inGame": {
                    'name': 'Grand Theft Auto V', 
                    'desc': 'Rockstar Games went bigger, since their previous installment of the series. You get the complicated and realistic world-building from Liberty City of GTA4 in the setting of lively and diverse Los Santos, from an old fan favorite GTA San Andreas. 561 different vehicles (including every transport you can operate) and the amount is rising with every update. \r\nSimultaneous storytelling from three unique perspectives: \r\nFollow Michael, ex-criminal living his life of leisure away from the past, Franklin, a kid that seeks the better future, and Trevor, the exact past Michael is trying to run away from. \r\nGTA Online will provide a lot of additional challenge even for the experienced players, coming fresh from the story mode. Now you will have other players around that can help you just as likely as ruin your mission. Every GTA mechanic up to date can be experienced by players through the unique customizable character, and community content paired with the leveling system tends to keep everyone busy and engaged.', 
                    'rating': 4.48, 
                    'fecha': '2013-09-17', 
                    'picture': 'https://media.rawg.io/media/games/b11/b115b2bc6a5957a917bc7601f4abdda2.jpg', 
                    'platforms': ['PC', 'PlayStation 4', 'PlayStation 3', 'Xbox 360', 'Xbox One'], 
                    'devs': ['Rockstar North'], 
                    'genres': ['Action', 'Adventure'],
                    'esrb': 'Mature'
                },
                "inBiblio": 123456789,
                "ex":'Error: Ingrese valor "biblioteca" de tipo string'
            },
            {
                "inGame": {
                    'name': 'Grand Theft Auto V', 
                    'desc': 'Rockstar Games went bigger, since their previous installment of the series. You get the complicated and realistic world-building from Liberty City of GTA4 in the setting of lively and diverse Los Santos, from an old fan favorite GTA San Andreas. 561 different vehicles (including every transport you can operate) and the amount is rising with every update. \r\nSimultaneous storytelling from three unique perspectives: \r\nFollow Michael, ex-criminal living his life of leisure away from the past, Franklin, a kid that seeks the better future, and Trevor, the exact past Michael is trying to run away from. \r\nGTA Online will provide a lot of additional challenge even for the experienced players, coming fresh from the story mode. Now you will have other players around that can help you just as likely as ruin your mission. Every GTA mechanic up to date can be experienced by players through the unique customizable character, and community content paired with the leveling system tends to keep everyone busy and engaged.', 
                    'rating': 4.48, 
                    'fecha': '2013-09-17', 
                    'picture': 'https://media.rawg.io/media/games/b11/b115b2bc6a5957a917bc7601f4abdda2.jpg', 
                    'platforms': ['PC', 'PlayStation 4', 'PlayStation 3', 'Xbox 360', 'Xbox One'], 
                    'devs': ['Rockstar North'], 
                    'genres': ['Action', 'Adventure'],
                    'esrb': 'Mature'
                },
                "inBiblio": True,
                "ex":'Error: Ingrese valor "biblioteca" de tipo string'
            }
        ]

        for tc in testCases:
            gameMock = MagicMock()
            gameMock.Add_juego.return_value = tc["ex"]
            real = addGame(gameMock,tc["inGame"],tc["inBiblio"])
            self.assertEqual(real,tc["ex"])

######################################################### TEST INTEGRACION AGREGAR JUEGO #########################################################     
    def testIntegrationAddJuego(self):
        testCases = [
            {
                "inGame":{
                    'name': 'The Legend of Zelda: Ocarina of Time', 
                    'desc': "The Legend of Zelda™: Ocarina of Time™ – one of the most critically\nacclaimed games ever made –returns on the Nintendo eShop for Wii U™. Set\noff on a legendary journey to stop Ganondorf, who has plunged Hyrule\ninto darkness. Travel through time as child and adult Link™ and\nexperience Hyrule in peace and war to save the world and protect the\nTriforce.\n\nYour quest takes you through dense forests and across wind-whipped\ndeserts. Swim raging rivers, climb treacherous mountains, dash on\nhorseback across rolling hills, and delve into dungeons full of\ncreatures that fight to the finish to put an end to your adventures. As\nLink, you'll also travel through time to solve puzzles, save friends,\nand right Ganondorf's wrongs with the help from your trusty Ocarina of\nTime and the mysterious youth, Sheik. The Legend of Zelda: Ocarina of\nTime is one of Nintendo's most epic challenges ever and one of its most\ntouching stories, and is an absolute must-play for Nintendo fans.\nThis classic game is part of the Virtual Console service, which brings you great games created for consoles such as NES™, Super NES™ and Game Boy™ Advance. We hope you'll enjoy the new features (including off-TV play) that have been added to this title. See more Virtual Console games for Wii U.", 
                    'rating': 4.37, 
                    'fecha': '1998-11-21', 
                    'picture': 'https://media.rawg.io/media/games/3a0/3a0c8e9ed3a711c542218831b893a0fa.jpg', 
                    'platforms': ['GameCube', 'Wii', 'Nintendo 64', 'Wii U'], 
                    'devs': ['Nintendo'], 
                    'genres': ['Action', 'Adventure', 'RPG'], 
                    'esrb': 'Everyone'
                },
                "inBiblio": "Aventura",
                "ex": "El juego ya existe en la biblioteca"
            },
            {
                "inGame": {
                    'name': 'Grand Theft Auto V', 
                    'desc': 'Rockstar Games went bigger, since their previous installment of the series. You get the complicated and realistic world-building from Liberty City of GTA4 in the setting of lively and diverse Los Santos, from an old fan favorite GTA San Andreas. 561 different vehicles (including every transport you can operate) and the amount is rising with every update. \r\nSimultaneous storytelling from three unique perspectives: \r\nFollow Michael, ex-criminal living his life of leisure away from the past, Franklin, a kid that seeks the better future, and Trevor, the exact past Michael is trying to run away from. \r\nGTA Online will provide a lot of additional challenge even for the experienced players, coming fresh from the story mode. Now you will have other players around that can help you just as likely as ruin your mission. Every GTA mechanic up to date can be experienced by players through the unique customizable character, and community content paired with the leveling system tends to keep everyone busy and engaged.', 
                    'rating': 4.48, 
                    'fecha': '2013-09-17', 
                    'picture': 'https://media.rawg.io/media/games/b11/b115b2bc6a5957a917bc7601f4abdda2.jpg', 
                    'platforms': ['PC', 'PlayStation 4', 'PlayStation 3', 'Xbox 360', 'Xbox One'], 
                    'devs': ['Rockstar North'], 
                    'genres': ['Action', 'Adventure'],
                    'esrb': 'Mature'
                },
                "inBiblio": "Accion",
                "ex": "La biblioteca no existe"
            },
            {
                "inGame": {
                    'name': 'Grand Theft Auto V', 
                    'desc': 'Rockstar Games went bigger, since their previous installment of the series. You get the complicated and realistic world-building from Liberty City of GTA4 in the setting of lively and diverse Los Santos, from an old fan favorite GTA San Andreas. 561 different vehicles (including every transport you can operate) and the amount is rising with every update. \r\nSimultaneous storytelling from three unique perspectives: \r\nFollow Michael, ex-criminal living his life of leisure away from the past, Franklin, a kid that seeks the better future, and Trevor, the exact past Michael is trying to run away from. \r\nGTA Online will provide a lot of additional challenge even for the experienced players, coming fresh from the story mode. Now you will have other players around that can help you just as likely as ruin your mission. Every GTA mechanic up to date can be experienced by players through the unique customizable character, and community content paired with the leveling system tends to keep everyone busy and engaged.', 
                    'rating': 4.48, 
                    'fecha': '2013-09-17', 
                    'picture': 'https://media.rawg.io/media/games/b11/b115b2bc6a5957a917bc7601f4abdda2.jpg', 
                    'platforms': ['PC', 'PlayStation 4', 'PlayStation 3', 'Xbox 360', 'Xbox One'], 
                    'devs': ['Rockstar North'], 
                    'genres': ['Action', 'Adventure'],
                    'esrb': 'Mature'
                },
                "inBiblio": "Aventura",
                "ex": "Juego agregado a biblioteca"
            },
            {
                "inGame": "GTA V",
                "inBiblio": "Aventura",
                "ex": 'Error: Ingrese valor "juego" de tipo dict'
            },
            {
                "inGame": 123456789,
                "inBiblio": "Aventura",
                "ex": 'Error: Ingrese valor "juego" de tipo dict'
            },
            {
                "inGame": True,
                "inBiblio": "Aventura",
                "ex": 'Error: Ingrese valor "juego" de tipo dict'
            },
            {
                "inGame": {
                    'name': 'Grand Theft Auto V', 
                    'desc': 'Rockstar Games went bigger, since their previous installment of the series. You get the complicated and realistic world-building from Liberty City of GTA4 in the setting of lively and diverse Los Santos, from an old fan favorite GTA San Andreas. 561 different vehicles (including every transport you can operate) and the amount is rising with every update. \r\nSimultaneous storytelling from three unique perspectives: \r\nFollow Michael, ex-criminal living his life of leisure away from the past, Franklin, a kid that seeks the better future, and Trevor, the exact past Michael is trying to run away from. \r\nGTA Online will provide a lot of additional challenge even for the experienced players, coming fresh from the story mode. Now you will have other players around that can help you just as likely as ruin your mission. Every GTA mechanic up to date can be experienced by players through the unique customizable character, and community content paired with the leveling system tends to keep everyone busy and engaged.', 
                    'rating': 4.48, 
                    'fecha': '2013-09-17', 
                    'picture': 'https://media.rawg.io/media/games/b11/b115b2bc6a5957a917bc7601f4abdda2.jpg', 
                    'platforms': ['PC', 'PlayStation 4', 'PlayStation 3', 'Xbox 360', 'Xbox One'], 
                    'devs': ['Rockstar North'], 
                    'genres': ['Action', 'Adventure'],
                    'esrb': 'Mature'
                },
                "inBiblio": 123456789,
                "ex":'Error: Ingrese valor "biblioteca" de tipo string'
            },
            {
                "inGame": {
                    'name': 'Grand Theft Auto V', 
                    'desc': 'Rockstar Games went bigger, since their previous installment of the series. You get the complicated and realistic world-building from Liberty City of GTA4 in the setting of lively and diverse Los Santos, from an old fan favorite GTA San Andreas. 561 different vehicles (including every transport you can operate) and the amount is rising with every update. \r\nSimultaneous storytelling from three unique perspectives: \r\nFollow Michael, ex-criminal living his life of leisure away from the past, Franklin, a kid that seeks the better future, and Trevor, the exact past Michael is trying to run away from. \r\nGTA Online will provide a lot of additional challenge even for the experienced players, coming fresh from the story mode. Now you will have other players around that can help you just as likely as ruin your mission. Every GTA mechanic up to date can be experienced by players through the unique customizable character, and community content paired with the leveling system tends to keep everyone busy and engaged.', 
                    'rating': 4.48, 
                    'fecha': '2013-09-17', 
                    'picture': 'https://media.rawg.io/media/games/b11/b115b2bc6a5957a917bc7601f4abdda2.jpg', 
                    'platforms': ['PC', 'PlayStation 4', 'PlayStation 3', 'Xbox 360', 'Xbox One'], 
                    'devs': ['Rockstar North'], 
                    'genres': ['Action', 'Adventure'],
                    'esrb': 'Mature'
                },
                "inBiblio": True,
                "ex":'Error: Ingrese valor "biblioteca" de tipo string'
            }
        ]
        for tc in testCases:
            real = self.db.Add_juego(tc["inGame"],tc["inBiblio"])
            self.assertEqual(real,tc["ex"])
######################################################### TEST MOCK REMOVER JUEGO DE BIBLIOTECA #########################################################     
    def testRemoveJuego(self):
        testCases = [
            {
                "inGame":"The legend of zelda ocarina of time",
                "inBiblio":"Aventura",
                "ex": "El juego ha sido eliminado de biblioteca: Aventura con exito"
            },
            {
                "inGame":"The legend of zelda ocarina of time",
                "inBiblio":"Shooter",
                "ex": "La biblioteca: Shooter no Existe"
            },
            {
                "inGame": "Grand theft auto V",
                "inBiblio": "Aventura",
                "ex": "El juego no existe en la biblioteca: Aventura"
            },
            {
                "inGame": True,
                "inBiblio": "Aventura",
                "ex": 'Error: Ingrese valor "juego" de tipo string'
            },
            {
                "inGame": 123456789,
                "inBiblio": "Aventura",
                "ex": 'Error: Ingrese valor "juego" de tipo string'
            }
        ]
        for tc in testCases:
            rmMock = MagicMock()
            rmMock.Remove_juego.return_value = tc["ex"]
            real = removeGame(rmMock,tc["inGame"],tc["inBiblio"])
            self.assertEqual(real,tc["ex"])

######################################################### TEST INTEGRACION REMOVER JUEGO DE BIBLIOTECA #########################################################     
    def testIntegrationRemoveJuego(self):
        testCases = [
            {
                "inGame":"The Legend of Zelda: Ocarina of Time",
                "inBiblio":"Aventura",
                "ex": "El juego ha sido eliminado de biblioteca: Aventura con exito"
            },
            {
                "inGame":"The Legend of zelda - ocarina of time",
                "inBiblio": "Aventura",
                "ex": "El juego no existe en la biblioteca: Aventura"
            },
            {
                "inGame":"The legend of zelda ocarina of time",
                "inBiblio":"Shooter",
                "ex": "La biblioteca: Shooter no Existe"
            },
            {
                "inGame": "Grand theft auto V",
                "inBiblio": "Aventura",
                "ex": "El juego no existe en la biblioteca: Aventura"
            },
            {
                "inGame": True,
                "inBiblio": "Aventura",
                "ex": 'Error: Ingrese valor "juego" de tipo string'
            },
            {
                "inGame": 123456789,
                "inBiblio": "Aventura",
                "ex": 'Error: Ingrese valor "juego" de tipo string'
            }
        ]
        for tc in testCases:
            real = self.db.Remove_juego(tc["inGame"],tc["inBiblio"])
            self.assertEqual(tc["ex"],real)
######################################################### TEST MOCK MOSTRAR JUEGOS DE BIBLIOTECA #########################################################     
    def  testShowJuego(self):
        testCases = [
            {
                "inBiblio": "Aventura",
                "ex": ["The Legend of Zelda: Ocarina of Time"]
            },
            {    
                "inBiblio": "Shooter",
                "ex": "La biblioteca: Shooter no existe"
            },
            {
                "inBiblio": "Estrategia",
                "ex": "La biblioteca: Estrategia esta vacia"
            },
            {
                "inBiblio": 123456789,
                "ex": 'Error: Ingrese un valor de tipo String'
            },
            {
                "inBiblio": True,
                "ex": 'Error: Ingrese un valor de tipo String'
            }
        ]
        for tc in testCases:
            shMock = MagicMock()
            shMock.Show_juego.return_value = tc["ex"]
            real = showGames(shMock,tc["inBiblio"])
            self.assertEqual(real,tc["ex"])
    
######################################################### TEST INTEGRACION MOSTRAR JUEGOS DE BIBLIOTECA #########################################################     
    def  testIntegrationShowJuego(self):
        testCases = [
            {
                "inBiblio": "Aventura",
                "ex": ["The Legend of Zelda: Ocarina of Time"]
            },
            {    
                "inBiblio": "Shooter",
                "ex": "La biblioteca: Shooter no existe"
            },
            {
                "inBiblio": "Estrategia",
                "ex": "La biblioteca: Estrategia esta vacia"
            },
            {
                "inBiblio": 123456789,
                "ex": 'Error: Ingrese un valor de tipo String'
            },
            {
                "inBiblio": True,
                "ex": 'Error: Ingrese un valor de tipo String'
            }
        ]
        for tc in testCases:
            real = self.db.Show_juego(tc['inBiblio'])
            self.assertEqual(real, tc["ex"])

if __name__ == '__main__':
    unittest.main()