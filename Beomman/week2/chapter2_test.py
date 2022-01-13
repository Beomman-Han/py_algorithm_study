"""
Object of User defined class is mutable...
Even if it is inherited by immutable object... ex. tuple...
"""

def Test1():
	class Test(tuple):
		"""User defined class <- tuple object
		"""
		pass

	test1 = Test()
	print(f'Test() object \'test1\' loc: {id(test1)}')
	try:
		print(test1.name)
	except AttributeError:
		print("no name...")
	print(f'Add \'test1\' .name attribute')
	test1.name = 'test1'
	print(f'\'test1\' .name : {test1.name}')
	print(f'\'test1\' object loc: {id(test1)}')

	return

def Test2():
	from dataclasses import dataclass
	@dataclass(frozen=True)
	class immutable:
		a: Any
		b: Any
