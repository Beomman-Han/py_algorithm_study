N = input("N은 0보다 크거나 같고, 99보다 작거나 같은 정수 N을 입력하시오 : ")
i=1
n=N
if int(N) < 10 :
                N = "0" + N

while True :
	a1 = N[0]
	b1 = N[1]
	N1 = int(a1)+int(b1)
	if N1 < 10 :
                N1 = "0" + str(N1)
	N1 = str(N1)
	a2 = N1[0]
	b2 = N1[1]
	N2 = b1 + b2
	if int(n) == int(N2) :
		print(i)
		break
	else : 
		i = int(i) + 1
		N = N2	
