def rev(x):
	x = int(x[::-1])
	return x

a, b = input().split()
a = rev(a)
b = rev(b)
if a > b :
	print(a)
else : 
	print(b)
