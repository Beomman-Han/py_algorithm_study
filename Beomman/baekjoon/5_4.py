numbers = []
for i in range(10):
	num = int(input()) % 42
	if num not in numbers:
		numbers.append(num)
print(len(numbers))
