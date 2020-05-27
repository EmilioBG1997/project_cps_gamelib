from juego import *
import unittest

class test_juego(unittest.TestCase):
    class mock_api():
        def __init__(self):
            self.url="something that does NOT matter RN"
            self.error = False
        def get_juego(self,game):
            if self.error == True:
                return -1
            game = juego(game,"adventure lonk", "5.0", "7/12/12", ["www.stockimages.com"], ["pc master race"],['EA'],['FPS','Strategy'],"A")
            return game

    def test_build_juego(self):
        tc = [
            {
                'in' : "A",
                'ex' : {
                    'name':"A",
                    'desc':'adventure lonk',
                    'rating':'5.0',
                    'fecha':"7/12/12",
                    'picture':["www.stockimages.com"],
                    'platforms':["pc master race"],
                    'devs':['EA'],
                    'genres':['FPS','Strategy'],
                    'esrb':"A",

                },
                'err': False
            },
            {
                'in' : "B",
                'ex' : {
                    'name':"B",
                    'desc':'adventure lonk',
                    'rating':'5.0',
                    'fecha':"7/12/12",
                    'picture':["www.stockimages.com"],
                    'platforms':["pc master race"],
                    'devs':['EA'],
                    'genres':['FPS','Strategy'],
                    'esrb':"A",
                },
                'err': False
            },
            {
                'in' : "C",
                'ex' : {
                    'name':"C",
                    'desc':'adventure lonk',
                    'rating':'5.0',
                    'fecha':"7/12/12",
                    'picture':["www.stockimages.com"],
                    'platforms':["pc master race"],
                    'devs':['EA'],
                    'genres':['FPS','Strategy'],
                    'esrb':"A",
                },
                'err': False
            },
            {
                'in' : "D",
                'ex' : -1,
                'err': True
            }
        ]
        api = self.mock_api()
        for i in tc:
            api.error = i['err']
            if api.error == False:
                result = build_juego(api,i['in']).get_everything()
            else:
                result = build_juego(api,i['in'])
            self.assertEqual(result,i['ex'])

    def test_build_juego_int(self):
        api = rawg_juego()
        tc=[
            {
                'in':'the legend of zelda ocarina of time',
                'ex':{
                    'name': 'The Legend of Zelda: Ocarina of Time',
                    'desc': "The Legend of Zelda™: Ocarina of Time™ – one of the most critically\nacclaimed games ever made –returns on the Nintendo eShop for Wii U™. Set\noff on a legendary journey to stop Ganondorf, who has plunged Hyrule\ninto darkness. Travel through time as child and adult Link™ and\nexperience Hyrule in peace and war to save the world and protect the\nTriforce.\n\nYour quest takes you through dense forests and across wind-whipped\ndeserts. Swim raging rivers, climb treacherous mountains, dash on\nhorseback across rolling hills, and delve into dungeons full of\ncreatures that fight to the finish to put an end to your adventures. As\nLink, you'll also travel through time to solve puzzles, save friends,\nand right Ganondorf's wrongs with the help from your trusty Ocarina of\nTime and the mysterious youth, Sheik. The Legend of Zelda: Ocarina of\nTime is one of Nintendo's most epic challenges ever and one of its most\ntouching stories, and is an absolute must-play for Nintendo fans.\nThis classic game is part of the Virtual Console service, which brings you great games created for consoles such as NES™, Super NES™ and Game Boy™ Advance. We hope you'll enjoy the new features (including off-TV play) that have been added to this title. See more Virtual Console games for Wii U.",
                    'rating': 4.36, 
                    'fecha': '1998-11-21',
                    'picture': 'https://media.rawg.io/media/games/3a0/3a0c8e9ed3a711c542218831b893a0fa.jpg',
                    'platforms': ['GameCube', 'Wii', 'Nintendo 64', 'Wii U'],
                    'devs': ['Nintendo'],
                    'genres': ['Action', 'Adventure', 'RPG'],
                    'esrb': 'Everyone'
                    }

            },
            {
                'in': 'gta v',
                'ex': {
                    'name': 'Grand Theft Auto V',
                    'desc': 'Rockstar Games went bigger, since their previous installment of the series. You get the complicated and realistic world-building from Liberty City of GTA4 in the setting of lively and diverse Los Santos, from an old fan favorite GTA San Andreas. 561 different vehicles (including every transport you can operate) and the amount is rising with every update. \r\nSimultaneous storytelling from three unique perspectives: \r\nFollow Michael, ex-criminal living his life of leisure away from the past, Franklin, a kid that seeks the better future, and Trevor, the exact past Michael is trying to run away from. \r\nGTA Online will provide a lot of additional challenge even for the experienced players, coming fresh from the story mode. Now you will have other players around that can help you just as likely as ruin your mission. Every GTA mechanic up to date can be experienced by players through the unique customizable character, and community content paired with the leveling system tends to keep everyone busy and engaged.',
                    'rating': 4.48,
                    'fecha': '2013-09-17',
                    'picture': 'https://media.rawg.io/media/games/b11/b115b2bc6a5957a917bc7601f4abdda2.jpg',
                    'platforms': ['PC', 'PlayStation 4', 'PlayStation 3', 'Xbox 360', 'Xbox One'],
                    'devs': ['Rockstar North'],
                    'genres': ['Action', 'Adventure'],
                    'esrb': 'Mature'
                 }



            },
            {
                    'in':"srlasdlkasd",
                    'ex': -1
            }
        ]
        for i in tc:
            try: #Por si llega a regresar el -1, que indica que el juego no se encontro
                actual = (build_juego(api,i['in']).get_everything())
            except: #Ya que no se pudo crear el objeto juego
                actual = build_juego(api,i['in'])
            self.assertEqual(actual,i['ex'])

if __name__=='__main__':
    unittest.main()
