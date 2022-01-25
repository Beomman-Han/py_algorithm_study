from typing import Callable

def func_fac(n: int) -> Callable:
	"""Make function which calculates x ** n

	Parameters
	----------
	n : int
		x ** 'n'
	
	Returns
	-------
	Callable(x)
		function which calculates x ** n
	"""

	def exp(x: int) -> int:
		"""Calculates x ** n
		
		Parameters
		----------
		x : int
			'x' ** n

		Returns
		-------
		int
			value of x ** n
		"""

		return x ** n

	return exp

print(type(func_fac))

fac2 = func_fac(2)
print(fac2(2))

fac3 = func_fac(3)
print(fac3(2))

## Multiple returns from lambda function?
## > https://stackoverflow.com/questions/16674004/python-can-lambda-have-more-than-one-return
f1 = lambda n1, n2: (n1 * n2, n1 + n2)
mul, add = f1(3, 4)
print(mul, add)

