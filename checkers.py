import tkinter as tk 
window = tk.Tk
from tkinter import Canvas
from tictac.jump import Jump
from tictac import checkers_AI as AI
from threading import Timer
import time 

jump = Jump()
class Board(window):
	def __init__(self, size ):
		super().__init__()
		self.config(bg='black')
		self.size = size 
		self.turn = 'black'
		self.selected = None
		self.board_grid = {}
		self.valid_move = {}
		self.board = []
		self.createboard()
		
	def createboard(self):
		global index , SIZE , myCanvas 
		index = -1
		myCanvas = Canvas(master=self,
										  	bg="white",
							  				height = 550,
							  				width =550)
		myCanvas.pack(fill = tk.X, side = tk.LEFT ,padx=20)
		SIZE = 69
		for h in range(self.size):
			self.rowconfigure(h,minsize=150,weight=1)
			self. columnconfigure(h, minsize=150,weight=1)
			for k in range(self.size):
				index += 1
				if k % 2 != ((h+1)%2):
					pigmnt = '#ba7a3a'
				else :
					pigmnt = '#f0d2b4'
				square = self.create_rectangle(k,h,SIZE,pigmnt,index)
				if h < 3 and pigmnt == '#f0d2b4':
					self.board.append('red')
				if h >= 3 and h < 5 and pigmnt == '#f0d2b4':
					self.board.append('e')
				if pigmnt == '#ba7a3a':
					self.board.append('n')
				if h >= 5 and pigmnt == '#f0d2b4':
					self.board.append('black')
				self.board_grid[index] = (k,h)
				myCanvas.tag_bind(square,"<ButtonPress-1>", self.play)
		self.draw_circle()
			
	def create_rectangle(self,x, y, r, pigment,num): 
		#center coordinates, radius
		x0 = x * r
		y0 = y * r
		x1 = x0+ r
		y1 = y0 + r
		return myCanvas.create_rectangle(x0,y0,x1,y1,fill=pigment,tag=f"rect{num}" , width = 2 , outline = 'tomato')
		
	def create_circle(self, x, y, r, color):
		#center coordinates, radius
		x0 = x - r
		y0 = y - r
		x1 = x + r
		y1 = y + r
		return myCanvas.create_oval(x0,y0,x1,y1,fill=color,outline='blue',tag=color)
		
	def cal_pos(self,point1,point2):
		return (point1*SIZE)+SIZE/2 ,(point2*SIZE)+SIZE/2
		
	def draw_circle(self):
		for spot in range(len(self.board)):
			if self.board[spot] != 'n' and self.board[spot] != 'e':
				x , y = self.board_grid[spot]
				numx , numy = self.cal_pos(x,y)
				color = self.board[spot].lower()
				circle = self.create_circle(numx, numy, 55/2,color)
				if self.board[spot].isupper():
					ncircle = self.create_circle(numx,numy,25/2,'blue')
					myCanvas.tag_bind(ncircle,"<ButtonPress-1>",self.play)
				myCanvas.tag_bind(circle,"<ButtonPress-1>", self.play)
				
	def play(self,event):
		c , g = (event.x//SIZE) , (event.y//SIZE)
		for key , value in self.board_grid.items():
			if value == (c, g):
				bkey = key
				if self.selected and bkey in self.valid_move:
					self.make_move(bkey,self.selected)
					t = Timer(1, self.almove)  
					t.start()
				elif self.board[bkey].lower() == self.turn:
					self.valid_move = {}
					self.clear_canvas()
					self.selected = bkey
					self.get_move(self.selected)
					
				else :
					self.selected = None
					self.valid_move = {}
					self.clear_canvas()

		for key , value in self.valid_move.items():
			if key in self.board_grid:
				x , y = self.board_grid[key]
				numx , numy = self.cal_pos(x,y)
				myCanvas.itemconfigure(f"rect{key}", fill='pink')
				circle = self.create_circle(numx, numy, 25/2,'green')
				myCanvas.tag_bind(circle,"<ButtonPress-1>", self.play)
	def almove(self):
		game = AI.Monte()
		result = game.find_next_move(self.board,1,AI.Node)
		self.board = result.board
		myCanvas.delete('red')
		myCanvas.delete('black')
		myCanvas.delete('blue')
		myCanvas.delete('text')
		self.draw_circle()
		self.turn = 'black'
	
	def get_move(self,nums):
		self.valid_move.update(jump.get_move(nums,self.board))
		
	def clear_canvas(self):
		index = -1
		for key in range(8):
			for value in range (8):
				index += 1
				if key % 2 != ((value+1)%2):
					pigmnt = '#ba7a3a'
				else :
					pigmnt = '#f0d2b4'
				myCanvas.itemconfigure(f'rect{index}', fill=pigmnt)
				myCanvas.delete('green')
			
	def make_move(self,to,frm):
		self.board = jump.make_move(self.board,self.valid_move,to,frm)
		self.valid_move = {}
		myCanvas.delete('red')
		myCanvas.delete('black')
		myCanvas.delete('blue')
		myCanvas.delete('text')
		if self.turn == 'red':
			self.turn = 'black'
		else :
			self.turn = 'red'
		self.clear_canvas()
		self.draw_circle()
		
def main():
	board = Board(8)
	board.mainloop()
main()