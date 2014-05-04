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
		nexttile = []
		input = open(sys.argv[1], "r")
		input.readline() # First 2 lines are comments
		input.readline()
		board = [map(int, input.readline().strip().split()) for i in range(4)]
		printboard(board)
		for line in input:
			map(nexttile.append, map(int, line.strip().split()))
		input.close()
		print("score: " + str(scoreboard(board)))
		play(board, nexttile)

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

def domove(board, move):
	# Treat everything as a left shift. Just "rotate" values to change them
	# We can do this with the magic of getyx()!
	# Which runs in O(1) time and O(1) memory to be super cool!
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
	pass

if __name__ == '__main__':
	main()
