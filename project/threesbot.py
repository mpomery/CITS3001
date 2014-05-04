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
		printboard(board)
		for line in input:
			map(tiles.append, map(int, line.strip().split()))
		input.close()
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
	for i in range(4):
		# everything moves "left". deal with it row by row
		# start is second position
		for j in range(4):
			x, y = getxy(i, j, move)
			xn, yn = getxy(i, j + 1, move)
			if max(x, y, xn, yn) != 4:
				#print(move + str(i) + str(j) + str(x) + str(y) + str(xn) + str(yn))
				if board[x][y] == board[xn][yn]:
					# equal. combine them
					board[x][y] += board[xn][yn]
					board[xn][yn] = 0
				elif board[x][y] == 0:
					# this square is empty. try fill it.
					board[x][y] += board[xn][yn]
					board[xn][yn] = 0
					# possibly merge these last two...
				elif sorted((board[x][y], board[xn][yn])) == (1, 2):
					#Merge them again!
					board[x][y] += board[xn][yn]
					board[xn][yn] = 0
					# We could combine these all!
	
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
	moves = "UDLR"
	for i in range(len(moves)):
		move = moves[i]
		tile = tiles[i]
		board = domove(board, move, tile)
		print(move)
		printboard(board)
		print("score: " + str(scoreboard(board)))
		print('')

if __name__ == '__main__':
	main()
