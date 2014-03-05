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

def rabim_karp(needle, haystack):
	"""Modulus part of the needle. Then check if the modulus is the same for
	parts of the haystack before naive searching from there until either found
	or failed
	Rinse and Repeat.
	"""
	return False

def knuth_morris_pratt(needle, haystack):
	"build a lookup table of characters in the haystack"
	lookup = [0] * 256
	for i in range(0, len(needle)):
		#print(i)
		#print(needle[i])
		#print(lookup[ord(needle[i])])
		if lookup[ord(needle[i])] is 0:
			lookup[ord(needle[i])] = i + 1
	#print lookup
	pos = 0
	while (pos + len(needle) < len(haystack)):
		#print("pos" + str(pos))
		match = 0
		while (match < len(needle)):
			#print("match" + str(match))
			if needle[match] == haystack[match + pos]:
				#if characters match
				match += 1
			else:
				break
		if match == len(needle):
			return True
		#characters didn't match
		#print("match " + str(match))
		#print("failed on " + needle[match])
		#print("leftmost at " + str(lookup[ord(needle[match])]))
		
		pos += lookup[ord(needle[match])]
	return False

def boyer_moore(needle, haystack):
	return False
