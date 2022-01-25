
## basic dict looping technique
d = dict(a = 1, b = 2, c = 3)
for k in d:
	print(d[k])

"""
	'View' object
	Tips (dict looping, 'view' object)
	> dict.keys()
	> dict.values()
	> dict.items()

	Q) 'view' object 조사??
	Q) list, tuple, dict memory occupacy 비교??
"""

for k in d.keys():  ## dict.keys()
	print(k)

for v in d.values():  ## dict.values()
	print(v)

for kv in d.items():  ## dict.items()
	print(kv)

for k, v in d.items():  ## with tuple unpacking
	print(k, v)

## 'pros' of view object ** (check!)
d = dict(a = 1, b = 2, c = 3)
vo = d.items()
for kv in vo:
	print(kv)

d['a'] += 3
d['c'] -= 2
d['d'] = 4
for kv in vo:  ## changes are reflected w/o re-init
	print(kv)

## dict comprehension
d1 = dict(a = 1, b = 2, c = 3)
d2 = {k : v*2 for k, v in d1.items()}
d3 = {k+'a' : v*2 for k, v in d2.items()}
print(d1)
print(d2)
print(d3)

d4 = {k : v for k, v in d1.items() if v % 2}
print(d4)

ks = ['a', 'b', 'c', 'd']
vs = [1, 2, 3, 4]
d = {k : v for k, v in zip(ks, vs)}
print(d)

