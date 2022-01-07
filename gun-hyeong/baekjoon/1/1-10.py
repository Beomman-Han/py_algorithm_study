a,b,c = input().split(" ")
a = int(a) 
b = int(b)
c = int(c)
if a >= 2 and c <= 10000 :
	print(int((a+b)%c))
	print(int((a/c)+((b%c)%c)))
	print(int((a*b)%c))
	print(int((a%c)*((b%c)%c)))
else:
	print("range : (2 <= A , C <= 10000)")

