class Board:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = self.create_board()
        self.posicion=[]

    def get_board_size(self):
        return self.board_size

    def set_board_size(self, size):
        self.board_size = size

    def get_piece(self, row, col):
        if (0 <= row < self.board_size) and (0 <= col < self.board_size):
            return self.board[row][col]
        else:
            return None

    def get_letter(self, row, col):
        if self.get_piece(row,col)==None:
            return None
        else:
            if (0 <= row < self.board_size) and (0 <= col < self.board_size):
                return self.board[row][col][0]

    def get_player(self, row, col):
        if self.get_piece(row, col) == None:
            return None
        else:
            if (0 <= row < self.board_size) and (0 <= col < self.board_size):
                return self.board[row][col][1]

    def get_board(self):
        return self.board

    def board_complete(self):
        size = self.get_board_size()
        for row in range(size):
            for col in range(size):
                piece = self.get_piece(row, col)
                if not piece is None:
                    continue
                else:
                    return False
        return True

    def board_empty(self):
        size = self.get_board_size()
        for row in range(size):
            for col in range(size):
                piece = self.get_piece(row, col)
                if piece is None:
                    continue
                else:
                    return False
        return True

    def create_board(self):
        self.board = [[None for i in range(self.board_size)] for j in range(self.board_size)]
        return self.board

    def insert_piece(self, row, col, piece, player):
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

        if not self.get_piece(row, col) == None:
            return 'Casilla ocupada'

        # Asignación de la pieza al tablero
        self.board[row][col] = (piece, player)

    def complete_SOS_simple(self):
        size = self.get_board_size()
        # Recorre el tablero
        for row in range(size):
            for col in range(size):
                # Verifica en fila
                if col<size-2 and self.get_letter(row, col) == 'S':
                    if self.get_letter(row, col + 1) == 'O' and self.get_letter(row, col + 2) == 'S':
                        self.posicion.append(((row, col), (row, col + 1), (row, col + 2)))
                        return True
                # Verifica en columna
                if row< size and self.get_letter(row, col) == 'S':
                    if self.get_letter(row + 1, col) == 'O' and self.get_letter(row + 2, col) == 'S':
                        self.posicion.append(((row, col), (row, col + 1), (row, col + 2)))
                        return True
                # Verifica en diagonal    
                if row <size-2 and col <size-2 and self.get_letter(row, col) == 'S':
                    if self.get_letter(row + 1, col + 1) == 'O' and self.get_letter(row + 2, col + 2) == 'S':
                        self.posicion.append(((row, col), (row, col + 1), (row, col + 2)))
                        return True
                # Verifica en diagonal inversa    
                if row >=2 and col <size-2 and self.get_letter(row, col) == 'S':
                    if self.get_letter(row - 1, col + 1) == 'O' and self.get_letter(row - 2, col + 2) == 'S':
                        self.posicion.append(((row, col), (row, col + 1), (row, col + 2)))
                        return True            
        return False
    #retorna un gandor empate o sigue jugando
    def win_or_tie_simple(self):
        if self.board_empty():
            return 'Empty Board'
        else:
            if self.board_complete():
                complete = self.complete_SOS_simple()
                if complete:
                    return 'Win'
                else:
                    return 'Tie'
            else:
                complete = self.complete_SOS_simple()
                if complete:
                    return 'Win'
                else:
                    return 'Continue'

    def complete_SOS_general(self):

        size = self.get_board_size()
        # Recorre el tablero

        for row in range(size):
            for col in range(size):
                # Verifica en fila
                if col < size - 2 and self.get_letter(row, col) == 'S':
                    if self.get_letter(row, col + 1) == 'O' and self.get_letter(row, col + 2) == 'S':
                        aux = ((row, col), (row, col + 1), (row, col + 2))
                        #si no se repite el sos
                        if aux not in self.posicion:
                            #guarda la posicion donde se forma sos
                            self.posicion.append(aux)
                            print(self.posicion)
                            return True
                # Verifica en columna
                if row < size and self.get_letter(row, col) == 'S':
                    if self.get_letter(row + 1, col) == 'O' and self.get_letter(row + 2, col) == 'S':
                        aux = ((row, col), (row + 1, col), (row + 2, col))
                        # si no se repite el sos
                        if aux not in self.posicion:
                            # guarda la posicion donde se forma sos
                            self.posicion.append(aux)
                            print(self.posicion)
                            return True
                # Verifica en diagonal
                if row < size - 2 and col < size - 2 and self.get_letter(row, col) == 'S':
                    if self.get_letter(row + 1, col + 1) == 'O' and self.get_letter(row + 2, col + 2) == 'S':
                        aux = ((row, col), (row + 1, col + 1), (row + 2, col + 2))
                        # si no se repite el sos
                        if aux not in self.posicion:
                            # guarda la posicion donde se forma sos
                            self.posicion.append(aux)
                            print(self.posicion)
                            return True
                # Verifica en diagonal inversa
                if row >= 2 and col < size - 2 and self.get_letter(row, col) == 'S':
                    if self.get_letter(row - 1, col + 1) == 'O' and self.get_letter(row - 2, col + 2) == 'S':
                        aux = ((row, col), (row - 1, col + 1), (row - 2, col + 2))
                        # si no se repite el sos
                        if aux not in self.posicion:
                            # guarda la posicion donde se forma sos
                            self.posicion.append(aux)
                            print(self.posicion)
                            return True
        return False
    #retorna un punto o sigue jugando
    def win_or_tie_general(self):
        if self.board_empty():
            return 'Empty Board'
        else:
            if self.board_complete():
                complete = self.complete_SOS_general()
                if complete:
                    return 'Point'
                else :
                    return 'Continue'
            else:
                complete = self.complete_SOS_general()
                if complete:
                    return 'Point'
                else:
                    return 'Continue'


