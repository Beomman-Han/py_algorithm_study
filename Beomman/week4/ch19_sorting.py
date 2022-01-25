
## basic sorting
ns = [3, 1, 4, 2]
ns.sort()
print(ns)

ns.sort(reverse = True)
print(ns)

## sort with key function
def age(t):
	return t[1]

ns = [('Yoon', 33), ('Lee', 12), ('Park', 29)]
ns.sort(key = age)
print(ns)

ns.sort(key = age, reverse = True)
print(ns)

def name(t):
	return t[0]

ns.sort(key = name, reverse = True)
print(ns)

## with lambda function
ns.sort(key = lambda t: t[0])
print(ns)

## sorted() method (all 'iterable' object possible)
org = [('Yoon', 33), ('Lee', 12), ('Park', 29)]
cpy = sorted(org, key = lambda t : t[1], reverse = True)
print(org)
print(cpy)


