def rev_list(L):
	"""
	input: L, a list
	Modifies L such that its elements are in reverse order
	returns: nothing
	"""
	for i in range(len(L)//2):
		j = len(L) - i - 1
		temp = L[i]
		L[i] = L[j]
		L[j] = temp

L = [1, 2, 3, 4]
rev_list(L)
print(L)
