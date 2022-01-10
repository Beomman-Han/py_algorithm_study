A = input("A를 입력하시오(100보다 크거나 같고, 1,000보다 작은 자연수) : ")
B = input("B를 입력하시오(100보다 크거나 같고, 1,000보다 작은 자연수) : ")
C = input("C를 입력하시오(100보다 크거나 같고, 1,000보다 작은 자연수) : ")

total = int(A) * int(B) * int(C)
for j in range(10) :
	a = 0
	for i in str(total) :
		if int(i) == int(j) :
			a = a + 1
	print(a)	
