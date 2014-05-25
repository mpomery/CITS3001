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
@timing
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
		for i in range (100):
			boardout = copy.deepcopy(board)
			(moves, finalboard) = naive(boardout, tiles)
			threes.printboard(finalboard)
			print(moves)
			print("")
			print("")

# The bot itself
def naive(board, tiles):
	i = 0
	output = ""
	#print(tiles)
	#raw_input()
	while i < len(tiles):
		#if i >= 48:
		#	raw_input()
		#print(board)
		qt = QuinaryTree.QuinaryTree(board)
		#qt.printqt()
		qt.makeleaves(tiles[i])
		#print(i)
		#print(len(tiles))
		
		if qt.left.board == None and qt.right.board == None and qt.up.board == None and qt.down.board == None:
			#print("Nones!")
			return(output, board)
		
		maximum = max(qt.left.score, qt.right.score, qt.up.score, qt.down.score)
		
		if (maximum == qt.left.score):
			#print("Moved: Left")
			board = qt.left.board
			#print(board)
			output += "L"
		elif (maximum == qt.right.score):
			#print("Moved: Right")
			board = qt.right.board
			#print(board)
			output += "R"
		elif (maximum == qt.up.score):
			#print("Moved: Up")
			board = qt.up.board
			#print(board)
			output += "U"
		elif (maximum == qt.down.score):
			#print("Moved: Down")
			board = qt.down.board
			#print(board)
			output += "D"
		i += 1
		#print("")
	#print("")
	#print("")
	#print(output)
	return(output, board)
	
	"""moves = "UDRRRRUUDDDRLLLUUDDULRLUDDRRRDRUUULLUUURRRUURULLLLURULUULULURUUURUULULURUR"
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
		#raw_input()"""

# If called from the command line, run main
if __name__ == '__main__':
	main()
