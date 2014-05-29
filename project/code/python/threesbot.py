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
			(moves, finalboard) = astar(boardout, tiles)
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

# http://en.wikipedia.org/wiki/A*_search_algorithm#Pseudocode
def astar(board, tiles):
	i = 0;
	output = "";
	while i < len(tiles):
		move = astarmove(board, tiles[i:])
		if move == "":
			return (output, board)
		board = threes.domove(board, move, tiles[i])
		#threes.printboard(board)
		#print(threes.scoreboard(board))
		output += move
		#print(output)
		i += 1
	return (output, board)

def astarmove(board, tiles):
	output = ""
	closed = []
	open = [(board, "")]
	maxscore = threes.scoreboard(board)
	maxpath = ""
	
	time1 = time.time()
	
	#print(len(tiles))
	while len(open) > 0 and time.time() - time1 < 0.15:
		#print(open)
		#print(closed)
		current = open.pop(0)
		#print(current)
		#print(current[0])
		#print(threes.scoreboard(current[0]))
		#print(len(open))
		#print(len(current[1]))
		if len(current[1]) == len(tiles):
			pass
		else:
			qt = QuinaryTree.QuinaryTree(current[0])
			qt.makeleaves(tiles[len(current[1])])
			factor = 0.75
			if qt.left.board != None:
				if qt.left.score >= factor * maxscore:
					maxscore = max(maxscore, qt.left.score)
					if maxscore == qt.left.score:
						maxpath = current[1] + "L"
					open.append((qt.left.board, current[1] + "L"))
			if qt.right.board != None:
				if qt.right.score >= factor * maxscore:
					maxscore = max(maxscore, qt.right.score)
					if maxscore == qt.right.score:
						maxpath = current[1] + "R"
					open.append((qt.right.board, current[1] + "R"))
			if qt.up.board != None:
				if qt.up.score >= factor * maxscore:
					maxscore = max(maxscore, qt.up.score)
					if maxscore == qt.up.score:
						maxpath = current[1] + "U"
					open.append((qt.up.board, current[1] + "U"))
			if qt.down.board != None:
				if qt.down.score >= factor * maxscore:
					maxscore = max(maxscore, qt.down.score)
					if maxscore == qt.down.score:
						maxpath = current[1] + "D"
					open.append((qt.down.board, current[1] + "D"))
			closed.append(current)
			#print(open)
			#print(closed)
	
	if len(maxpath) == 0:
		return ""
	return maxpath[0]
	
	#print(len(open))
	#print(len(closed))
	
	# Prune non complete level
	"""if len(open) == 0:
		return ""
	
	maxlength = 0
	for o in open:
		maxlength = max(maxlength, len(o[1]))
	#print(maxlength)
	
	i = len(open) - 1
	while i >= 0:
		if len(open[i][1]) != maxlength:
			open.pop(i)
		i -= 1
	
	left = 0
	right = 0
	up = 0
	down = 0
	
	#print(len(open))
	#print(closed)
	for b in open:
		if b[1][0] == "L":
			left += 1
		if b[1][0] == "R":
			right += 1
		if b[1][0] == "U":
			up += 1
		if b[1][0] == "D":
			down += 1
		#print(b[0])
		#print(b[1])
		#print(threes.scoreboard(b[0]))
	#print("Left: " + str(left))
	#print("Right: " + str(right))
	#print("Up: " + str(up))
	#print("Down: " + str(down))
	
	maximum = max(left, right, up, down)
	if maximum == 0:
		return ""
	if left == maximum:
		return "L"
	if right == maximum:
		return "R"
	if up == maximum:
		return "U"
	if down == maximum:
		return "D"
	"""

# If called from the command line, run main
if __name__ == '__main__':
	main()
