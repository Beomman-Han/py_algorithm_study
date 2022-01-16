T = int(input("케이스의 개수 T를 입력하시오 : "))
for i in range(T) :
	a,b = map(int, input("A, B를 입력하시오 (0 < A, B < 10) : ").split())
	print('Case #%d: %d + %d = %d' %(i+1,a,b,a+b))
