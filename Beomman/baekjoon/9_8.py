#dot_list = []
x_cord = dict()
y_cord = dict()
for i in range(3):
	[x, y] = [int(e) for e in input().strip().split()]
	#dot_list.append((x, y))
	try:
		x_cord[x] += 1
	except KeyError:
		x_cord[x] = 1
	
	try:
		y_cord[y] += 1
	except KeyError:
		y_cord[y] = 1

x = [ i for i in x_cord if x_cord[i] == 1 ]
y = [ i for i in y_cord if y_cord[i] == 1 ]

print(x[0], y[0])
