from patternmatching import *

datafile = open('data.csv', 'r')

functions = [naive, rabim_karp, knuth_morris_pratt, boyer_moore]

for data in datafile:
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