import sys

## 'map' function #1 - list object
def pow(n):
	return n ** 2

#st1 = [1, 2, 3]
st1 = [x for x in range(100)]
print(st1)
print(sys.getsizeof(st1))

## Method 1
#st2 = [pow(st1[0]), pow(st1[1]), pow(st1[2])]
st2 = [pow(x) for x in st1]
print(st2)
print(sys.getsizeof(st2))

## Method 2 ('map' function)
#st2 = list(map(pow, st1))
st2 = map(pow, st1)
print(st2) ## generator (in chapter 9)
print(sys.getsizeof(st2))

## 'map' function #2 - tuple, string (all iterable object)
def db1(e):
	return e * 2

print(list(map(db1, (1, 3, 4))))
print(list(map(db1, 'hello')))

## 'map' fnction #3 - multiple object
def sum(n1, n2):
	return n1 + n2

print(list(map(sum, [1, 2, 3], [3, 2, 1])))

def sum2(n1, n2, n3):
	return n1 + n2 + n3

print(list(map(sum2, [1, 2, 3], [3, 2, 1], [1, 1, 1])))

## 'map' function + 'lambda' expression
st = ['one', 'two', 'three']
st2 = list(map(lambda x: x[::-1], st))
print(st2)


## 'filter' funtion + 'lambda' expression
st = list(range(1, 11))
st2 = list(filter(lambda x: not(x % 3), map(lambda x: x ** 2, st)))
print(st2)

## list comprehension
st3 = [ x ** 2 for x in st if not((x ** 2) % 3) ]
print(st3)
