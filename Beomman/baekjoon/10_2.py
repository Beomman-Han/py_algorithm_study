def fibonacci(N: int) -> int:
	if N == 0:
		return 0
	elif N == 1:
		return 1
	
	return fibonacci(N-1) + fibonacci(N-2)

n = int(input())
print(fibonacci(n))
