class Board():
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = self.create_board()

    def get_board_size(self):
        return self.board_size

    def create_board(self):
        self.board = [[None for i in range(self.board_size)] for j in range(self.board_size)]
        return self.board
    def insert_piece(self, row, col, piece):
        # Validación del rango de las coordenadas
        if not (0 <= row < self.board_size) or not (0 <= col < self.board_size):
            return 'Coordenadas fuera del rango del tablero'

        # Validación del tipo de dato de la pieza
        if not isinstance(piece, str):
            return 'La pieza debe ser de tipo string'

        # Validación de valores válidos para la pieza
        valid_pieces = ['S', 'O']

        if piece not in valid_pieces:
            return 'Pieza no valida'

        if not (self.get_piece(row,col) == None):
            return 'Casilla ocupada'

        # Asignación de la pieza al tablero
        self.board[row][col] = piece
    def get_piece(self, row, col):
        if (0 <= row < self.board_size) and (0 <= col < self.board_size):
            return self.board[row][col]
        else:
            return None