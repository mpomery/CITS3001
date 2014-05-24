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
		print("BOARD: " + str(self.board))
		self.score = threes.scoreboard(b)

	def printqt(self):
		print("qt for board:")
		threes.printboard(self.board)
		print("score: " + str(self.score))
		#for i in [self.left, self.right, self.up, self.down]:
		#	if i != None:
		#		threes.printboard(i.board)
		#		print('')
	
	def makeleaves(self, nexttile):
		self.left = QuinaryTree(threes.domove(self.board, "L", nexttile))
		self.right = QuinaryTree(threes.domove(self.board, "R", nexttile))
		self.up = QuinaryTree(threes.domove(self.board, "U", nexttile))
		self.down = QuinaryTree(threes.domove(self.board, "D", nexttile))
