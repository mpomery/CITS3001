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
		print(string1[0:-1])
		print(string2[0:-1])
		return lcs_naive(string1[0:-1], string2[0:-1]) + string1[-1]
	else:
		left = lcs_naive(string1[0:-1], string2)
		right = lcs_naive(string1[0:-1], string2)
		if (len(left) > len(right)):
			return left
		else:
			return right
