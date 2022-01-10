def solve(a: list) -> int:
	"""Calculate sum of integers in input list.

	Parameters
	----------
	a: list
		input list which contains integers for summation
	
	Returns
	-------
	int
		sum of integers in 'a'
	"""

	sum_ = 0
	for int_ in a:
		sum_ += int_
		
	return sum_

