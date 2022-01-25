
## dict.setdefault(key, val)
s = 'robbot'
d = {}
for k in s:  ## my style
	try:
		d[k] += 1
	except KeyError:
		d[k] = 1

for k in s:
	if k in d.keys():
		d[k] += 1
	else:
		d[k] = 1

d = {}
for k in s:
	d[k] = d.setdefault(k, 0) + 1  ## dict method (setdefault(key, val)
print(d)

## defaultdict
from collections import defaultdict

s = 'robbot'
d = defaultdict(int)  ## int() == 0
for k in s:
	d[k] += 1
print(d)

def ret_zero():
	return 0

d = defaultdict(ret_zero)
for k in s:
	d[k] += 1
print(d)

d = defaultdict(lambda: 7)
d['z'] += 1
print(d)
