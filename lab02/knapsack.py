if __name__ == '__main__':
	print("0-1 Knapsack")
	print("Include this and use the functions to fill a knapsack with as much")
	print("value as possible. Returns the fille knapsack")

def dynamic_knapsack(weights, values, maxweight):
	# weights - How heavy each item is
	# values - Value of each item
	# maximum weight of our knapsack
	nitems = len(weights)
	#V = [[0] * (maxweight + 1)] * (w + 1)
	V = [[0 for x in range (maxweight + 1)] for x in range (nitems + 1)]
	
	#print(nitems)
	#print(maxweight)
	#print V
	
	for row in range(1, nitems + 1):
		for col in range (1, maxweight + 1):
			if weights[row - 1] <= col:
				V[row][col] = max(V[row - 1][col],
					V[row - 1][col - weights[row - 1]] + values[row - 1])
			else:
				V[row][col] = V[row - 1][col]
			#V[0][0] = 1
			#print V[0]
			#print V[1]
			#print V[2]
			#print V[3]
			#print
	#print V
	return V[nitems][maxweight]