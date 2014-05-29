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
#import psutil
import os

functime = 1

# Some magic for timing the playthrough
# Stolen From: http://stackoverflow.com/a/5478448
def timing(f):
	def wrap(*args):
		global functime
		time1 = time.time()
		ret = f(*args)
		time2 = time.time()
		functime = (time2-time1)*1000.0
		print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
		return ret
	return wrap

# Main function. Loads the input file
def main(infile, outfile):
	# Up out process priority
	#p = psutil.Process(os.getpid())
	#p.set_nice(psutil.HIGH_PRIORITY_CLASS)
	# Load Data from input file arg
	# We assume the input is correctly formatted

	# This stuff is Pythonic!
	tiles = []
	input = open(infile, "r")
	input.readline() # First 2 lines are comments
	input.readline()
	# Read in the board
	board = [map(int, input.readline().strip().split()) for i in range(4)]
	# Read in the tiles
	for line in input:
		map(tiles.append, map(int, line.split()))
	input.close()
	
	boardout = copy.deepcopy(board)
	(moves, finalboard) = astar(boardout, tiles)
	print(finalboard)
	threes.printboard(finalboard)
	print("Score: " + str(threes.scoreboard(finalboard)))
	print(moves)
	print(str(len(moves)) + " moves made in " + str(functime) + "ms")
	print("OR")
	print(str(len(moves)/(functime/1000.0)) + " moves per second")
	output = open(outfile, "w")
	output.write("ThreesBot\n")
	output.write("By Mitchell Pomery (21130887) and Kieran Hannigan (21151118)\n")
	output.write(moves)

# Niave bot. Will find the best move then make it.
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
@timing
def astar(board, tiles):
	i = 0;
	output = "";
	while i < len(tiles):
		move = astarmoves(board, tiles[i:])
		if move == "":
			return (output, board)
		else:
			print(move)
		board = threes.domove(board, move, tiles[i])
		output += move
		i += 1
		print(output)
	return (output, board)

def astarmoves(board, tiles):
	lookahead = min(5, len(tiles))
	nextXtiles = tiles[0:lookahead]
	if board == None:
		return ""
	print(nextXtiles)
	print(board)
	naiveX = naive(board, nextXtiles)
	scorenaive = threes.scoreboard(naiveX[1]) # f(n)
	#print(naiveX)
	#print(scorenaive)
	#print(nextXtiles)
	
	if len(naiveX[0]) == 0:
		return ""
	
	closed = []
	open = [(board, "")]
	
	depth = 0
	while len(open) > 0 and depth < lookahead: #and time.time() - starttime < 0.19:
		#print("aa")
		current = open.pop(0)
		closed.append(current)
		depth = len(current[1])
		#print(nextXtiles)
		#print(len(current[1]))
		#print(lookahead)
		if len(current[1]) == lookahead:
			pass
		else:
			qt = QuinaryTree.QuinaryTree(current[0])
			qt.makeleaves(nextXtiles[len(current[1])])
			if qt.left.board != None:
				open.append((qt.left.board, current[1] + "L"))
			if qt.right.board != None:
				open.append((qt.right.board, current[1] + "R"))
			if qt.up.board != None:
				open.append((qt.up.board, current[1] + "U"))
			if qt.down.board != None:
				open.append((qt.down.board, current[1] + "D"))
	#print("open: " + str(len(open)))
	#print("closed: " + str(len(closed)))
	
	count = 0
	count2 = 0
	
	bestadjusted = scorenaive * threes.freespaces(naiveX[1])
	bestpath = naiveX[0]
	
	for o in open:
		if threes.scoreboard(o[0]) >= scorenaive:
			count += 1
			#print(o[0])
			#print(threes.scoreboard(o[0]))
			#print(threes.freespaces(o[0]))
			#print(threes.scoreboard(o[0]) * threes.freespaces(o[0]))
			if threes.scoreboard(o[0]) * threes.freespaces(o[0]) >= bestadjusted:
				count2 += 1
				bestadjusted = threes.scoreboard(o[0]) * threes.freespaces(o[0])
				bestpath = o[1]
	
	#print("")
	return bestpath[0]

def astarmove(board, tiles):
	output = ""
	closed = []
	open = [(board, "")]
	maxscore = threes.scoreboard(board)
	maxpath = ""
	starttime = time.time()
	depth = 0
	
	while len(open) > 0 and time.time() - starttime < 0.19:# and depth < 8:
		current = open.pop(0)
		depth = len(current[1])
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
	
	if len(maxpath) == 0:
		return ""
	return maxpath[0]

# If called from the command line, run main
if __name__ == '__main__':
	if len(sys.argv) != 3:
		print("Usage:\n\tthreesbot.py input output\n")
		print("\tinput\tInput File")
		print("\toutput\tOutput File")
		print("\n")
	else:
		main(sys.argv[1], sys.argv[2])
