import tkinter as tk 
from tkinter import font
from tictac.classbasedtictactoe import Game 
from threading import Timer
import time 
game = Game()
window = tk.Tk

class Board(window):
	def __init__(self, size ):
		super().__init__()
		self.size = size 
		self.ply = 'X'
		self.board_grid = {}
		self.createboard()
	def createboard(self):
		frame = tk.Frame(master=self,
										bg = 'red',
										width = 200,
										height = 10,	)
		global index 
		index = -1
		frame.pack(fill = tk.X, side = tk.LEFT ,padx=55)
		for h in range(self.size):
			self.rowconfigure(h,minsize=15,weight=1)
			self. columnconfigure(h, minsize=15,weight=1)
			for k in range(self.size):
				index += 1
				label = tk.Button(text="",
												fg = 'blue',
												bg = 'white',
												width = 10,
												height =5,
												border=2,
												highlightbackground="blue",
												master=frame)
				self.board_grid[label] = index
				label.bind("<ButtonPress-1>", self.play)
				label.grid(row = h, column = k,pady=5,padx=5,sticky="nsew" )
					
	def play(self,event):
		button = event.widget
		if button['text'] == '' and self.ply == 'X' and not game.winning('D'):
			button['text'] = self.ply
			game.make_move(self.board_grid[button],self.ply)
			self.ply = 'D'
			t = Timer(0.5, self.almove)  
			t.start()
			#self.almove()
	def almove(self):
		if not game.winning('X') and len(game.avaliable_spot()) != 0:
			point = game.minimax(self.ply)['index']
			for key, value in self.board_grid.items():
				if value == point :
					key['text'] = self.ply
					game.make_move(point,self.ply)
					self.ply = 'X'
			
			
def main():
	board = Board(3)
	board.mainloop()
	
main()
				