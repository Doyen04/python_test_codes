#board,n,ply,sevn,skip,first
board = [
				'n','red','n','red','n','red','n','red',
				'red','n','red','n','red','n','red','n',
				'n','red','n','red','n','red','n','red',
				'e','n','black','n','e','n','e','n',
				'n','e','n','e','n','e','n','e',
				'black','n','black','n','black','n','black','n',
				'n','black','n','black','n','black','n','black',
				'black','n','black','n','black','n','black','n',
]
class Jump:
	def jumpright(self,board,n,ply_color,sevn,nin,skip=[],first_skip=[]):
		data = {}
		last_jump = []
		if ply_color == 'red' or ply_color == 'RED':
			enemy = 'black'
		else :
			enemy = 'red'
		point = n+(sevn*2)
		try :
			board[point]
		except IndexError:
			return data 
		else :
			if board[point] == 'e' and board[point-sevn].lower() == enemy:
				last_jump.append(point-sevn)
				data[point] = last_jump+skip+first_skip
				data.update(self.jumpright(board,point,ply_color,sevn,nin,skip=last_jump,first_skip=skip))
				data.update(self.jumpleft(board,point,ply_color,sevn,nin,skip=last_jump,first_skip=skip))
		return data 
	def jumpleft(self,board,n,ply_color,sevn,nin,skip=[],first_skip=[]):
		data = {}
		last_jump = []
		if ply_color == 'red' or ply_color == 'RED':
			enemy = 'black'
		else :
			enemy = 'red'
		point = n+(nin*2)
		try :
			board[point]
		except IndexError:
			return data
		else :
			if board[point] == 'e' and board[point-nin].lower() == enemy :
				last_jump.append(point-nin)
				data[point] = last_jump+skip+first_skip
				data.update(self.jumpright(board,point,ply_color,sevn,nin,skip=last_jump,first_skip=skip))
				data.update(self.jumpleft(board,point,ply_color,sevn,nin,skip=last_jump,first_skip=skip))
		return data 
	def get_move(self,nums,board):
		moves = {}
		ply = board[nums]
		if ply == 'red':
			sevn = 7 
			nin = 9
		else :
			sevn = -7 
			nin = -9
		if ply == 'red' or ply == 'black':
			runs = 1
		else :
			runs = 2
		for rate in range(runs):
			try :
				board[nums+sevn]
			except IndexError:
				moves['e'] = []
			else :
				if board[nums+sevn] == 'e':
					moves[nums+sevn] = []
			try :
				board[nums+nin]
			except IndexError:
				moves['e'] = []
			else :
				if board[nums+nin] == 'e':
					moves[nums+nin] = []
			moves.update(self.jumpright(board,nums,ply,sevn,nin))
			moves.update(self.jumpleft(board,nums,ply,sevn,nin))
			sevn = 7
			nin = 9
		return moves 
	def make_move(self,board,moves,to,frm):
		if to in moves:
			for k in moves[to]:
				board[k] = "e"
		#print(board[frm])
		board[to]  = board[frm]
		#print(board[to])
		board[frm]  = 'e'
		
		if to <= 7 and board[to] =='black':
			board[to] = board[to].upper()
		if  board[to] == 'red' and to >= 56:
			board[to] = board[to].upper()
		return board
	def draw(self,board):
		board = [k for k in board]
		for key in range(len(board)):
			if board[key] == 'n':
				board[key] = '•'
			if board[key] != 'e' :
				board[key] = board[key][0]
			print("|<{}>|".format(board[key]), end="")
			value = [7,15,23,31,39,47,55,63]
			for k in value :
				if k == key:
					print(key)
					
					
print(Jump().draw(board))
'''
print(Jump().jumpright(board,56,'black',-7,-9))
myCanvas.create_text(241,310,font="Times 10 italic ", text=f"{ply}", fill = 'green',tag="text")'''