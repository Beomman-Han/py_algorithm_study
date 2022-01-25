
## OrderedDict
from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)

od2 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
for kv in od2.items():
	print(kv)

## dict.__eq__, OrderedDict.__eq__ comparison?
d1 = dict(a = 1, b = 2, c = 3)  ## .__eq__
d2 = dict(c = 3, a = 1, b = 2)
print(d1 == d2)

od1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])  ## .__eq__ 
od2 = OrderedDict([('c', 3), ('a', 1), ('b', 2)])
print(od1 == od2)

od = OrderedDict(a = 1, b = 2, c = 3)
vu = od.items()
for kv in vu:
	print(kv)

od.move_to_end('b')  ## move to right end
for kv in vu:
	print(kv)

od.move_to_end('b', last = False)
for kv in vu:
	print(kv)

