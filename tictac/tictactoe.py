
#human_player =int(input('write something ')) https://docs.djangoproject.com/en/4.0/intro/reusable-apps/  https://codingshiksha.com/javascript/how-to-build-html-live-editor-like-w3schoolsvscodecodepen-in-javascript-full-project/  https://codepen.io/tutsplus/pen/QNeJgR
board = [0 ,1 ,2 ,3,4,5,6,7,8]
ai = 'X'
hu = 'D'
def minimax(fboard,ply):
	moves = get_avaliable_moves(fboard)
	if winning(fboard,ai) :
		return {'score' : 10}
	elif winning(fboard,hu) :
		return {'score' : -10 }
	elif len(get_avaliable_moves(fboard)) == 0 :
		return {'score' : 0}
	
	all_moves = []
	for m in moves :
		data = {}
		data['index'] = m 
		fboard[m] = ply
		if ply == ai :
			evaluate = minimax(fboard,'D')['score']
			data['score'] = evaluate 
		else :
			evaluate = minimax(fboard,'X')['score']
			data['score'] = evaluate 
		fboard[m] = data['index']
		all_moves.append(data)
		
	bestmove = None
	if ply == 'X' :
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

def winning(fboard,ply):
	pwinning = [
							[0,1,2],	[3,4,5],	[6,7,8],	[0,4,8],
					    	[2,4,6],	[0,3,6],	[1,4,7],	[2,5,8],
						]
	for wins in pwinning :
		a , b , c = wins
		if fboard[a] == ply and fboard[b] == ply and fboard[c] == ply :
			return True			
			
def get_avaliable_moves(fboard):
	empty_spot = []
	for moves in fboard :
		if moves  != 'X' and moves  != 'D' :
			empty_spot.append(moves)
	return empty_spot 
	
#def avaliable_moves(fboard,ply):
#	moves = []
#	for spot in get_avaliable_moves(fboard) :
#		kboard = deepcopy(fboard)
		#kboard[spot] = ply
#		moves.append(kboard)
#	return moves

def deepcopy(fboard):
	kboard = []
	for b in range (9):
		kboard.append(fboard[b])
	return kboard 

def draw(fboard):
	kboard = deepcopy(fboard)
	for l in range(9):
		if kboard[ l ] == l :
			kboard[ l ] = '•'
		if l < 3 :
			print( '| <{}> |'.format(kboard[l] ),end = "")
			if l == 2:
				print()
		if l >= 3 and l < 6 :
			print( '| <{}> |'.format(kboard[l] ),end = "")
			if l == 5:
				print()
		if l >= 6:
			print( '| <{}> |'.format(kboard[l] ),end = "")
			if l == 8 :
				print()
			

def play_game(position):
	free_spot = get_avaliable_moves(position)
	print('This is the avaliable moves:  '+str(free_spot))
	get_input = int(input('write something make sure it is in the avaliable moves: '))
	if get_input in free_spot and not winning(position,ai) :
		position[get_input] = hu
		draw(position)
		if len(get_avaliable_moves(position)) != 0 :
			if not winning(position,ai) and not winning(position,hu):
				print('ai')
				value = minimax(position,ai)
				position[value['index']] = ai
				draw(position)
				print()
				if winning(position , ai ):
					print('AI won')
				else :
					play_game(position)
		elif len(get_avaliable_moves(position)) == 0 :
			print('\n'+'Draw')
	else :
		play_game(position)
		
		
play_game(board)
#print(evaluation(board))
#position = minimax(board, 2 ,True)[1]
#draw(position)
