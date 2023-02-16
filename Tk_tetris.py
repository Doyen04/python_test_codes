import tkinter as tk
from tkinter import messagebox
from random import choice

class Game(tk.Canvas):
	SPEED = 250
	SQUARE_SIZE = 20
	WIDTH = 400
	HEIGHT = 600
	def __init__(self):
		super().__init__(background='black',width=self.WIDTH,height=self.HEIGHT)
		self.pieces = [
	[('orange'),(160,0),(180,0),(180,20),(200,20)],
	[('lightblue'),(180,0),(200,0),(160,20),(180,20)],
	[('green'),(180,0),(200,0),(180,20),(200,20)],
	[('blue'),(160,20),(180,0),(180,20),(200,20)],
    [('red'),(160, 0), (180, 0), (200, 0),(220,0)],
	[('yellow'),(160, 0), (180, 0), (200, 0),(160,-20)],
	[('purple'),(200,-20),(160, 0), (180, 0),(200, 0),],
			]
		self.screen = []
		self.begin = True
		self.curr = []
		self.score = 0
		self.pack()
		self.draw_button()
		
	def draw(self,arg):
		box = []
		for x,  y in arg[1:]:
			rect = self.create_rectangle(x,y,x+20,y+20,fill=arg[0],tag='rect')
			box.append(rect)
		return box 
			
	def draw_button(self):
		dir = ['Up','Left','Right','Down']
		i = 0
		for y in range (3):
			for x in range((y+1)%2,3,2):
				label = tk.Button(text=dir[i],
					fg = 'white',
					bg = 'red',
					width = 5,
					height =3,
					border=2,
					highlightbackground="blue",)
				label.bind("<ButtonPress-1>",self.key)
				label.place(x = (150)+(95*x), y = self.HEIGHT+(85*y),)
				i+=1
		
	def key(self,event):
		direc = event.widget['text']
		if direc == 'Right':	self.move_box((20,0))
		if direc == 'Left':	self.move_box((-20,0))
		if direc == 'Up':	self.rotate()
		if direc == 'Down':	self.move_box((0,20))
		
	def get_move_coord(self,arg):
		x = [self.coords(k)[2]+arg[0] for k in self.curr]
		y = [self.coords(k)[3]+arg[1] for k in self.curr]
		fake = tuple(zip(x,y))
		return fake
		
	def move_box(self,arg):
		n = arg
		fake = self.get_move_coord(arg)
		if self.check(fake) and self.row_move(fake) and self.col_move(fake):
			for key  in self.curr:
				self.move(key,n[0],n[1])
		faker = self.get_move_coord((0,20))
		if self.col_move(faker) == False or self.check(faker) == False:
			for key in self.curr:
				self.screen.append(key)
			self.remove_com()
			self.curr = self.draw(choice(self.pieces))
			dfake = self.get_move_coord((0,20))
			if self.check(dfake) == False:
				self.delete(tk.ALL)
				self.screen = []
				messagebox.showinfo(
					'Game Over',"You scored %d points." % self.score)
				self.begin = True
				
	def check(self,arg):
		fake = [(x,y) for x,y in arg]
		bx = [self.coords(rect)[2] for rect in self.screen]
		by = [self.coords(rect)[3] for rect in self.screen]
		for k, v in fake:
			for key , value in zip(bx,by):
				if k == key and v == value :
					return False 
		return True 
		
	def remove_com(self):
		self.delete('scor')
		y = [self.coords(rect)[3] for rect in self.find_all()]
		box = list(self.find_all())
		cord = {}
		some = []
		for key in set(y) :
			cord[key] = y.count(key)
		for key , value in cord.items():
			if value == self.WIDTH//self.SQUARE_SIZE:
				some.append(key)
		 
		for key , value in zip(box,y):
			if any(value == crd for crd in some) :
				self.delete(key)
				self.screen.remove(key)
		if some:
			self.score += len(some)
			for key in self.screen:
				coord = self.coords(key)[3]
				for crd in some :
					if coord < crd:
						self.move(key,0,20)
		
	def row_move(self ,arg):
		fk = [(x,y) for x,y in arg]
		for x, y in fk:
			if x < 20 or x > self.WIDTH:
				return False 
		return True 
		
	def col_move(self ,arg):
		fk = [(x,y) for x,y in arg]
		for x, y in fk:
			if y > self.HEIGHT:
				return False 
		return True 
		
	def rotate(self):
		pivot = self.curr[2]
		px , py = (self.coords(pivot)[2], self.coords(pivot)[3])
		fake = []
		crd = []
		for key in self.curr:
			x,y = (self.coords(key)[2],self.coords(key)[3])
			nx =  ((px - x) + (py - y))
			ny = (-(px - x) + (py - y))
			fake.append((x+nx, y+ny))
			crd.append((nx,ny))
		if self.check(fake) and self.row_move(fake) and self.col_move(fake):
			for key in range(len(self.curr)):
				self.move(self.curr[key],crd[key][0],crd[key][1])
			
	def play(self):
		self.delete('scor')
		self.create_text(
				50, 20, text=f"Score : {self.score}", tag="scor",fill="white", font=('Helvetica 4 bold'))
		if self.begin:
			self.curr =self.draw(choice(self.pieces))
			self.begin = False
		self.move_box((0,20))
		self.after(self.SPEED,self.play)

if __name__ == '__main__':
	root = tk.Tk()
	root.config(bg='lightblue')
	g = Game()
	g.play()
	root.mainloop()