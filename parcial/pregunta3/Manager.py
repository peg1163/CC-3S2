import tkinter as tk
from tkinter import PhotoImage
from screens import Container
class Manager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("SOS Game")
        self.geometry("900x650")
        icon = PhotoImage(file="imagenes/duck.png")
        self.iconphoto(True, icon)
        self.resizable(False, False)
        container = tk.Frame(self)
        container.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True)
        container.configure(bg="red")

        self.frames = {}
        f = Container
        frame = f(container, self)
        self.frames[f] = frame
        # frame.grid(row=0,column=0,sticky=tk.NSEW)
        self.show_frame(Container)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()