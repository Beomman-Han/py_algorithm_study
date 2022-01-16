# -*- coding: utf-8 -*-
score = input("시험 성적을 입력하시오. (시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수) : ")
score = int(score)
if 90 <= score :
	print("A")
elif 80 <= score :
	print("B")
elif 70 <= score :
	print("C")
elif 60 <= score :
	print("D")
else :
	print("F")
