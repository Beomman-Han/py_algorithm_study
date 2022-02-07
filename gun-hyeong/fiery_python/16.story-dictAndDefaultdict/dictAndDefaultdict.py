from collections import defaultdict

s = 'robbot'

d= {}

for k in s:
    if k in d:
        d[k] += 1
    else:
        d[k] = 1

print(d)

#setdefault method

d = {} 
for k in s:
    d[k] = d.setdefault(k,0) + 1

print(d)

d = defaultdict(lambda : 0)

for k in s:
    d[k] += 1
print(d)






















































































































































