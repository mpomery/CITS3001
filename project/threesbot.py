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

def domove(board, move):
	if move == "L":
		pass
	return board

def printboard(board):
	#print(str("a").ljust(3))
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
	"""score(empty) = 0 
	score(1) = score(2) = 1 
	score(x) = 3 ^ (log2(x / 3) + 1), x > 2 """
	
	
	return score

def play(board, tiles):
	pass

if __name__ == '__main__':
	main()
