from knapsack import *

#datafile = open('data.csv', 'r')

functions = [dynamic_knapsack]

"""for data in datafile:
	needle, haystack, needleinhay = data.split(",", 3)
	if needleinhay[0] == "T":
		needleinhay = True
	else:
		needleinhay = False
	print("")
	print(data)
	for function in functions:
		found = function(needle, haystack)
		if found == needleinhay:
			print("Correct Output - " + str(function).split(" ", 3)[1])
		else:
			print("Incorrect Output - " + str(function).split(" ", 3)[1])
"""

#weights = [2, 2, 4, 1]
#values = [2, 4, 3, 0]
#max_weight = 4

values = [3, 2, 4]
weights = [2, 2, 3]
max_weight = 5

kvalue = fractional_knapsack(weights, values, max_weight)

print kvalue