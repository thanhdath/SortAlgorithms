i = 2
while i < 100:
	j = 2
	while j <= (i/j):
		if not i%j:
			break
		j = j + 1
		if j > i/j: 
			print(i, " la so nguyen to")
		i = i + 1

print("Good bye!")
