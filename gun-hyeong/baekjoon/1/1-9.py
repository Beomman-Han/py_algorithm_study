a,b = map(int,input().split(" "))


if a >= 1 and b <= 10000 :
	print(a+b)
	print(a-b)
	print(a*b)
	print(int(a/b))
	print(a%b)
else:
	print("range : (1 <= A , B <= 10000)")

