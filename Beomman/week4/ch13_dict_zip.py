
## dict initiation
empty_d = {} ## not set!
print(type(empty_d))

d = {'a': 1, 'b': 2, 'c': 3}  ## #1
print(d)

d = dict([('a', 1), ('b', 2), ('c', 3)])  ## #2
print(d)

d = dict(a = 1, b = 2, c = 3)  ## #3 (key: str type)
print(d)

#d = dict((['a', 1]))  ## Error!
#d = dict((('a', 1)))  ## Error!
#print(d)

d = dict(zip(['a', 'b', 'c'], [1, 2, 3]))  ## #4 **
print(d)

## In > python3.7 , the order of keys of dict is consistent.
d = {'a': 1, 'b': 2, 'c': 3}
d['d'] = 4
print(d)
for k in d:
	print(d[k])

## zip example
z = zip(['a', 'b', 'c'], [1, 2, 3])  ## 1
for i in z:
	print(i)  ## tuple type!

z = zip(('a', 'b', 'c'), (1, 2, 3))  ## 2
for i in z:
	print(i)

z = zip('abc', [1, 2, 3])  ## 3
for i in z:
	print(i)

c = list(zip('abc', (1, 2, 3), ['one', 'two', 'three']))  ## 4
print(c)
