if __name__ == '__main__':
	print("Longest Common Subsequence")
	print("Include this and use the functions to find the LCS")
	print("returns the length of the LCS")

def lcs_naive(string1, string2):
	max = max(len(string1), len(string1))
	if max == 0:
		return 0
	

