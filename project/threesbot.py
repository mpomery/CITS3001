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

"""class QuinaryTree:
	def __init__(self, b):
		self.left = None
		self.right = None
		self.up = None
		self.down = None
		self.board = b
		self.score = scoreboard(b)
	
	def printqt(self):
		print("qt for board:")
		printboard(self.board)
		print("score: " + str(self.score))
		for i in [self.left, self.right, self.up, self.down]:
			if i != None:
				printboard(i.board)
				print('')
	
	def makeleaves(self, tile):
		if self.left == None:
			self.left = QuinaryTree(domove(self.board, "L", tile))
			printboard(self.left.board)
			print("")
		if self.right == None:
			self.right = QuinaryTree(domove(self.board, "R", tile))
			printboard(self.right.board)
			print("")
		if self.up == None:
			self.up = QuinaryTree(domove(self.board, "U", tile))
			printboard(self.up.board)
			print("")
		if self.down == None:
			self.down = QuinaryTree(domove(self.board, "D", tile))
			printboard(self.down.board)
			print("")"""

if __name__ == '__main__':
	main()
