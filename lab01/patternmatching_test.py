import patternmatching

datafile = open('data.csv', 'r')
for data in datafile:
	needle, haystack, needleinhay = data.split(",", 3)
	if needleinhay[0] == "T":
		needleinhay = True
	else:
		needleinhay = False
	found = patternmatching.naive(needle, haystack)
	if found == needleinhay:
		print("Correct Output - naive")
		print(data)
	else:
		print("Incorrect Output - naive")
		print(data)