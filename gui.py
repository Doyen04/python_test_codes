import tkinter as tk
from tictac.classbasedtictactoe import Game 
game = Game()
nums = 1
ply = 'X'
def check1():
	 global nums 
	 global ply
	 if nums % 2 == 1:
	 	label1['text'] = ply
	 	label1['fg'] = 'white'
	 	game.make_move(0,'X')
	 	nums += 1
	 	ply = 'D'
	 	rest = game.minimax('D')['index']
	 	game.make_move(rest,'D')
	 	rin = data[rest]
	 	rin()
	 else :
	 	label1['text'] = ply 
	 	label1['fg'] = 'white'
	 	nums += 1
	 	ply = 'X'
def check2():
	 global nums 
	 global ply
	 if nums % 2 == 1:
		 label2['text'] = ply
		 label2['fg'] = 'white'
		 game.make_move(1,'X')
		 nums += 1
		 ply = 'D'
		 rest = game.minimax('D')['index']
		 game.make_move(rest,'D')
		 rin = data[rest]
		 rin()
	 else :
	 	label1['text'] = ply 
	 	label1['fg'] = 'white'
	 	nums += 1
	 	ply = 'X'
def check3():
	 global nums 
	 global ply
	 if nums % 2 == 1:
	 	label3['text'] = ply
	 	label3['fg'] = 'white'
	 	game.make_move(2,'X')
	 	nums += 1
	 	ply = 'D'
	 	rest = game.minimax('D')['index']
	 	game.make_move(rest,'D')
	 	rin = data[rest]
	 	rin()
	 	
	 else :
	 	label3['text'] = ply 
	 	label3['fg'] = 'white'
	 	nums += 1
	 	ply = 'X'
def check4():
	 global nums 
	 global ply
	 if nums % 2 == 1:
	 	label4['text'] = ply
	 	label4['fg'] = 'white'
	 	game.make_move(3,'X')
	 	nums += 1
	 	ply = 'D'
	 	rest = game.minimax('D')['index']
	 	game.make_move(rest,'D')
	 	rin = data[rest]
	 	rin()
	 	
	 else :
	 	label4['text'] = ply 
	 	label4['fg'] = 'white'
	 	nums += 1
	 	ply = 'X'
def check5():
	 global nums 
	 global ply
	 if nums % 2 == 1:
		 label5['text'] = ply
		 label5['fg'] = 'white'
		 game.make_move(4,'X')
		 nums += 1
		 ply = 'D'
		 rest = game.minimax('D')['index']
		 game.make_move(rest,'D')
		 rin = data[rest]
		 rin()
		 
	 else :
	 	label5['text'] = ply 
	 	label5['fg'] = 'white'
	 	nums += 1
	 	ply = 'X'
def check6():
	 global nums 
	 global ply
	 if nums % 2 == 1:
 		label6['text'] = ply
	 	label6['fg'] = 'white'
	 	game.make_move(5,'X')
	 	nums += 1
	 	ply = 'D'
	 	rest = game.minimax('D')['index']
	 	game.make_move(rest,'D')
	 	rin = data[rest]
	 	rin()
	 	
	 else :
	 	label6['text'] = ply 
	 	label6['fg'] = 'white'
	 	nums += 1
	 	ply = 'X'
def check7():
	 global nums 
	 global ply
	 if nums % 2 == 1:
	 	label7['text'] = ply
	 	label7['fg'] = 'white'
	 	game.make_move(6,'X')
	 	nums += 1
	 	ply = 'D'
	 	rest = game.minimax('D')['index']
	 	game.make_move(rest,'D')
	 	rin = data[rest]
	 	rin()
	 	
	 else :
	 	label7['text'] = ply 
	 	label7['fg'] = 'white'
	 	nums += 1
	 	ply = 'X'
def check8():
	 global nums 
	 global ply
	 if nums % 2 == 1:
	 	label8['text'] = ply
	 	label8['fg'] = 'white'
	 	game.make_move(7,'X')
	 	nums += 1
	 	ply = 'D'
	 	rest = game.minimax('D')['index']
	 	game.make_move(rest,'D')
	 	rin = data[rest]
	 	rin()
	 	
	 else :
	 	label8['text'] = ply 
	 	label8['fg'] = 'white'
	 	nums += 1
	 	ply = 'X'
def check9():
	 global nums 
	 global ply
	 if nums % 2 == 1:
	 	label9['text'] = ply
	 	label9['fg'] = 'white'
	 	game.make_move(8,'X')
	 	nums += 1
	 	ply = 'D'
	 	rest = game.minimax('D')['index']
	 	game.make_move(rest,'D')
	 	rin = data[rest]
	 	rin()
	 	
	 else :
	 	label9['text'] = ply 
	 	label9['fg'] = 'white'
	 	nums += 1
	 	ply = 'X'
data = [check1, check2, check3, check4, check5, check6, check7, check8,check9]

window = tk.Tk()
#window.columnconfigure(0, minsize=150)
#window.rowconfigure([0, 1], minsize=250)
frame = tk.Frame(master = window, 
								relief=tk.RAISED,
            					bg = 'white',
            					width=500,
            					height = 400).pack(fill=tk.X ,side=tk.LEFT,padx=90,pady=50)
label1 = tk.Button(text="A",
							bg='green',
							fg='green',
							width = 13,
							height = 6,
							master=frame,
							command = check1
							)
label1.place(x=90, y=290,)

label2 = tk.Button(text='b',
							bg='green',
							fg='green',
							width = 13,
							height = 6,
							command = check2,
							master=frame,)
label2.place(x=230, y=290, )

label3 = tk.Button(text='c',
							bg='green',
							fg='green',
							width = 13,
							height = 6,
							command = check3,
							master=frame)
label3.place(x=370, y=290, )
label4 = tk.Button(text='d',
							bg='green',
							fg='green',
							width = 13,
							height = 6,
							command = check4,
							master=frame)
label4.place(x=90, y=430, )
label5 = tk.Button(text='e',
							bg='green',
							fg='green',
							width = 13,
							height = 6,
							command = check5,
							master=frame)
label5.place(x=230, y=430, )
label6= tk.Button(text='f',
							bg='green',
							fg='green',
							width = 13,
							height = 6,
							command = check6,
							master=frame)
label6.place(x=370, y=430, )
label7= tk.Button(text='g',
							bg='green',
							fg='green',
							width = 13,
							height = 6,
							command = check7,
							master=frame)
label7.place(x=90, y=570, )
label8= tk.Button(text='h',
							bg='green',
							fg='green',
							width = 13,
							height = 6,
							command = check8,
							master=frame)
label8.place(x=230, y=570, )
label9= tk.Button(text='i',
							bg='green',
							fg='green',
							width = 13,
							height = 6,
							command = check9,
							master=frame)
label9.place(x=370, y=570, )
def main():
	window.mainloop()
if __name__ == '__main__':
	main()