import unittest
from unittest.mock import MagicMock
from DB_biblio import *
import os

class test_DB(unittest.TestCase):

    def setUp(self):
        self.db = DB_Biblioteca()
        
    def tearDown(self):
        self.db.Close()
        os.remove("Bibliotecas.db")
    
    def testCreateTables(self):
        testCases=[
            {
                "in": "Aventura",
                "ex": "La Biblioteca Se creo Exitosamente"
            },
            {
                "in": "Accion",
                "ex": "La Biblioteca Se creo Exitosamente"
            },
            {
                "in": 1,
                "ex": "Error al crear Biblioteca"
            },
            {
                "in":"MEJORES JUEGOS",
                "ex": "Error al crear Biblioteca"
            }
        ]

        for tc in testCases:
            dbMock = MagicMock()
            dbMock = tc["ex"]
            real = self.db.Create_Biblio(tc['in'])
            self.assertEqual(dbMock,real)
        
if __name__ == '__main__':
    unittest.main()
    