import random as rd 
import math 
from copy import deepcopy
from tictac.jump import Jump, board 

jump = Jump()
l = None 
class Node:
	def __init__(self,parent = l, child = [] , board = l, ply_no = None, v_count = 0, w_score = 10):
		self.parent = parent
		self.child = []
		self.board = board
		self.ply_no = ply_no
		self.v_count = v_count
		self.w_score = w_score
	def get_random_child(self):
		return rd.choice(self.child)
			
	def get_avaliable_spot(self):
		empty_spot = []
		ply_no =  self.ply_no
		for k in range(len(self.board)):
			if ply_no == 1:
				ply1 = 'red'
				ply2 = 'RED'
			else :
				ply1 = 'black'
				ply2 = 'BLACK'
			if self.board[k] == ply1 or self.board[k] == ply2:
				result = jump.get_move(k,self.board)
				if result != {}:
					best = []
					edge = []
					moves = {}
					spot = None
					#print(result)
					for key , value in result.items():
						if type(key) == int :
							if len(value) > len(best):
								best = value 
								spot = key
								moves[spot] = best
								edge = []
							else :
								move = {}
								move[key] = value 
								edge.append(move)
					for key, value in moves.items():
						if type(key) == int:
							fake_dict = {}
							fake_dict[key] = value 
							fake_dict['frm'] = k
							empty_spot.append(fake_dict)
					for num in edge:
						for key, value in num.items():
							if type(key) == int:
								fake_dict = {}
								fake_dict[key] = value 
								fake_dict['frm'] = k
								empty_spot.append(fake_dict)
		#print(empty_spot)
		return empty_spot
		
	def make_move(self , board, ply, spot):
		board[spot] = ply
		return board
		
	def get_possible_state(self):
		empty_spot = []
		ply_no = 3 - self.ply_no
		for k in range(len(self.board)):
			if ply_no == 1:
				ply1 = 'red'
				ply2 = 'RED'
			else :
				ply1 = 'black'
				ply2 = 'BLACK'
			if self.board[k] == ply1 or self.board[k] == ply2:
				result = jump.get_move(k,self.board)
				if result != {}:
					best = []
					sec = []
					move = {}
					spot = None
					for key , value in result.items():
						if type(key) == int :
							if len(value) > len(best):
								best = value 
								spot = key
							else :
								move = {}
								move[key] = value 
								sec.append(move)
					for key in sec:
						if type(key) == dict:
							for spt, value in key.items():
								board = deepcopy(self.board)
								state = jump.make_move(board,key,spt,k)
								empty_spot.append(state)
					move = {}
					sec = []
					move[spot] = best
					if spot != None:
						board = deepcopy(self.board)
						state = jump.make_move(board,move,spot,k)
						empty_spot.append(state)
		return empty_spot
		
	def get_child_max(self):
		score_array = []
		for key in self.child:
			score_array.append(key.v_count)
		max_score = max(score_array)
		index = score_array.index(max_score)
		return self.child[index]
		
	def random_play(self):
		spot = self.get_avaliable_spot()
		#print(len(spot))
		try :
			index = rd.choice(spot)
		except IndexError :
			print(len(spot),self.ply_no)
			return len(spot)
		else :
			frm= index['frm']
		#print(index)
		for key in index:
			if type(key) == int:
				side = jump.make_move(self.board ,index,key, frm)
				return side
	def toggle_ply(self):
		self.ply_no = 3 - self.ply_no
	def get_opponent(self):
		return 3 - self.ply_no 
	def add_score(self , score):
		if self.w_score != -math.inf:
			self.w_score += score
	def count_player(self):
		player_red_1 = 0
		player_black_2 = 0
		for key in range(len(self.board)) :
			if self.board[key] == 'RED':
				player_red_1 += 5
			if self.board[key] == 'red':
				player_red_1 += 1
			if self.board[key] == 'BLACK':
				player_black_2 += 5
			if self.board[key] == 'black':
				player_black_2 += 1
		return [player_red_1 , player_black_2]
	def check(self , oldred , oldblack ):
		newred , newblack = self.count_player()
		if oldred > newred :
			return 2,(oldred-newred)
		if oldblack > newblack :
			return 1,(oldblack-newblack)
		if newred == 0 or newblack == 0:
			return 0,0
		else :
			return -1,1

