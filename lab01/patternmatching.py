if __name__ == '__main__':
	print("Pattern Matching")
	print("Include this and use the functions to match the pattern")
	print("They return true if the needle is found in the haystack")

def naive(needle, haystack):
	position = 0
	while (position + len(needle) < len(haystack)):
		#print("position" + str(position))
		place = 0
		while (place < len(needle)):
			#print("place" + str(place))
			if needle[place] == haystack[place + position]:
				place += 1
			else:
				break
		if place == len(needle):
			return True
		position += 1
	return False