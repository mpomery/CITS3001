#!/usr/bin/python

# Threes (threes.py)
# Written by Mitchell 'Pommers' Pomery (21130887)
#
# All the things required to play a game of threes

import math
import copy

# Pretends we have rotated the board so a movement left means a movement
# in the defined ULDR
def getxy(x, y, udlr):
	if udlr in ['R', 'D']:
		y = 3 - y
	if udlr in ['U', 'D']:
		x, y = y, x
	return (x, y)

# Moves all tiles on the board in the specified direction. Then adds the new
# tile
def domove(boardin, move, nexttile):
	# Treat everything as a left shift. Just "rotate" values to change them
	# We can do this with the magic of getyx()!
	# Which runs in O(1) time and O(1) memory to be super cool!
	# everything moves "left". deal with it row by row
	board = copy.deepcopy(boardin)
	possible=[]
	for i in range(4):
		for j in range(3):
			x, y = getxy(i, j, move)
			xn, yn = getxy(i, j + 1, move)
			# Should figure out how to remove the need for the next line
			if max(x, y, xn, yn) != 4 and min(x, y, xn, yn) != -1:
				# IF
				# Next Position not 0 AND
				#   current position is zero OR
				#   both pieces match. Aren't 1's or 2's OR
				#   pieces are a 1 and a 2
				if board[xn][yn] != 0 and \
				(board[x][y] == 0 or \
				(board[x][y] == board[xn][yn] and board[x][y] not in [1, 2])or \
				sorted((board[x][y], board[xn][yn])) == [1, 2]):
					board[x][y] += board[xn][yn]
					board[xn][yn] = 0
					if i not in possible:
						possible.append(i)
	# If there is nowhere to place tile, exit now
	if len(possible) == 0:
		return None
	# Working backward, place the new tile
	i = 3
	while len(possible) > 0 and i >= 0:
		cells = []
		vals = []
		# Narrow down the locations for the new tile
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
	possible = min(possible)
	x, y = getxy(possible, 3, move)
	board[x][y] = nexttile
	return board

# Print the board to the command line for debugging
def printboard(board):
	for i in range(4):
		print(''.join(str(board[i][j]).ljust(5) for j in range(4)))

# Calculate the score for a board
def scoreboard(board):
	score = 0
	if board == None:
		return -1
	for i in range(4):
		for j in range(4):
			if board[i][j] in [1, 2]:
				score += 1
			elif board[i][j] != 0:
				score += int(math.pow(3, math.log(board[i][j]/3, 2) + 1))
	return score

def freespaces(board):
	free = 0
	for i in range(4):
		for j in range(4):
			if board[i][j] == 0:
				free += 1
	return free

def usedspaces(board):
	used = 0
	for i in range(4):
		for j in range(4):
			if board[i][j] != 0:
				used += 1
	return used

def linedup(board):
	utility = 1
	for i in range(4):
		if ((board[i][0] >= board[i][1] >= board[i][2] >= board[i][3]) or
			(board[i][0] <= board[i][1] <= board[i][2] <= board[i][3])):
			utility *= 2
		if ((board[0][i] >= board[1][i] >= board[2][i] >= board[3][i]) or
			(board[0][i] <= board[1][i] <= board[2][i] <= board[3][i])):
			utility *= 2
	return utility

def ringsum(board):
	utility = 0
	for i in range(4):
		utility += board[i][0] + board[0][i] + board[i][3] + board[3][i]
	utility -= board[0][0] + board[0][3] + board[3][0] + board[3][3]
	return utility

#def coresum(board):
#	utility = 0
#	for i in range(2):
#		utility += board[1][i+1] + board[2][i+1]
#	return utility

#def edgeheavy(board):
#	utility = 0
#	if board[0][1] > board[1][1]:
#		utility += 2
#	if board[0][2] > board[1][2]:
#		utility += 2
#	if board[1][0] > board[1][1]:
#		utility += 2
#	if board[2][0] > board[2][1]:
#		utility += 2
#	if board[1][3] > board[1][2]:
#		utility += 2
#	if board[2][3] > board[2][2]:
#		utility += 2
#	if board[3][1] > board[2][1]:
#		utility += 2
#	if board[3][2] > board[2][2]:
#		utility += 2
#	return utility

#def united(board):
#	utility = 1;
#	for i in range(4):
#		for j in range(2):
#			if not(board[i][j+1] < board[i][j] and board[i][j+1] < board[i][j+2]):
#				utility *= 2
#			if not(board[j+1][i] < board[j][i] and board[j+1][i] < board[j+2][i]):
#				utility *= 2
#	return utility
#
