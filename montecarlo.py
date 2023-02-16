import random 
import math 

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
		return self.child[random.randint(0,len(self.child)-1)]
		
	def get_avaliable_spot(self):
		empty_spot = []
		for k in range(len(self.board)):
			if self.board[k] == 0:
				empty_spot.append(k)
		return empty_spot
		
	def make_move(self , board, ply, spot):
		board[spot] = ply
		return board
		
	def get_possible_state(self):
		state = []
		free_spot = self.get_avaliable_spot()
		for key in free_spot:
			new_board = [spot  for spot in self.board]
			new_ply_no = 3 - self.ply_no
			result = self.make_move(new_board,new_ply_no,key)
			state.append(result)
		return state 
		
	def get_child_max(self):
		score_array = []
		for key in self.child:
			score_array.append(key.v_count)
		max_score = max(score_array)
		index = score_array.index(max_score)
		return self.child[index]
		
	def random_play(self):
		spot = self.get_avaliable_spot()
		index = spot[random.randint(0,len(spot)-1)]
		self.make_move(self.board , self.ply_no,index)
	def toggle_ply(self):
		self.ply_no = 3 - self.ply_no
	def get_opponent(self):
		return 3 - self.ply_no 
	def add_score(self , score):
		if self.w_score != -math.inf:
			self.w_score += score
	def check(self):
		win = [ [0, 1, 2],  [3, 4, 5],   [6, 7, 8],   [0, 3, 6],   [1, 4, 7],
					 [2, 5, 8],  [0, 4, 8],   [2, 4, 6]    ];
		for key in win :
			fx = self.board
			a, b, c = key
			if fx[a] == fx[b] and fx[b] == fx[c] and fx[c] == 1:
				return 1
			if fx[a] == fx[b] and fx[b] == fx[c] and fx[c] == 2:
				return 2
		if len(self.get_avaliable_spot()) > 0:
			return -1
		if len(self.get_avaliable_spot()) == 0:
			return 0

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
		#global Node 
		rootnode = Node()
		rootnode.board = board
		rootnode.ply_no = opponent 
		simulation = 1000
		while simulation != 0:
			promising_node = self. select_promising_node(rootnode)
			if promising_node.check() == -1 :
				self.expand(promising_node)
			node_playing = promising_node

			if len(node_playing.child) > 0:
				node_playing = promising_node.get_random_child()
			result = self.simulate(node_playing , opponent )
			self.back_trace(node_playing , result )
			simulation -= 1
		winner = rootnode.get_child_max()
		Node = winner 
		return Node
		
	def select_promising_node(self,node):
		node_check = node
		while len(node_check.child) != 0:
			node_check  = self.find_best_node_uct(node_check)
		return node_check
	
	def expand(self, node):
		states = node.get_possible_state()
		for state in states:
			new_node = Node(board = state)
			new_node.parent = node
			new_node.ply_no = node.get_opponent()
			node.child.append(new_node)
			
	def back_trace(self , node,  result ):
		fake_n = node 
		while fake_n != None :
			fake_n.v_count +=1
			if fake_n.ply_no == result :
				fake_n.add_score(1)
			fake_n = fake_n.parent
			
	def simulate(self,node , opponent ):
			fake_node = Node()
			fake_node.board =[node for node in node.board ]
			fake_node.parent = node.parent
			fake_node.v_count = node.v_count
			fake_node.child = node.child
			fake_node.ply_no = node.ply_no
			fake_node.w_score = node.w_score
			status = fake_node.check() 
			if status == opponent :
				fake_node.parent.w_score = -math.inf
				return status
			while status == -1:
				fake_node.toggle_ply()
				fake_node.random_play()
				status = fake_node.check()
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
		
def aitest():
	board = [0,0,0,0,0,0,0,0,0]
	AI = Monte()
	player = 1
	for key in range(9):
		result = AI.find_next_move(board,player,Node)
		player = 3 - player 
		board = result.board
		AI.draw(result.board)
		print(result.check())
		if result.check() != -1:
			break 
		

aitest()