"""
	Unpacking
	> func(*iterable)
	> func(**dict)
	
	Packing
	> def func(*args)
	> def func(**args)
"""

## Unpacking
def who(a, b, c):
	print(a, b, c)

who(*[1, 2, 3])
who(*'abc')  ## str

d = dict(a = 1, b = 2, c = 3)
who(*d)  ## key
who(**d)  ## value
who(*(d.items()))  ## (key, value)

## Packing
def func(*args):
	print(args)

func()
func(1)
func(1, 2)
func(1, 2, 3)

def func(**args):
	print(args)

func()
func(a = 1)
func(a = 1, b = 2)
func(a = 1, b = 2, c = 3)

def func(*args1, **args2):  ## Q) func(**args2, *args): ??
	print(args1)
	print(args2)

func()
func(1)
func(a = 1)
func(1, a = 1)
func(1, a = 1, b = 2)
func(1, 2, a = 1)
