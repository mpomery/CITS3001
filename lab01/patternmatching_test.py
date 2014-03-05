import patternmatching

datafile = open('data.csv', 'r')
for data in datafile:
	needle, haystack, needleinhay = data.split(",", 3)
	if needleinhay[0] == "T":
		needleinhay = True
	else:
		needleinhay = False
	found = patternmatching.naive(needle, haystack)
	print("")
	print(data)
	if found == needleinhay:
		print("Correct Output - naive")
	else:
		print("Incorrect Output - naive")
	found = patternmatching.knuth_morris_pratt(needle, haystack)
	if found == needleinhay:
		print("Correct Output - knuth_morris_pratt")
	else:
		print("Incorrect Output - knuth_morris_pratt")