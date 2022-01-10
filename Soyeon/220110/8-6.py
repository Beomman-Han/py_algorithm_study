T = int(input())
for i in range(T):
	k = int(input())
	n = int(input())
	a = []
	for m in range(k+1):
		if m == 0:
			b = []
			for x in range(n):
				b.append(x+1)
			a.append(b)
		else:
			b = [1]
			for j in range(1, n) : 
				b.append(b[j-1] + a[m-1][j])
			a.append(b)
	print(int((a[k][n-1])))
