import tkinter as tk
from tkinter import messagebox
import random as rd

class Snake(tk.Canvas):
	def __init__(self):
		super().__init__(
			width=600, height=600, background="black", )
		self._init()
		self.make_snake()
		self.pack()
		self.draw_button()
		self.after(1000,self.play)
	def _init(self):
		self.snake_pos = [(100, 100), (80, 100), (60, 100)]
		self.food = (300,300)
		self.direc = 'Right'
		self.game = False
		self.score = 0
		
	def draw_button(self):
		self.create_rectangle(18,38,580,582,outline='red',tag='border',width = 1,)
		dir = ['Up','Left','Right','Down']
		i = 0
		for y in range (3):
			for x in range((y+1)%2,3,2):
				label = tk.Button(text = dir[i],
					fg = 'white',
					bg = 'red',
					width = 4,
					height =2,
					border=2,
					highlightbackground="blue",)
				label.bind("<ButtonPress-1>",self.key_press)
				label.place(x = (140)+(110*x), y = 600+(90*y),)
				i+=1
	def key_press(self,event):
		direc = event.widget['text']
		oppose = [{'Up','Down'},{'Left','Right'}]
		if {self.direc , direc} not in oppose:
			self.direc = direc
			self.update()
		self.delete('scorer')
		self.create_text(
			195, 20, text=f"direction : {self.direc}", tag="scorer",fill="white", font=('Helvetica 4 bold'))
			
	def clear_canvas(self):
		self.delete('score')
		self.delete('snake')
		self.delete('food')
	
	def make_snake(self):
		self.clear_canvas()
		self.create_text(
			65, 20, text=f"Score : {self.score}", tag="score",fill="white", font=('Helvetica 4 bold'))
		I = 0
		for x , y in self.snake_pos:
			self.create_rectangle(x,y,x+20,y+20,fill='green',tag='snake',width = 1,)
			if I >= 6:
				I = -1
			I += 1
		a , b = self.food
		self.create_oval(a,b,a+20,b+20,fill='blue',tag='food')
		
	def check(self):
		x , y = self.snake_pos[0]
		if (x, y) == self.food:
			self.score += 1
			self.food = (rd.randint(1,28)*20,rd.randint(2,29)*20)
			self.snake_pos.append(self.snake_pos[-1])
		if x  >= 580 or x <= 0 or y >=580 or y<= 20:
			self.game  = True 
		else :
			self.game = False 
		if (x, y) in self.snake_pos[1:]:
			self.game = True
		
	def update(self):
		self.check()
		x , y = self.snake_pos[0]
		if self.direc == 'Right':
			x = x + 20
		if self.direc == 'Left':
			x = x - 20
		if self.direc == 'Up':
			y = y - 20
		if self.direc == 'Down':
			y = y + 20
		self.snake_pos = [(x, y)]+self.snake_pos[:-1]
		self.check() 
		if self.game == False :
			self.make_snake()
		else :
			self.clear_canvas()
			self._init()
			self.delete('scorer')
			messagebox.showinfo(
					'Game Over',"You scored %d points." % self.score)
		
	def play(self):
		self.update()
		self.after(400,self.play)

root = tk.Tk()
root.title("Snake")
root.resizable(False, False)
root.tk.call("tk", "scaling", 3.0)

board = Snake()

root.mainloop()