import tkinter as tk
from tkinter import *

win = tk.Tk


class App(win):
    def __init__(self):
        super().__init__()
        self.config(bg='black')
        self.canvas = tk.Canvas(width=550,
                                height=450,
                                bg='white')
        self.canvas.pack(fill=tk.X, side=tk.LEFT, padx=20)
        self.canvas.bind('<Motion>', self.draw)
        self.canvas.bind('<ButtonRelease>', self.reset)
        self.oldx = None
        self.oldy = None
        self.mainloop()

    def draw(self, event):
        x, y = event.x, event.y
        if self.oldx == None:
            self.canvas.create_oval(x, y, x, y, fill='green', width=20, outline='green')
            '''capstyle = ROUND'''
        # ''' ,'''splinesteps = 36 smooth = True ,
        if self.oldx and self.oldy:
            print(True)
            self.canvas.create_line(self.oldx, self.oldy, event.x, event.y, fill='red', width=20, capstyle=ROUND)
        self.oldx = x
        self.oldy = y

    def reset(self, event):
        self.oldx, self.oldy = None, None


App()
