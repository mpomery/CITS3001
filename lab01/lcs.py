if __name__ == '__main__':
	print("Longest Common Subsequence")
	print("Include this and use the functions to find the LCS")
	print("returns the length of the LCS")

def lcs_naive(string1, string2):
	if len(string1) * len(string2) == 0:
		# One string is length 0, so LCS is empty
		return ""
	elif string1[-1] == string2[-1]:
		# Last characters are the same
		#print(string1[0:-1])
		#print(string2[0:-1])
		return lcs_naive(string1[0:-1], string2[0:-1]) + string1[-1]
	else:
		left = lcs_naive(string1[0:-1], string2)
		right = lcs_naive(string1[0:-1], string2)
		if (len(left) > len(right)):
			return left
		else:
			return right

def lcs_dynamic(string1, string2):
	lcs = [[0 for x in range(len(string2) + 1)] for x in range(len(string1) + 1)]
	dir = [["" for x in range(len(string2) + 1)] for x in range(len(string1) + 1)]
	# d = above-let
	# l = left
	# u = above
	for x in range(0, len(string1)):
		for y in range(0, len(string2)):
			if string1[x] == string2[y]:
				lcs[x + 1][y + 1] = lcs[x][y] + 1
				dir[x + 1][y + 1] = "d"
			elif lcs[x][y + 1] >= lcs[x + 1][y]:
				lcs[x + 1][y + 1] = lcs[x][y + 1]
				dir[x + 1][y + 1] = "u"
			else:
				lcs[x + 1][y + 1] = lcs[x + 1][y]
				dir[x + 1][y + 1] = "l"
	x = len(string1)
	y = len(string2)
	ret = ""
	while lcs[x][y] != 0:
		if dir[x][y] == "d":
			ret = string1[x - 1] + ret
			x -= 1
			y -= 1
		elif dir[x][y] == "u":
			x -= 1
		else:
			y -= 1
	return ret

#lcs_dynamic("01101001", "01101001")
lcs_dynamic("01101001", "110110")