
def drawsquare(width , height ):
	for h in range(height):
		for j in range (width):
			if h == 0 or h == height-1 :
				print(' *' ,end="")
			if j == width-1 and h == 0 :
				print()
		if h > 0 and h < height-1 :
			print(" *"+" "*((width-2)*2+1)+'* ')

drawsquare( 22 , 22 )		
			#for l in range (9):
for k in range (20,0,-1):
		#print(k)
		print(" "*(k//2)+"🔥"*(20-k))