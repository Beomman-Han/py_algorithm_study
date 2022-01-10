def pattern(N: int) -> list:
	"""Make pattern recursively.

	Parameters
	----------
	N: int
		the size of square (N=3^k)
	
	Returns
	-------
	list:
		list of string (pattern)
	"""

	if N == 3:
		return ['***', '* *', '***']
	
	n = int(N/3)
	l = pattern(n)
	#'{pattern(n)[0]}{pattern(n)[0]}'
	return [ f'{x}{x}{x}' for x in l ] + [ f'{x}{" "*n}{x}' for x in l ] + [ f'{x}{x}{x}' for x in l ]

N = int(input())
print('\n'.join(pattern(N)))
