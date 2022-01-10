while True :
	a, b = input("A, B를 입력하시오(0 < A, B < 10) : ").split()
	if int(a) == 0 and int(b) == 0 :
		break
	else : 
		print(int(a)+int(b))
