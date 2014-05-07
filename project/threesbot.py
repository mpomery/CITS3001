#!/usr/bin/python

# Threes Bot (threesbot.py)
# Written by Mitchell 'Pommers' Pomery (21130887)

import sys
import threes

def main():
	# Load Data from input file arg
	# We assume the input is correctly formatted
	if len(sys.argv) != 3:
		print("Usage:\n\tthreesbot.py input output\n")
		print("\tinput\tInput File")
		print("\toutput\tOutput File")
		print("\n")
		return 1
	else:
		# This stuff is Pythonic!
		tiles = []
		input = open(sys.argv[1], "r")
		input.readline() # First 2 lines are comments
		input.readline()
		# Read in the board
		board = [map(int, input.readline().strip().split()) for i in range(4)]
		# Read in the tiles
		for line in input:
			map(tiles.append, map(int, line.split()))
		input.close()
		play(board, tiles)

def play(board, tiles):
	moves = "UDRRRRUUDDDRLLLUUDDULRLUDDRRRDRUUULLUUURRRUURULLLLURULUULULURUUURUULULURUR"
	for i in range(len(moves)):
		print("Move: " + str(i + 1))
		move = moves[i]
		tile = tiles[i]
		board = threes.domove(board, move, tile)
		print(move)
		threes.printboard(board)
		print("added tile: " + str(tiles[i]))
		print("score: " + str(threes.scoreboard(board)))
		print('')
		#raw_input()

if __name__ == '__main__':
	main()
