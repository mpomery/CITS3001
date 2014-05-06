#!/usr/bin/python

# Threes Bot (threesbot.py)
# Written by Mitchell 'Pommers' Pomery (21130887)

import sys
import math

def main():
	# Load Data from input file arg
	# We saddume the input is correctly formatted
	if len(sys.argv) != 3:
		print("Usage:\n\tthreesbot.py input output\n")
		return 1
	else:
		# This stuff is Pythonic!
		tiles = []
		input = open(sys.argv[1], "r")
		input.readline() # First 2 lines are comments
		input.readline()
		board = [map(int, input.readline().strip().split()) for i in range(4)]
		for line in input:
			print(line)
			map(tiles.append, map(int, line.split()))
		input.close()
		print(str(tiles))
		printboard(board)
		print("score: " + str(scoreboard(board)))
		play(board, tiles)

def getxy(x, y, udlr):
	# Pretends we have rotated the board so a movement left means a movement
	# in the defined ULDR
	if udlr in ['R', 'D']:
		# reverse y values
		y = 3 - y
	if udlr in ['U', 'D']:
		# swap x and y values
		x, y = y, x
	return (x, y)

def domove(board, move, nexttile):
	# Treat everything as a left shift. Just "rotate" values to change them
	# We can do this with the magic of getyx()!
	# Which runs in O(1) time and O(1) memory to be super cool!
	
	possible=[]
	for i in range(4):
		# everything moves "left". deal with it row by row
		for j in range(3):
			x, y = getxy(i, j, move)
			xn, yn = getxy(i, j + 1, move)
			if max(x, y, xn, yn) != 4 and min(x, y, xn, yn) != -1:
				#print(move + str(i) + str(j) + str(x) + str(y) + str(xn) + str(yn))
				#if board[x][y] == board[xn][yn] or board[x][y] == 0 or sorted((board[x][y], board[xn][yn])) == [1, 2]:
				if board[xn][yn] != 0 and \
				(board[x][y] == 0 or \
				(board[x][y] == board[xn][yn] and board[x][y] not in [1, 2])or \
				sorted((board[x][y], board[xn][yn])) == [1, 2]):
					# equal. combine them
					# this square is empty. try fill it.
					# 1 and 2 merge
					board[x][y] += board[xn][yn]
					board[xn][yn] = 0
					if i not in possible:
						possible.append(i)
					#print(str(x) + str(y) + str(xn) + str(yn))
	# Lexographical score
	# What we need to do here:
	# With a list of all cells that 
	# Starting at the "right" most position of the row, find the lowest number
	# remove any not that number
	# move "left" one until there is only one possible position
	#print("p: " + str(possible))
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
			#print(str(i) + " " + str(minimum) + " " + str(r[0]) + " " + str(r[1]))
			if r[1] != minimum:
				possible.remove(r[0])
		#print(str(i) + " " + str(possible))
		i -= 1
	# We have narrowed down the possible locations now
	if len(possible) != 0:
		possible = min(possible)
	x, y = getxy(possible, 3, move)
	board[x][y] = nexttile
	return board

def printboard(board):
	for i in range(4):
		print(''.join(str(board[i][j]).ljust(3) for j in range(4)))

def printboardrotated(board, rotation):
	for i in range(4):
		for j in range(4):
			x, y = getxy(i, j, rotation)
			print(''.join(str(board[x][y]).ljust(3)))

def scoreboard(board):
	score = 0
	for i in range(4):
		for j in range(4):
			if board[i][j] in [1, 2]:
				score += 1
			elif board[i][j] != 0:
				score += int(math.pow(3, math.log(board[i][j]/3, 2) + 1))
	return score

def play(board, tiles):
	"""moves = "UDRRRRUUDDDRLLLUUDDULRLUDDRRRDRUUULLUUURRRUURULLLLURULUULULURUUURUULULURUR"
	for i in range(len(moves)):
		print("Move: " + str(i + 1))
		move = moves[i]
		tile = tiles[i]
		board = domove(board, move, tile)
		print(move)
		printboard(board)
		print("added tile: " + str(tiles[i]))
		print("score: " + str(scoreboard(board)))
		print('')
		#raw_input()"""
	for nexttile in tiles:
		qt = QuadTree(0)
		

class QuadTree:
	left = None
	right = None
	up = None
	down = None
	score = 0
	def __init__(self, s):
		score = s
	
	

if __name__ == '__main__':
	main()
