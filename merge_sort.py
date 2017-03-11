def mergeSort(ent):
	if len(ent) > 1:
		m = math.floor(len(ent)/2)
		L1 = ent[:m]
		L2 = ent[m+1:len(ent)]
		L = merge(mergesort(L1), mergesort(L2))
	return L
print(mergeSort(ent))
