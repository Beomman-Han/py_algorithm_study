import sys
## module for 'type hinting'
from typing import Iterator, List

## Q) how to write type hinting for generator function ?
## > https://docs.python.org/3.6/library/typing.html#typing.Generator
def gen_num() -> Iterator[int]:
	print('first number')
	yield 1
	print('second number')
	yield 2
	print('third number')
	yield 3

gen = gen_num()
print(type(gen))
print(hasattr(gen, '__next__'))

## 'lazy evaluation'
print(next(gen))  ## 1
print(next(gen))  ## 2
print(next(gen))  ## 3
#print(next(gen))  ## Exception

## generator + for loop
def gen_for() -> Iterator[int]:
	for i in [1, 2, 3]:
		yield i

g = gen_for()
print(next(g))
print(next(g))
print(next(g))

## generator memory usage
def pows(s: list) -> list:
	r = []
	for i in s:
		r.append(i ** 2)
	return r

N = 30
st = pows([x for x in range(1, N)])
for i in st:
	print(i, end=' ')
print()
print(sys.getsizeof(st))

def gpows(s: list) -> Iterator[int]:
	for i in s:
		yield i ** 2

st = gpows([x for x in range(1, N)])
for i in st:
	print(i, end=' ')
print()
print(sys.getsizeof(st))

def get_nums(s: List[int]) -> Iterator[int]:
	#for i in s:
	#	yield i
	yield from s

st = get_nums([x for x in range(1, N)])
for i in st:
	print(i, end=' ')
print()