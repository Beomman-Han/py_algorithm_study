
## set
A = {'a', 'b', 'c'}
B = {'a', 'b', 'd'}

"""
	A - B
	A & B
	A | B
	A ^ B
"""

A = set(['a', 'b', 'c'])

## frozenset
A = frozenset(['a', 'd', 'c'])
B = frozenset(['a', 'b', 'd'])
"""
	A - B
	A | B
	A == B
	...
"""

## set comprehension
s1 = {x for x in range(1, 11)}
s2 = {x**2 for x in range(1, 11)}
