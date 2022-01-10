X = int(input())
x_list=0
x=0
while x_list < X :
	x += 1
	x_list += x

x_list -= x

if x % 2 == 0:
	i = X - x_list
	j = x - i + 1
else:
	i = x - (X - x_list) + 1
	j = X - x_list

print(f"{i}/{j}")
