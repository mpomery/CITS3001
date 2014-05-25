#!/usr/bin/python

# Threes Bot (threesbot.py)
# Written by Mitchell 'Pommers' Pomery (21130887)

# A bot to play threes and aim to get the best score, knowing what tiles are
# coming up

import sys
import copy
import time
import threes
import QuinaryTree

# Some magic for timing the playthrough
# Stolen From: http://stackoverflow.com/a/5478448
def timing(f):
	def wrap(*args):
		time1 = time.time()
		ret = f(*args)
		time2 = time.time()
		print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
		return ret
	return wrap

# Main function. Loads the input file
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
		
		for i in range(1):
			boardout = copy.deepcopy(board)
			(moves, finalboard) = naive(boardout, tiles)
			if i is 0:
				threes.printboard(finalboard)
				print("Score: " + str(threes.scoreboard(finalboard)))
				print(moves)
				output = open(sys.argv[2], "w")
				output.write("\n")
				output.write("\n")
				output.write(moves)

# Niave bot. Will find the best move then make it.
@timing
def naive(board, tiles):
	i = 0
	output = ""
	while i < len(tiles):
		qt = QuinaryTree.QuinaryTree(board)
		qt.makeleaves(tiles[i])
		
		if qt.left.board == None and qt.right.board == None and \
		qt.up.board == None and qt.down.board == None:
			return(output, board)
		
		maximum = max(qt.left.score, qt.right.score, qt.up.score, qt.down.score)
		if (maximum == qt.left.score):
			board = qt.left.board
			output += "L"
		elif (maximum == qt.right.score):
			board = qt.right.board
			output += "R"
		elif (maximum == qt.up.score):
			board = qt.up.board
			output += "U"
		elif (maximum == qt.down.score):
			board = qt.down.board
			output += "D"
		i += 1
	return(output, board)

# If called from the command line, run main
if __name__ == '__main__':
	main()
