import unittest
import random
from board import Board

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
    def setUp(self):
        self.board_size = 3
        self.board = Board(self.board_size)
        ##probamos los metodos de la clase board
        #veremos si se puede insertar o no una pieza
        #pondremos una pieza incorrecta
    def test_insertar_pieza_horizontal(self):

        self.assertEqual(self.board.insert_piece(0,2,'S'),True)






if __name__ == '__main__':
    unittest.main()
