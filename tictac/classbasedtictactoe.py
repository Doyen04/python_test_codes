
class Game:
	HU = 'X'
	AI = 'D'
	def __init__(self):
		self.state = [0,1,2,3,4,5,6,7,8]
		self.turn = 1
		#self.get_input()
	def minimax(self,ply):
		moves = self.avaliable_spot()
		if self.winning(self.AI) :
			return {'score' : 10}
		elif self.winning(self.HU) :
			return {'score' : -10 }
		elif len(self.avaliable_spot()) == 0 :
			return {'score' : 0}
	
		all_moves = []
		for m in moves :
			data = {}
			data['index'] = m 
			self.state[m] = ply
			if ply == self.AI:
				evaluate = self.minimax(self.HU)['score']
				data['score'] = evaluate 
			else :
				evaluate = self.minimax(self.AI)['score']
				data['score'] = evaluate 
			self.state[m] = data['index']
			all_moves.append(data)
		
		bestmove = None
		if ply == self.AI:
			bestscore = -9999
			for l in all_moves :
				score = l['score']
				if score > bestscore :
					bestscore = l['score']
					bestmove = l
		else :
			bestscore = 9999
			for l in all_moves :
				if l['score'] < bestscore :
					bestscore = l['score']
					bestmove = l
		return bestmove
	def __draw_board(self):
		print()
		for spot in range(9):
			if self.state[spot] == spot :
				self.state[spot] = '•'
			print( ' |<{}>|'.format(self.state[spot]),end="")
			if spot == 8 or spot == 2 or spot == 5:
				print()
			if self.state[spot] == '•' :
				self.state[spot] = spot
		print()
	def avaliable_spot(self):
		spot = []
		for x in self.state:
			if x != 'X' and x != 'D':
				spot.append(x)
		return spot 
	def winning(self,ply):
		pwinning = [
							[0,1,2],	[3,4,5],	[6,7,8],	[0,4,8],
					    	[2,4,6],	[0,3,6],	[1,4,7],	[2,5,8],
						]
		fboard = self.state
		for wins in pwinning :
			a , b , c = wins
			if fboard[a] == ply and fboard[b] == ply and fboard[c] == ply :
				return True	
	def make_move(self,num,ply):
		self.state[num] = ply
		
	def get_input(self):
		spot = self.avaliable_spot()
		if len(spot) == 9:
			self.__draw_board()
		print('Available spots : '+str(spot))
		nums = int(input('Enter something that is in the : ' ))
		if nums in spot and not self.winning(self.AI):
			self.make_move(nums , self.HU)
			self.__draw_board()
			spot = self.avaliable_spot()
			if len(spot) != 0 and not self.winning(self.HU):
				print('AI TURN THINKING\n')
				cord = self.minimax(self.AI)['index']
				self.make_move(cord , self.AI)
				self.__draw_board()
				spot = self.avaliable_spot()
			elif len(spot) == 0:
				print('draw \n')
			if len(spot) != 0 and not self.winning(self.AI):
				self.get_input()
			elif self.winning(self.AI):
				print('AI WON')
		else :
			print(' Spot not defined \n')
			self.get_input()
#game = Game()
#print('second game start')
#second = Game()
#print(game.minimax('D')['index'])
