
names = ['yoon', 'kim', 'jang', 'lee', 'park']
names.sort()
dnames = {}
i = 1
for n in names:
	dnames[i] = n
	i += 1

eo = enumerate(names)
for n in eo:
	print(n)

eo = enumerate(names, 1)  ## second parameter
for n in eo:
	print(n)

for n in eo:  ## != view object, should re-init
	print(n)

dnames = {k : v for k, v in enumerate(names, 1)}
print(dnames)

