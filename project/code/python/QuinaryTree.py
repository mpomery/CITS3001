#!/usr/bin/python

# Quinary Tree (QuinaryTree.py)
# Written by Mitchell 'Pommers' Pomery (21130887)
#
# Useful for mapping the different moves that threesbot can make

import threes

class QuinaryTree:
	def __init__(self, b):
		self.left = None
		self.right = None
		self.up = None
		self.down = None
		self.board = b
		self.score = threes.scoreboard(b)

	def printqt(self):
		print("qt for board:")
		threes.printboard(self.board)
		print("score: " + str(self.score))
		for i in [self.left, self.right, self.up, self.down]:
			if i != None:
				threes.printboard(i.board)
				print('')

	def makeleaves(self, tile):
		if self.left == None:
			self.left = QuinaryTree(threes.domove(self.board, "L", tile))
			threes.printboard(self.left.board)
			print("")
		if self.right == None:
			self.right = QuinaryTree(threes.domove(self.board, "R", tile))
			threes.printboard(self.right.board)
			print("")
		if self.up == None:
			self.up = QuinaryTree(threes.domove(self.board, "U", tile))
			threes.printboard(self.up.board)
			print("")
		if self.down == None:
			self.down = QuinaryTree(threes.domove(self.board, "D", tile))
			threes.printboard(self.down.board)
			print("")