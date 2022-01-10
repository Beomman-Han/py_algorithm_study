A = int(input())
B = int(input())
C = int(input())

result = str(A*B*C)
for i in range(10):
	count = 0
	for num in result:
		if str(i) == num:
			count += 1
	print(count)
