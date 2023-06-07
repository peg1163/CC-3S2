import tkinter as tk
from tkinter.messagebox import *
from constantes import style
from Board import Board
import random


class Container(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        # Dimension de la vista login
        self.pack()
        self.place(x=0, y=0, width=900, height=660)
        self.configure(bg=style.beige)
        # edita desde aqui
        self.controller = controller
        self.init_widgets()

        self.frames = {}
        self.create_frames_button = tk.Button(self, text="Start", **style.menu, command=self.create_frames)
        self.create_frames_button.place(x=760, y=20, width=70, height=25)

    def create_frames(self):
        f = Container2
        frame = f(self, self)
        self.frames[f] = frame
        frame.tkraise()
        # se abre el archivo txt para poder limpiar el registro de la partida ya jugada
        archivo = open('Replay/replay.txt', 'w')
        archivo.truncate(0)

        archivo.close()

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

    def control(self):
        self.show_frame(Container2)

    def init_widgets(self):
        # frame1
        self.frame1 = tk.Frame(self, bg=style.beige)
        self.frame1.place(x=0, y=0, width=760, height=60)

        label_board_size = tk.Label(self.frame1, text='Board size: ', **style.label)
        label_board_size.place(x=500, y=20, width=100, height=20)

        self.entry_board_size = tk.Entry(self.frame1, font=style.arial)
        self.entry_board_size.place(x=600, y=20, width=40, height=20)


class Container2(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(parent)
        self.board = None
        self.container = container
        self.pack()
        self.place(x=0, y=60, width=900, height=600)
        self.configure(bg=style.beige2)
        self.condition()
        self.canvas.variable = tk.StringVar()
        # registro de puntos de cada jugador
        self.red_point = 0
        self.bluepoint = 0
        # registro de posicion de sos formado
        self.longitud = 0

    def condition(self):
        if int(self.container.entry_board_size.get()) >= 3:
            # self.create_board()
            self.init_widgets()
        else:
            showerror(tittle='Error', message="Tamaño invalido.")

    def create_board(self):

        # Se actualiza el tamaño del contenedor del tablero
        self.frame_board.update()

        # Crea un tablero vacio
        '''''
        self.board_size toma el valor del tamaño del tablero que se ingresa en la interfaz despues de apretar start
        lo que se quiere es que el tamañp del tablero se adapte a su contenedor en este caso seria self.frame_board
        asi que se toma el minimo valor entre ancho y altura y luego se divide entre el tamaño del tablero ingresado 
        de esta forma se logra contener el tablero en el frame board sea cual sea el tamaño que se ingrese.
        '''
        self.board = Board(int(self.container.entry_board_size.get()))
        self.board_size = self.board.get_board_size()

        frame_width = self.frame_board.winfo_width()
        frame_height = self.frame_board.winfo_height()
        # print(f'frame {frame_width} \ncell')
        self.cell_size = min(frame_width, frame_height) / self.board_size
        # print(self.cell_size)

        self.canvas_width = self.board_size * self.cell_size
        self.canvas_height = self.board_size * self.cell_size

        self.canvas = tk.Canvas(self.frame_board, width=self.canvas_width, height=self.canvas_height)
        self.canvas.place(x=0, y=0)
        self.canvas.variable = None

        # dibuja los rectangulos del tablero
        for row in range(self.board_size):
            for col in range(self.board_size):
                x0 = col * self.cell_size
                y0 = row * self.cell_size
                x1 = (col + 1) * self.cell_size
                y1 = (row + 1) * self.cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, fill='white', tags='cell')

                self.canvas.tag_bind('cell', '<Button-1>', self.on_cell_clicked)

    def on_cell_clicked(self, event):
        piece = self.piece()
        # si el turno no es del computador
        if piece != None and ((self.valueTurn.get() == 'red' and self.valuecomputer2.get() == 'No') or (
                self.valueTurn.get() == 'blue' and self.valuecomputer1.get() == 'No')):

            x = self.canvas.canvasx(event.x)
            y = self.canvas.canvasy(event.y)

            # Esta division nos indica el indice de la columna en la qu el usuario hace click
            col = int(x // self.cell_size)
            row = int(y // self.cell_size)

            print(f'inicio: {self.board.board}')

            # Mientras la celda seleccionada esté ocupada, solicitar al jugador que seleccione otra celda vacía
            while self.board.get_piece(row, col) is not None:
                showinfo(tittle='Care', message='Casilla Ocupada')
                event = self.canvas.wait_variable(self.canvas.variable)
                x = self.canvas.canvasx(event.x)
                y = self.canvas.canvasy(event.y)
                col = int(x // self.cell_size)
                row = int(y // self.cell_size)
                # guarda en elregistro que se ha creado un tablero
            if self.board.board_empty():
                self.replay(piece, self.valueTurn.get())

            # Insertamos la pieza en la posicion indicada
            self.board.insert_piece(row, col, piece, self.valueTurn.get())
            # Dibujamos la pieza en la posicion indicada
            self.draw_piece(self.valueTurn.get(), row, col, piece)

            # Cambiamos el turno
            #########################
            # game_mode determina el modo de juego
            #########################

            if self.game_mode.get() == "Simple":

                self.turn_s(piece)


            elif self.game_mode.get() == "General":

                self.turn_g(piece)

            print(f'final: {self.board.board}')
        # si el turno es del computador
        elif (self.valueTurn.get() == 'red' and self.valuecomputer2.get() == 'Yes') or (
                self.valueTurn.get() == 'blue' and self.valuecomputer1.get() == 'Yes'):
            pieza = random.randint(0, 1)
            if pieza == 0:
                piece = 'S'
            else:
                piece = 'O'
            col = random.randint(0, self.board_size - 1)
            row = random.randint(0, self.board_size - 1)
            while self.board.get_piece(row, col) is not None:
                col = random.randint(0, self.board_size - 1)
                row = random.randint(0, self.board_size - 1)
            if self.board.board_empty():
                self.replay(piece, self.valueTurn.get())
            self.board.insert_piece(row, col, piece, self.valueTurn.get())
            # Dibujamos la pieza en la posicion indicada
            self.draw_piece(self.valueTurn.get(), row, col, piece)
            # Cambiamos el turno
            #########################
            # game_mode determina el modo de juego
            #########################

            if self.game_mode.get() == "Simple":
                self.turn_s(piece)
            elif self.game_mode.get() == "General":
                self.turn_g(piece)
        else:
            showerror(title='Error', message='Seleccione una pieza')

    def turn_s(self, piece):
        turn = self.valueTurn.get()
        if self.valueTurn.get() == 'red':

            if self.valuecomputer2.get() == 'No':
                self.S_blue_player.config(state='normal')
                self.O_blue_player.config(state='normal')
                self.S_red_player.config(state='disabled')
                self.O_red_player.config(state='disabled')
                if self.win_or_tie_s('red'):
                    # si se forma un sos entonces dibuja la linea roja
                    self.draw_line(self.valueTurn.get())

            elif self.win_or_tie_s('red'):
                # si se forma un sos entonces dibuja la linea roja
                self.draw_line(self.valueTurn.get())
            self.replay(piece, turn)
        else:

            if self.valuecomputer1.get() == 'No':
                self.S_blue_player.config(state='disabled')
                self.O_blue_player.config(state='disabled')
                self.S_red_player.config(state='normal')
                self.O_red_player.config(state='normal')
                if self.win_or_tie_s('blue'):
                    # si se forma un sos entonces dibuja la linea azul
                    self.draw_line(self.valueTurn.get())
            elif self.win_or_tie_s('blue'):
                # si se forma un sos entonces dibuja la linea azul
                self.draw_line(self.valueTurn.get())
            self.replay(piece, turn)

    # verifica si hay un ganador o continua el juego
    def win_or_tie_s(self, turn):
        complete = self.board.win_or_tie_simple()
        if complete == 'Empty Board':
            showinfo(title='Care', message='Continue')
        else:
            if complete == 'Continue':
                if turn == 'red':
                    self.valueTurn.set('blue')
                else:
                    self.valueTurn.set('red')
            elif complete == 'Win':
                showinfo(title='Care', message=f'{turn} player win.\nCongratulations!')
                return True
            elif complete == 'Tie':
                showinfo(title='Care', message='Tie.\nTry again')

    # verifica si hay un punto , hay ganador o continua el juego
    def win_or_tie_g(self, turn):
        complete = self.board.win_or_tie_general()

        if complete == 'Empty Board':
            showinfo(title='Care', message='Continue')
            return True
        elif self.board.board_complete():
            if complete == 'Point':
                if turn == 'red':
                    self.red_point += 1
                else:
                    self.bluepoint += 1
            if self.red_point > self.bluepoint:
                showinfo(title='Care', message='Red player win.\nCongratulations!')
            elif self.red_point < self.bluepoint:
                showinfo(title='Care', message='Blue player win.\nCongratulations!')
            else:
                showinfo(title='Care', message='Tie.\nTry again')
        else:
            if complete == 'Continue':
                if turn == 'red':
                    self.valueTurn.set('blue')
                    return True
                else:
                    self.valueTurn.set('red')
                    return True
            elif complete == 'Point':
                if turn == 'red':
                    self.red_point += 1
                    return False
                else:
                    self.bluepoint += 1
                    return False

    def turn_g(self, piece):
        # guarda el punto para poder guardarlo el registro
        turna = self.valueTurn.get()
        if self.valueTurn.get() == 'red' and self.valuecomputer2.get() == 'No':

            if self.win_or_tie_g('red'):

                self.S_blue_player.config(state='normal')
                self.O_blue_player.config(state='normal')
                self.S_red_player.config(state='disabled')
                self.O_red_player.config(state='disabled')

            else:
                self.draw_line(self.valueTurn.get())

            self.replay(piece, turna)

        elif self.valueTurn.get() == 'blue' and self.valuecomputer1.get() == 'No':

            if self.win_or_tie_g('blue'):

                self.S_blue_player.config(state='disabled')
                self.O_blue_player.config(state='disabled')
                self.S_red_player.config(state='normal')
                self.O_red_player.config(state='normal')
            else:
                self.draw_line(self.valueTurn.get())
            self.replay(piece, turna)
        else:

            if not (self.win_or_tie_g(self.valueTurn.get())):
                self.draw_line(self.valueTurn.get())
            self.replay(piece, turna)

    def piece(self):
        if (self.redValue.get() == 'S') or (self.blueValue.get() == 'S'):
            piece = 'S'
        elif (self.redValue.get() == 'O') or (self.blueValue.get() == 'O'):
            piece = 'O'
        else:
            piece = None

        self.redValue.set(None)
        self.blueValue.set(None)
        return piece

    def draw_piece(self, valueTurn, row, col, piece):
        if piece == 'S':
            self.board.insert_piece(row, col, piece, valueTurn)
            self.canvas.create_text(
                (col + 0.5) * self.cell_size,
                (row + 0.5) * self.cell_size,
                text='S',
                font=('Arial', 32),
                fill=valueTurn
            )
            if valueTurn == 'red':
                self.S_red_player.deselect()
            elif valueTurn == 'blue':
                self.S_blue_player.deselect()
        elif piece == 'O':
            self.board.insert_piece(row, col, piece, valueTurn)
            self.canvas.create_text(
                (col + 0.5) * self.cell_size,
                (row + 0.5) * self.cell_size,
                text='O',
                font=('Arial', 32),
                fill=valueTurn
            )
            if valueTurn == 'red':
                self.O_red_player.deselect()
            elif valueTurn == 'blue':
                self.O_blue_player.deselect()

    def replay(self, piece, turn):
        longitud1 = len(self.board.posicion)
        archivo = open('Replay/replay.txt', 'a')
        with open('Replay/replay.txt', 'r') as archivo1:
            contenido = archivo1.read()
            print(len(contenido))
        if len(contenido) == 0:
            archivo.write('Tablero creado ' + '\n')
            archivo.write('Tablero : ' + str(self.board.board) + '\n')
        elif not len(contenido) == 0:
            archivo.write('El jugador ' + str(turn) + ' con la pieza ' + str(piece) + '\n')
            archivo.write('Tablero : ' + str(self.board.board) + '\n')
            if longitud1 > self.longitud:
                self.longitud = longitud1
                archivo.write('El jugador ' + str(turn) + ' formo un SOS' + '\n')

    def draw_line(self, valueTurn):

        position = self.board.posicion[-1]
        pos1 = position[0]
        pos2 = position[2]
        if valueTurn == 'red':
            self.canvas.create_line(
                (pos1[1] + 0.5) * self.cell_size,
                (pos1[0] + 0.5) * self.cell_size,
                (pos2[1] + 0.5) * self.cell_size,
                (pos2[0] + 0.5) * self.cell_size, fill='red', width=3)
        elif valueTurn == 'blue':
            self.canvas.create_line(
                (pos1[1] + 0.5) * self.cell_size,
                (pos1[0] + 0.5) * self.cell_size,
                (pos2[1] + 0.5) * self.cell_size,
                (pos2[0] + 0.5) * self.cell_size, fill='blue', width=3)

    def computer_get1(self):
        self.S_blue_player.config(state='disabled')
        self.O_blue_player.config(state='disabled')

    def computer_get2(self):
        self.S_red_player.config(state='disabled')
        self.O_red_player.config(state='disabled')
        self.valueTurn.set('blue')
        self.S_blue_player.config(state='normal')
        self.O_blue_player.config(state='normal')

    def init_widgets(self):

        # frame blue_player
        self.frame_blue_player = tk.Frame(self, bg=style.beige2)
        self.frame_blue_player.place(x=0, y=0, width=210, height=500)

        # frame tablero
        self.frame_board = tk.Frame(self, bg=style.beige2)
        self.frame_board.place(x=210, y=0, width=480, height=500)
        # print(f'frame {self.frame_board.winfo_width()}')

        # frame red_player
        self.frame_red_player = tk.Frame(self, bg=style.beige2)
        self.frame_red_player.place(x=690, y=0, width=210, height=500)

        # frame turno
        self.frame_turn = tk.Frame(self, bg=style.beige)
        self.frame_turn.place(x=0, y=500, width=900, height=100)

        self.valueTurn = tk.StringVar()
        self.valueTurn.set('red')
        self.valuecomputer1 = tk.StringVar()
        self.valuecomputer1.set('No')
        self.valuecomputer2 = tk.StringVar()
        self.valuecomputer2.set('No')
        # #
        # frame blue_player(210x500)
        label_blue_player = tk.Label(self.frame_blue_player, text='Blue Player', **style.blue)
        label_blue_player.place(x=30, y=50, width=100, height=30)

        label_human = tk.Label(self.frame_blue_player, text='Human', bg=style.beige2)
        label_human.place(x=30, y=100, width=100, height=30)

        self.blueValue = tk.StringVar()
        self.blueValue.set(None)
        self.S_blue_player = tk.Radiobutton(self.frame_blue_player, text='S', **style.letras, variable=self.blueValue,
                                            value='S', state='disabled')
        self.S_blue_player.place(x=50, y=150, width=100, height=30)
        self.O_blue_player = tk.Radiobutton(self.frame_blue_player, text='O', **style.letras, variable=self.blueValue,
                                            value='O', state='disabled')
        self.O_blue_player.place(x=50, y=200, width=100, height=30)

        label_computer1 = tk.Label(self.frame_blue_player, text='Computer', bg=style.beige2)
        label_computer1.place(x=30, y=250, width=100, height=30)
        self.computer_blue = tk.Radiobutton(self.frame_blue_player, text='Computer', **style.letras,
                                            variable=self.valuecomputer1, value='Yes', command=self.computer_get1)
        self.computer_blue.place(x=50, y=300, width=100, height=30)
        ##
        # frame red_player
        label_red_player = tk.Label(self.frame_red_player, text='Red Player', **style.red)
        label_red_player.place(x=30, y=50, width=100, height=30)

        label_human = tk.Label(self.frame_red_player, text='Human', bg=style.beige2)
        label_human.place(x=30, y=100, width=100, height=30)

        self.redValue = tk.StringVar()
        self.redValue.set(None)
        self.S_red_player = tk.Radiobutton(self.frame_red_player, text='S', **style.letras, variable=self.redValue,
                                           value='S')
        self.S_red_player.place(x=50, y=150, width=100, height=30)
        self.O_red_player = tk.Radiobutton(self.frame_red_player, text='O', **style.letras, variable=self.redValue,
                                           value='O')
        self.O_red_player.place(x=50, y=200, width=100, height=30)
        label_computer2 = tk.Label(self.frame_red_player, text='Computer', bg=style.beige2)
        label_computer2.place(x=30, y=250, width=100, height=30)
        self.computer_red = tk.Radiobutton(self.frame_red_player, text='Computer', **style.letras,
                                           variable=self.valuecomputer2, value='Yes', command=self.computer_get2)
        self.computer_red.place(x=50, y=300, width=100, height=30)

        self.replay_button = tk.Button(self.frame_red_player, text='Replay', **style.menu, state='disabled')
        self.replay_button.place(x=50, y=350, width=100, height=40)
        self.new_game_button = tk.Button(self.frame_red_player, text='New Game', **style.menu, state='disabled')
        self.new_game_button.place(x=50, y=400, width=100, height=40)

        # creamos el tablero
        self.after(1000, self.create_board())

        ##
        # frame turn (900x100)
        label_current_game = tk.Label(self.frame_turn, text='Current Turn: ', **style.label)
        label_current_game.place(x=330, y=30, width=80, height=30)
        self.game_mode = tk.StringVar()
        self.game_mode.set('None')
        self.simple_game_button = tk.Radiobutton(self.frame_turn, text="Simple Game", **style.menu,
                                                 variable=self.game_mode, value='Simple')
        self.simple_game_button.place(x=120, y=20, width=100, height=30)

        self.general_game_button = tk.Radiobutton(self.frame_turn, text="General Game", **style.menu,
                                                  variable=self.game_mode, value='General')
        self.general_game_button.place(x=600, y=20, width=100, height=30)

        label_turn = tk.Label(self.frame_turn, textvariable=self.valueTurn, **style.label)
        label_turn.place(x=410, y=30, width=50, height=30)
