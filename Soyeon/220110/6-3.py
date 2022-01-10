def check(X):
	X = str(X)
	
	if len(X) == 3 :
		if int(X[0]) - int(X[1]) == int(X[1]) - int(X[2]) :
			return int(X)
		else : 
			return 0
	elif int(X) == 1000 :
		return 0
	else :	
		return int(X)

N = input("N을 입력하시오 (1,000보다 작거나 같은 자연수 N) : ")
count = 0
for i in range(int(N)) :
	j = check(i+1)
	if j != 0 :
		count = count + 1
print(count)	