class Monte:
	def draw(self,board):
		print()
		for spot in range(9):
			if board[spot] == 0 :
				board[spot] = '•'
			print( ' |<{}>|'.format(board[spot]),end="")
			if spot == 8 or spot == 2 or spot == 5:
				print()
			if board[spot] == '•' :
				board[spot] = 0
		print()
		
	def find_next_move(self,board , plyno , Node):
		opponent = 3 - plyno 
		rootnode = Node()
		rootnode.board = board
		rootnode.ply_no = opponent
		simulation = 100
		while simulation != 0:
			promising_node = self. select_promising_node(rootnode)
			if promising_node.check(0,0)[0] == -1 :
				self.expand(promising_node)
			node_playing = promising_node

			if len(node_playing.child) > 0:
				node_playing = promising_node.get_random_child()
				#jump.draw(node_playing.board)
				#print()
			result = self.simulate(node_playing , opponent )
			#print(result)
			self.back_trace(node_playing , result ,opponent)
			simulation -= 1
		winner = rootnode.get_child_max()
		#for key in rootnode.child:
			#jump.draw(key.board)
			#print(key.v_count,key.w_score)
		Node = winner
		return Node
		
	def select_promising_node(self,node):
		node_check = node
		while len(node_check.child) != 0:
			node_check  = self.find_best_node_uct(node_check)
		return node_check
	
	def expand(self, node):
		states = node.get_possible_state()
		#print(node)
		for state in states:
			new_node = Node(board = state)
			new_node.parent = node
			new_node.ply_no = node.get_opponent()
			node.child.append(new_node)
			
	def back_trace(self , node,  result,opponent ):
		_node = node 
		while _node != None :
			_node.v_count +=1
			if 3-opponent  == result[0] :
				score = 10*result[1]
				_node.add_score(score)
			if opponent == result[0]:
				_node.add_score(-math.inf)
			_node = _node.parent
			
	def simulate(self,node , opponent ):
			fake_node = Node()
			fake_node.board =[spot for spot in node.board ]
			fake_node.parent = node.parent
			fake_node.v_count = node.v_count
			fake_node.child = node.child
			fake_node.ply_no = node.ply_no
			fake_node.w_score = node.w_score
			red, black = node.parent.count_player()
			status = fake_node.check(red,black) 
			if status[0] == opponent :
				fake_node.parent.w_score = -math.inf
				fake_node.w_score = -math.inf
				return status
			if status[0] == 3-opponent :
				fake_node.parent.w_score=math.inf
				fake_node.w_score = math.inf
				return status 
			count = 15
			ret = 1
			while count != 0 and ret != 0 :
				fake_node.toggle_ply()
				rd, blk = fake_node.count_player()
				ret = fake_node.random_play()
				status = fake_node.check(rd,blk)
				count -= 1
			#print(status)
			return status 
			
			
	def find_best_node_uct(self,node):
		parent_visit = node.v_count
		child_uct = []
		for child in node.child:
			result = self.uct_value(parent_visit,child.w_score , child.v_count )
			child_uct.append(result)
		big = max(child_uct)
		return node.child[child_uct.index(big)]
			
	def uct_value(self,p_visit , chd_w_score , chd_v_count):
		if chd_v_count == 0:
			return math.inf
		return (chd_w_score/chd_v_count) + 1.41 * math.sqrt(math.log(p_visit)/chd_v_count)


#new = Monte()
red = Node(ply_no=1,board=board)
red.get_avaliable_spot()
#board = new.find_next_move(board,1,Node)
#jump.draw(board.board)
'''for b in board :
	jump.draw(b)
	print()'''
'''board = new.get_possible_state()'''
'''
def aitest():
	global board 
	board = board 
	AI = Monte()
	player = 1
	result = -1
	while result == -1:
		game = AI.find_next_move(board,player,Node)
		player = 3 - player 
		board = game.board
		jump.draw(game.board)
		print()
		result = game.check(0,0)
		
		if result != -1:
			break 
		

#aitest()
'''