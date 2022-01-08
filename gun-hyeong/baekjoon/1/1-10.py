a,b,c = map(int,input().split(" "))

if a >= 2 and c <= 10000 :
	print(int((a+b)%c))
	print(int((a/c)+((b%c)%c)))
	print(int((a*b)%c))
	print(int((a%c)*((b%c)%c)))
else:
	print("range : (2 <= A , C <= 10000)")

