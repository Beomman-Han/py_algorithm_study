from typing import Iterable, Iterator, Literal

def show_all(s: Iterable[int]) -> None:
	for i in s:
		print(i, end=' ')

st = [2 * i for i in range(1, 10)]
show_all(st)
print()

## 1) generator function
def times2() -> Iterator[int]:
	for i in range(1, 10):
		yield 2 * i

g = times2()
show_all(g)
print()

## 2) generator expression
g = ( i * 2 for i in range(1, 10) )
print(type(g))
show_all(g)
print()

g_list = [ i * 2 for i in range(1, 10) ]
print(type(g_list))

## confirm 'lazy evaluation'
def two() -> Literal[2]:
	print('two')
	return 2

g = (two() * i for i in range(1, 10))
print(next(g))
print(next(g))

g_list = [two() * i for i in range(1, 10)]
g_list = iter(g_list)
print(next(g_list))
print(next(g_list))

## 3) generator expression #2
show_all((2 * i for i in range(1, 10)))
show_all(2 * i for i in range(1, 10))
