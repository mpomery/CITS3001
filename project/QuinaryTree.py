class QuinaryTree:
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
			print("")