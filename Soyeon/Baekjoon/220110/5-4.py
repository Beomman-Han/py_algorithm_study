a = list()
b = list()
c = 0
for i in range(10) : 
	a.append(int(input()))
	b.append(a[i] % 42)
	if b[i] not in b[0:i] :
		c = c + 1
print(c)
