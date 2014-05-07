import math

def getxy(x, y, udlr):
	# Pretends we have rotated the board so a movement left means a movement
	# in the defined ULDR
	if udlr in ['R', 'D']:
		y = 3 - y
	if udlr in ['U', 'D']:
		x, y = y, x
	return (x, y)

def domove(board, move, nexttile):
	# Treat everything as a left shift. Just "rotate" values to change them
	# We can do this with the magic of getyx()!
	# Which runs in O(1) time and O(1) memory to be super cool!
	# everything moves "left". deal with it row by row
	possible=[]
	for i in range(4):
		for j in range(3):
			x, y = getxy(i, j, move)
			xn, yn = getxy(i, j + 1, move)
			if max(x, y, xn, yn) != 4 and min(x, y, xn, yn) != -1:
				if board[xn][yn] != 0 and \
				(board[x][y] == 0 or \
				(board[x][y] == board[xn][yn] and board[x][y] not in [1, 2])or \
				sorted((board[x][y], board[xn][yn])) == [1, 2]):
					board[x][y] += board[xn][yn]
					board[xn][yn] = 0
					if i not in possible:
						possible.append(i)
	i = 3
	while len(possible) > 0 and i >= 0:
		cells = []
		vals = []
		for row in possible:
			x, y = getxy(row, i, move)
			cells.append([row, board[x][y]])
			vals.append(board[x][y])
		minimum = min(vals)
		for r in cells:
			if r[1] != minimum:
				possible.remove(r[0])
		i -= 1
	# We have narrowed down the possible locations now
	if len(possible) == 0:
		# No where to place tile
		return None
	elif len(possible) != 0:
		possible = min(possible)
	x, y = getxy(possible, 3, move)
	board[x][y] = nexttile
	return board

def printboard(board):
	for i in range(4):
		print(''.join(str(board[i][j]).ljust(3) for j in range(4)))

def scoreboard(board):
	score = 0
	for i in range(4):
		for j in range(4):
			if board[i][j] in [1, 2]:
				score += 1
			elif board[i][j] != 0:
				score += int(math.pow(3, math.log(board[i][j]/3, 2) + 1))
	return score