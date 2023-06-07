from Board import Board
import random
import unittest
from screens import Container
from screens import Container2

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board_size = random.randint(3, 100)
        self.board = Board(self.board_size)

    def test_create_board(self):

        # Verificamos si el tablero tiene tamaño n en cada dimension
        self.assertEqual(len(self.board.board), self.board_size)
        self.assertEqual(len(self.board.board[0]), self.board_size)
        self.assertEqual(len(self.board.board[1]), self.board_size)
        self.assertEqual(len(self.board.board[2]), self.board_size)

        # Verifica si cada casilla esta vacia para un tablero vacio
        for i in range(self.board.board_size):
            for j in range(self.board.board_size):
                self.assertEqual(self.board.board[i][j], None)


    def test_insert_piece_valid(self):
        #Insertar una pieza valida en una posicion valida y tambien el juego que ha ingreso la ficha
        row = 0
        col = 0
        piece = 'O'
        self.board.insert_piece(row, col, piece, 'red')
        result = self.board.get_letter(row, col)
        self.assertEqual(result, 'O')
        self.assertEqual(self.board.get_player(row,col), 'red')

    def test_insert_piece_invalid_coordinates(self):
        # Insertar una pieza en una posicion invalida y tambien el juego que se ha ingresado la ficha
        row = self.board_size
        col = self.board_size
        piece = 'S'
        result = self.board.insert_piece(row,col,piece,'red')
        self.assertEqual(result, 'Coordenadas fuera del rango del tablero')
        self.assertIsNone(self.board.get_letter(row, col), 'red')

    def test_insert_piece_invalid_piece_type(self):
        # Insertar una pieza de tipo invalido en una posicion valida
        row = 0
        col = 0
        piece = 4
        result = self.board.insert_piece(row, col, piece,'red')
        self.assertEqual(result,'La pieza debe ser de tipo string')
        self.assertIsNone(self.board.get_letter(row,col))

    def test_insert_piece_invalid_piece_value(self):
        # Insertar una pieza con un valor invalido en una posicion valida
        row = 0
        col = 0
        piece = 'W'
        result = self.board.insert_piece(row, col, piece,'red')
        self.assertEqual(result, 'Pieza no valida')
        self.assertIsNone(self.board.get_letter(row, col))

    def test_insert_piece_valid_position_busy(self):
        # Insertar una pieza valida en una casilla ocupada
        row = 0
        col = 0
        piece = 'S'
        # Insertamos una pieza en (0,0)
        self.board.insert_piece(row, col, piece,'red')
        # Volvemos a insertar otra pieza en (0,0)
        result = self.board.insert_piece(row, col, piece,'red')
        self.assertEqual(result,'Casilla ocupada')

class TestCompleteSOS(unittest.TestCase):
    def setUp(self):
        self.board = Board(4)
        self.container = Container
        self.container2 = Container2
    # Test
    def test_complete_row_SOS(self):
        self.board.insert_piece(0, 0, 'S','red')
        self.board.insert_piece(0, 1, 'S','red')
        self.board.insert_piece(0, 2, 'O','red')
        self.board.insert_piece(0, 3, 'S','red')
        result = self.board.complete_SOS_general()
        self.assertTrue(result)


    def test_complete_colum_SOS(self):
        self.board.insert_piece(0, 0, 'S','red')
        self.board.insert_piece(1, 0, 'S','red')
        self.board.insert_piece(2, 0, 'O','red')
        self.board.insert_piece(3, 0, 'S','red')
        result,player = self.board.complete_SOS_simple()
        self.assertTrue(result)
        self.assertEqual(player,'red')

    def test_complete_diagonal_rigth_to_left(self):
        self.board.insert_piece(0, 0, 'S','red')
        self.board.insert_piece(1, 1, 'S','red')
        self.board.insert_piece(2, 2, 'O','red')
        self.board.insert_piece(3, 3, 'S','red')
        result = self.board.complete_SOS_simple()
        self.assertTrue(result)


    def test_complete_diagonal_left_to_rigth(self):
        self.board.insert_piece(0, 3, 'S','red')
        self.board.insert_piece(1, 2, 'S','red')
        self.board.insert_piece(2, 1, 'O','red')
        self.board.insert_piece(3, 0, 'S','red')
        result,player = self.board.complete_SOS_simple()
        self.assertTrue(result)
        self.assertEqual(player,'red')


class TestWinOrTie(unittest.TestCase):
    def setUp(self):
        self.board = Board(4)
        self.container = Container
        self.container2 = Container2
    def test_empty_board(self):
        result = self.board.win_or_tie_general()
        self.assertEqual(result,'Empty Board')


    def test_board_complete_SOS_incomplete(self):
        for row in range(self.board.get_board_size()):
            for col in range(self.board.get_board_size()):
                self.board.insert_piece(row, col, 'S','red')
        result = self.board.win_or_tie_general()
        self.assertEqual(result,'Continue')


    def test_board_complete_SOS_complete(self):
        self.board.insert_piece(0, 0, 'S','blue')
        self.board.insert_piece(1, 0, 'O','blue')
        self.board.insert_piece(2, 0, 'S','blue')
        self.board.insert_piece(3, 0, 'S','blue')

        for row in range(self.board.get_board_size()):
            for col in range(1, self.board.get_board_size()):
                self.board.insert_piece(row, col, 'S','red')
        turn='blue'
        result = self.board.win_or_tie_general()
        self.assertEqual(result, 'Point')


    def test_board_incomplete_SOS_complete(self):
        self.board.insert_piece(0, 0, 'S','blue')
        self.board.insert_piece(1, 0, 'O','blue')
        self.board.insert_piece(2, 0, 'S','blue')
        self.board.insert_piece(3, 0, 'S','blue')

        result,player = self.board.win_or_tie_simple()
        self.assertEqual(result, 'Win')

    def test_board_incomplete_SOS_incomplete(self):
        self.board.insert_piece(0, 0, 'S','blue')

        result,player = self.board.win_or_tie_simple()
        self.assertEqual(result, 'Continue')
        self.assertEqual(player,'None')


if __name__ == '__main__':
    unittest.main()

