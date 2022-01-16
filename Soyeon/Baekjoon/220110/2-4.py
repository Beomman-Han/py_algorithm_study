# -*- coding: utf-8 -*-
x = input("x를 입력하시오. (−1000 ≤ x ≤ 1000; x ≠ 0) : ")
y = input("y를 입력하시오. (−1000 ≤ y ≤ 1000; y ≠ 0) : ")
x = int(x)
y = int(y)
if x > 0 and y > 0 :
	print("1")
elif x < 0 and y > 0 :
	print("2")
elif x < 0 and y < 0 :
	print("3")
else :
	print("4") 
